import random
from typing import List, Tuple
from sqlalchemy.orm import Session
from exercise.models import Exercise, Sentence, Vocabulary

class ExerciseGenerator:
    
    def __init__(self, db: Session):
        self.db = db
    
    def generate_from_sentences(self, lesson_id: int, sentences: List[Sentence], 
                                types: List[str] = None, start_index: int = 0):
        if types is None:
            types = ["translation", "reverse_translation"]
        
        exercises = []
        index = start_index
        
        for sentence in sentences:
            for ex_type in types:
                exercise = None
                
                if ex_type == "translation":
                    exercise = self._make_translation(sentence, lesson_id, index)
                elif ex_type == "reverse_translation":
                    exercise = self._make_reverse_translation(sentence, lesson_id, index)
                elif ex_type == "fill_blank":
                    exercise = self._make_fill_blank(sentence, lesson_id, index)
                elif ex_type == "word_ordering":
                    exercise = self._make_word_ordering(sentence, lesson_id, index)
                elif ex_type == "error_correction":
                    exercise = self._make_error_correction(sentence, lesson_id, index)
                
                if exercise:
                    exercises.append(exercise)
                    index += 1
                    
            sentence.is_used = True
        
        self.db.add_all(exercises)
        self.db.commit()
        return exercises
    
    def generate_from_vocabulary(self, lesson_id: int, words: List[Vocabulary],
                                types: List[str] = None, start_index: int = 0):
        if types is None:
            types = ["mcq", "word_matching"]
        
        exercises = []
        index = start_index
        
        if "mcq" in types:
            mcq_exercises = self._make_mcq_batch(words, lesson_id, index)
            exercises.extend(mcq_exercises)
            index += len(mcq_exercises)
        
        if "word_matching" in types:
            matching_exercise = self._make_word_matching(words, lesson_id, index)
            if matching_exercise:
                exercises.append(matching_exercise)
        
        self.db.add_all(exercises)
        self.db.commit()
        return exercises
    
    
    def _make_translation(self, sentence, lesson_id, index):
        return Exercise(
            question=sentence.en,
            answer=sentence.sa,
            lesson_id=lesson_id,
            type="translation",
            order_index=index,
            is_active=True
        )
    
    def _make_reverse_translation(self, sentence, lesson_id, index):
        return Exercise(
            question=sentence.sa,
            answer=sentence.en,
            lesson_id=lesson_id,
            type="reverse_translation",
            order_index=index,
            is_active=True
        )
    
    def _make_fill_blank(self, sentence, lesson_id, index):
        words = sentence.sa.split()
        if len(words) < 3:
            return None
        
        blank_index = random.randint(0, len(words) - 1)
        answer = words[blank_index]
        words[blank_index] = "_____"
        question = " ".join(words)
        
        return Exercise(
            question=f"{sentence.en}\n\nFill the blank: {question}",
            answer=answer,
            lesson_id=lesson_id,
            type="fill_blank",
            order_index=index,
            is_active=True
        )
    
    def _make_word_ordering(self, sentence, lesson_id, index):
        words = sentence.sa.split()
        if len(words) < 3:
            return None
        
        scrambled = words.copy()
        random.shuffle(scrambled)
        question = " ".join(scrambled)
        
        return Exercise(
            question=f"{sentence.en}\n\nArrange correctly: {question}",
            answer=sentence.sa,
            lesson_id=lesson_id,
            type="word_ordering",
            order_index=index,
            is_active=True
        )
    
    def _make_error_correction(self, sentence, lesson_id, index):
        words = sentence.sa.split()
        if len(words) < 3:
            return None
        
        i = random.randint(0, len(words) - 2)
        words[i], words[i+1] = words[i+1], words[i]
        incorrect = " ".join(words)
        
        return Exercise(
            question=f"{sentence.en}\n\nCorrect the error: {incorrect}",
            answer=sentence.sa,
            lesson_id=lesson_id,
            type="error_correction",
            order_index=index,
            is_active=True
        )
    
    
    def _make_mcq_batch(self, words: List[Vocabulary], lesson_id, start_index):
        exercises = []
        all_words = self.db.query(Vocabulary).all()
        
        for idx, word in enumerate(words):
            distractors = [w.translation for w in all_words 
                          if w.id != word.id and w.translation != word.translation]
            
            if len(distractors) < 3:
                continue
            
            choices = random.sample(distractors, 3) + [word.translation]
            random.shuffle(choices)
            
            question = f"What is the translation of '{word.word}'?\n\n"
            for i, choice in enumerate(choices):
                question += f"{i+1}. {choice}\n"
            
            exercise = Exercise(
                question=question,
                answer=word.translation,
                lesson_id=lesson_id,
                type="mcq",
                order_index=start_index + idx,
                is_active=True,
                choices=",".join(choices)
            )
            exercises.append(exercise)
        
        return exercises
    
    def _make_word_matching(self, words: List[Vocabulary], lesson_id, index):
        if len(words) < 5:
            return None
        
        selected = random.sample(words, 5)
        source_words = [w.word for w in selected]
        target_words = [w.translation for w in selected]
        
        random.shuffle(target_words)
        
        question = "Match the words:\n"
        for i, (src, tgt) in enumerate(zip(source_words, target_words)):
            question += f"{i+1}. {src} → {tgt}\n"
        
        answer = ",".join([f"{w.word}:{w.translation}" for w in selected])
        
        return Exercise(
            question=question,
            answer=answer,
            lesson_id=lesson_id,
            type="word_matching",
            order_index=index,
            is_active=True
        )