import csv
from typing import List, Dict
from .base_loader import BaseDatasetLoader

class SanskritDatasetLoader(BaseDatasetLoader):
    def __init__(self, csv_path:str):
        self.csv_path = csv_path

    def load_vocabulary(self) -> List[Dict]:
        vocabulary = []
        
        with open(self.csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vocabulary.append({
                    'word': row['word'],
                    'translation': row['translation'],
                    'category': row['category'],
                })
            return vocabulary
    
    def get_sentences(self):
        return super().get_sentences()