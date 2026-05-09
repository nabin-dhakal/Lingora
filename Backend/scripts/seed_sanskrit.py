from core.database import get_db
from exercise.dataset_loaders.sanskrit_loader import load_sentences, _passes_length_filter, _remove_duplicates, _estimate_difficulty, get_statistics, extract_vocabulary
from exercise.models import Sentence, Vocabulary, Exercise
from course.models import Course
from lesson.models import Lesson
from typing import List, Dict


