from abc import ABC, abstractmethod
from typing import List, Dict

class BaseDatasetLoader(ABC):
    @abstractmethod
    def load_vocabulary(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def get_sentences(self) -> List[Dict]:
        pass