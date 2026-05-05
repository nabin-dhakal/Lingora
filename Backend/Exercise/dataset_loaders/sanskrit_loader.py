"""
Sanskrit Dataset Loader for Saamayik Corpus

This module handles loading and filtering the Saamayik English-Sanskrit parallel dataset.
It is used ONLY during seeding, never at runtime.

Usage:
    from app.exercise.sanskrit_loader import load_sentences
    
    sentences = load_sentences(limit=150)
    # Returns list of {"en": "...", "sa": "...", "difficulty": "..."}
"""

from datasets import load_dataset
from typing import List, Dict, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_sentences(
    limit: int = 150,
    max_en_words: int = 8,
    max_sa_chars: int = 80,
    min_en_words: int = 1,
    streaming: bool = False,
    buffer_multiplier: float = 1.5
) -> List[Dict[str, str]]:
    """
    Load and filter sentences from Saamayik dataset.
    
    Args:
        limit: Maximum number of sentences to return
        max_en_words: Maximum English word count (filter)
        max_sa_chars: Maximum Sanskrit character count (filter)
        min_en_words: Minimum English word count (filter, avoid empty sentences)
        streaming: If True, use streaming mode (memory efficient)
        buffer_multiplier: Collect extra sentences before dedup to compensate for duplicates
    
    Returns:
        List of dictionaries, each containing:
            - en: English sentence (prompt)
            - sa: Sanskrit sentence (correct answer)
            - difficulty: "beginner", "intermediate", or "advanced"
    
    Raises:
        ValueError: If not enough sentences found after filtering
    """
    
    logger.info(f"Loading Saamayik dataset with limit={limit}, max_en_words={max_en_words}, max_sa_chars={max_sa_chars}")
    
    # Calculate how many to collect before deduplication (oversample)
    collect_target = int(limit * buffer_multiplier)
    
    # Load dataset (train split only)
    if streaming:
        logger.info("Using streaming mode (memory efficient)")
        dataset = load_dataset("acomquest/Saamayik", split="train", streaming=True)
    else:
        logger.info("Loading full dataset into memory")
        dataset = load_dataset("acomquest/Saamayik", split="train")
    
    # Collect filtered sentences
    filtered_sentences = []
    
    for idx, item in enumerate(dataset):
        # Stop when we have enough (plus buffer)
        if len(filtered_sentences) >= collect_target:
            logger.info(f"Reached collection target of {collect_target} sentences")
            break
        
        # Extract English and Sanskrit
        en_text = item["translation"]["en"]
        sa_text = item["translation"]["sa"]
        
        # Apply filters
        if not _passes_length_filter(en_text, sa_text, min_en_words, max_en_words, max_sa_chars):
            continue
        
        # Passed all filters
        difficulty = _estimate_difficulty(en_text, sa_text, max_en_words, max_sa_chars)
        
        filtered_sentences.append({
            "en": en_text,
            "sa": sa_text,
            "difficulty": difficulty
        })
        
        # Log progress periodically
        if len(filtered_sentences) % 50 == 0:
            logger.info(f"Collected {len(filtered_sentences)} sentences so far")
    
    # Remove duplicates
    logger.info(f"Removing duplicates from {len(filtered_sentences)} sentences")
    unique_sentences = _remove_duplicates(filtered_sentences)
    logger.info(f"Removed {len(filtered_sentences) - len(unique_sentences)} duplicates")
    
    # Truncate to exact limit
    result = unique_sentences[:limit]
    
    # Check if we have enough
    if len(result) < limit:
        logger.warning(f"Only found {len(result)} sentences after filtering. Requested {limit}.")
        logger.warning(f"Consider relaxing filters (max_en_words, max_sa_chars) or reducing limit.")
    
    logger.info(f"Successfully loaded {len(result)} sentences")
    return result


def _passes_length_filter(
    en_text: str,
    sa_text: str,
    min_en_words: int,
    max_en_words: int,
    max_sa_chars: int
) -> bool:
    """
    Check if sentence passes length-based filters.
    
    Returns:
        True if sentence should be kept, False otherwise
    """
    # Count English words
    en_word_count = len(en_text.split())
    
    # Count Sanskrit characters
    sa_char_count = len(sa_text)
    
    # Apply filters
    if en_word_count < min_en_words:
        return False
    if en_word_count > max_en_words:
        return False
    if sa_char_count > max_sa_chars:
        return False
    
    return True


def _remove_duplicates(sentences: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Remove duplicate English and Sanskrit sentences.
    
    Uses sets to track seen English and Sanskrit text.
    If English OR Sanskrit sentence has been seen before, the pair is skipped.
    """
    seen_en = set()
    seen_sa = set()
    unique = []
    
    for item in sentences:
        en_text = item["en"]
        sa_text = item["sa"]
        
        # Skip if English or Sanskrit already seen
        if en_text in seen_en or sa_text in seen_sa:
            continue
        
        seen_en.add(en_text)
        seen_sa.add(sa_text)
        unique.append(item)
    
    return unique


def _estimate_difficulty(
    en_text: str,
    sa_text: str,
    max_en_words: int,
    max_sa_chars: int
) -> str:
    """
    Estimate difficulty based on sentence length.
    
    Returns:
        "beginner", "intermediate", or "advanced"
    """
    en_word_count = len(en_text.split())
    sa_char_count = len(sa_text)
    
    # Beginner threshold: <= max_en_words and <= max_sa_chars (already filtered)
    # But we can add intermediate level within those bounds
    
    if en_word_count <= 5 and sa_char_count <= 50:
        return "beginner"
    elif en_word_count <= max_en_words and sa_char_count <= max_sa_chars:
        return "intermediate"
    else:
        return "advanced"


def get_statistics(sentences: List[Dict[str, str]]) -> Dict:
    """
    Get statistics about loaded sentences (useful for debugging).
    
    Args:
        sentences: List returned by load_sentences()
    
    Returns:
        Dictionary with counts, average lengths, difficulty distribution
    """
    if not sentences:
        return {"error": "No sentences provided"}
    
    en_lengths = [len(item["en"].split()) for item in sentences]
    sa_lengths = [len(item["sa"]) for item in sentences]
    
    difficulties = {}
    for item in sentences:
        diff = item["difficulty"]
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    return {
        "total_sentences": len(sentences),
        "avg_en_words": sum(en_lengths) / len(en_lengths),
        "avg_sa_chars": sum(sa_lengths) / len(sa_lengths),
        "min_en_words": min(en_lengths),
        "max_en_words": max(en_lengths),
        "difficulty_distribution": difficulties
    }


# Optional: Quick test when run directly
if __name__ == "__main__":
    print("Testing sanskrit_loader.py")
    print("=" * 50)
    
    # Test with small limit
    test_sentences = load_sentences(limit=10, streaming=True)
    
    print(f"\nLoaded {len(test_sentences)} sentences")
    print("\nFirst 3 examples:")
    
    for i, sent in enumerate(test_sentences[:3]):
        print(f"\n{i+1}. EN: {sent['en']}")
        print(f"   SA: {sent['sa']}")
        print(f"   Difficulty: {sent['difficulty']}")
    
    print("\n" + "=" * 50)
    print("Statistics:")
    stats = get_statistics(test_sentences)
    for key, value in stats.items():
        print(f"  {key}: {value}")