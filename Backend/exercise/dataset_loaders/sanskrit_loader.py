from datasets import load_dataset
from typing import List, Dict, Optional
import logging

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
    
    logger.info(f"Loading Saamayik dataset with limit={limit}, max_en_words={max_en_words}, max_sa_chars={max_sa_chars}")
    
    collect_target = int(limit * buffer_multiplier)
    
    if streaming:
        logger.info("Using streaming mode (memory efficient)")
        dataset = load_dataset("acomquest/Saamayik", split="train", streaming=True)
    else:
        logger.info("Loading full dataset into memory")
        dataset = load_dataset("acomquest/Saamayik", split="train")
    
    filtered_sentences = []
    
    for idx, item in enumerate(dataset):
        if len(filtered_sentences) >= collect_target:
            logger.info(f"Reached collection target of {collect_target} sentences")
            break
        
        en_text = item["translation"]["en"]
        sa_text = item["translation"]["sa"]
        
        if not _passes_length_filter(en_text, sa_text, min_en_words, max_en_words, max_sa_chars):
            continue
        
        difficulty = _estimate_difficulty(en_text, sa_text, max_en_words, max_sa_chars)
        
        filtered_sentences.append({
            "en": en_text,
            "sa": sa_text,
            "difficulty": difficulty
        })
        
        if len(filtered_sentences) % 50 == 0:
            logger.info(f"Collected {len(filtered_sentences)} sentences so far")
    
    logger.info(f"Removing duplicates from {len(filtered_sentences)} sentences")
    unique_sentences = _remove_duplicates(filtered_sentences)
    logger.info(f"Removed {len(filtered_sentences) - len(unique_sentences)} duplicates")
    
    result = unique_sentences[:limit]
    
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
    en_word_count = len(en_text.split())
    sa_char_count = len(sa_text)
    
    if en_word_count < min_en_words:
        return False
    if en_word_count > max_en_words:
        return False
    if sa_char_count > max_sa_chars:
        return False
    
    return True


def _remove_duplicates(sentences: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen_en = set()
    seen_sa = set()
    unique = []
    
    for item in sentences:
        en_text = item["en"]
        sa_text = item["sa"]
        
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
    en_word_count = len(en_text.split())
    sa_char_count = len(sa_text)
    
    if en_word_count <= 5 and sa_char_count <= 50:
        return "beginner"
    elif en_word_count <= max_en_words and sa_char_count <= max_sa_chars:
        return "intermediate"
    else:
        return "advanced"


def get_statistics(sentences: List[Dict[str, str]]) -> Dict:
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


def extract_vocabulary(sentences: List[Dict[str, str]]) -> List[Dict[str, any]]:
    word_map = {}
    
    for item in sentences:
        en_text = item["en"]
        sa_text = item["sa"]
        
        en_words = en_text.split()
        sa_words = sa_text.split()
        
        min_length = min(len(en_words), len(sa_words))
        
        for i in range(min_length):
            sa_word = sa_words[i].strip(".,!?;:()\"'")
            en_word = en_words[i].strip(".,!?;:()\"'")
            
            if sa_word and en_word:
                if sa_word not in word_map:
                    word_map[sa_word] = {
                        "word": sa_word,
                        "translation": en_word,
                        "frequency": 0
                    }
                word_map[sa_word]["frequency"] += 1
    
    result = list(word_map.values())
    result.sort(key=lambda x: x["frequency"], reverse=True)
    
    return result
