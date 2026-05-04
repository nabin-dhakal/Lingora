from datasets import load_dataset

def main():
    print("=" * 60)
    print("Saamayik Dataset Explorer (Corrected)")
    print("=" * 60)
    
    # Load first 100 examples from train split
    print("\n1. Loading dataset (first 100 examples)...")
    dataset = load_dataset("acomquest/Saamayik", split="train[:100]")
    
    # Basic info
    print(f"\n2. Dataset Info:")
    print(f"   - Examples loaded: {len(dataset)}")
    print(f"   - Columns: {dataset.column_names}")
    
    # Look at first example
    print("\n3. First Example:")
    first = dataset[0]
    print(f"   - English: {first['translation']['en']}")
    print(f"   - Sanskrit: {first['translation']['sa']}")
    
    # Check sentence length distribution
    print("\n4. English sentence lengths (word count):")
    lengths = [len(item['translation']['en'].split()) for item in dataset]
    print(f"   - Shortest: {min(lengths)} words")
    print(f"   - Longest: {max(lengths)} words")
    print(f"   - Average: {sum(lengths) / len(lengths):.1f} words")
    
    # Find very short sentences (beginner friendly)
    print("\n5. Short sentences (≤ 5 English words):")
    short = [item for item in dataset if len(item['translation']['en'].split()) <= 5]
    print(f"   Found: {len(short)} sentences")
    
    for i, item in enumerate(short[:5]):
        print(f"\n   {i+1}. EN: {item['translation']['en']}")
        print(f"      SA: {item['translation']['sa']}")
    
    # Streaming example (no memory limit)
    print("\n6. Streaming mode (first 10 sentences):")
    stream = load_dataset("acomquest/Saamayik", split="train", streaming=True)
    count = 0
    for item in stream:
        if count >= 10:
            break
        print(f"   {count+1}. {item['translation']['en']}")
        count += 1
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()