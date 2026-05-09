from core.database import get_db
from exercise.dataset_loaders.sanskrit_loader import load_sentences, _passes_length_filter, _remove_duplicates, _estimate_difficulty, get_statistics, extract_vocabulary
from exercise.models import Sentence, Vocabulary, Exercise
from course.models import Course
from lesson.models import Lesson
from langs.models import Language
from exercise.generator.exercise import ExerciseGenerator
from typing import List, Dict


def get_or_create_language(db, code: str, name: str):

    language = db.query(Language).filter_by(code=code).first()
    if not language:
        language = Language(code=code, name=name)
        db.add(language)
        db.commit()
        print(f"Created Language: {name} ({code})")
    else:
        print(f"Found existing Language {name} ({code})")
    return language

def get_or_create_course(db, language_id: str, title: str, description: str):
    course = db.query(Course).filter(Course.language_id == language_id).first()
    if not course:
        course = Course(
            title=title,
            description=description,
            language_id=language_id,
            )
        db.add(course)
        db.commit()
        db.refresh(course)
        print(f"Created course: {title}")
    else:
        print(f"Found existing course: {title}")
    return course

def get_or_create_lesson(db, course_id: str, title: str):
    lesson = db.query(Lesson).filter(Lesson.course_id == course_id, Lesson.title == title).first()
    if not lesson:
        lesson = Lesson(
            title=title,
            course_id=course_id
        )
        db.add(lesson)
        db.commit()
        db.refresh(lesson)
        print(f"Created lesson: {title}")
    else:
        print(f"Found existing lesson: {title}")
    return lesson

def save_sentences(db, sentences: List[Dict], lesson_id: str = None):
    new_count = 0
    for sent in sentences:
        existing = db.query(Sentence).filter(
            Sentence.en == sent["en"],
            Sentence.sa == sent["sa"]
        ).first()
        
        if not existing:
            new_sentence = Sentence(
                en=sent["en"],
                sa=sent["sa"],
                difficulty=sent.get("difficulty", "intermediate"),
                is_used=False
            )
            db.add(new_sentence)
            new_count += 1
    
    db.commit()
    print(f"Saved {new_count} new sentences")
    return new_count

def create_exercises(db):
    generator = ExerciseGenerator(db)
    
    lesson = db.query(Lesson).first()
    sentences = db.query(Sentence).filter(Sentence.is_used == False).all()
    vocabulary = db.query(Vocabulary).all()
    
    generator.generate_from_sentences(
        lesson_id=lesson.id,
        sentences=sentences[:20],
        types=["translation", "reverse_translation", "fill_blank", "word_ordering"]
    )
    
    generator.generate_from_vocabulary(
        lesson_id=lesson.id,
        words=vocabulary[:20], 
        types=["mcq", "word_matching"]
    )

def save_vocabulary(db, vocab_list: List[Dict], limit: int = 100):
    new_count = 0
    for item in vocab_list[:limit]:
        existing = db.query(Vocabulary).filter(Vocabulary.word == item["word"]).first()
        
        if not existing:
            new_vocab = Vocabulary(
                word=item["word"],
                translation=item.get("translation", ""),
                category=None,
                frequency=str(item["frequency"])
            )
            db.add(new_vocab)
            new_count += 1
    
    db.commit()
    print(f"Saved {new_count} new vocabulary words with translations")
    return new_count


def seed_sanskrit_data():
    print("=" * 50)
    print("Starting Sanskrit Data Seeding")
    print("=" * 50)
    
    db = next(get_db())
    
    try:
        language = get_or_create_language(
            db, 
            code="sa", 
            name="Sanskrit",         )
        
        course = get_or_create_course(
            db,
            language_id=language.id,
            title="Sanskrit for Beginners",
            description="Learn basic Sanskrit through simple sentences",
        )
        
        lesson = get_or_create_lesson(
            db,
            course_id=course.id,
            title="Lesson 1: Basic Sentences",
        )
        
        print("\nLoading sentences from Saamayik dataset...")
        sentences = load_sentences(limit=50, streaming=True)
        print(f"Loaded {len(sentences)} sentences")
        
        print("\nSaving sentences...")
        save_sentences(db, sentences)
        
        print("\nExtracting vocabulary...")
        vocab_list = extract_vocabulary(sentences)
        print(f"Found {len(vocab_list)} unique words")
        
        print("\nSaving vocabulary...")
        save_vocabulary(db, vocab_list, limit=100)
        
        create_exercises(db)

        print("\n" + "=" * 50)
        print("Seeding Completed Successfully!")
        print("=" * 50)
        print(f"\nSummary:")
        print(f"  - Language: {language.name}")
        print(f"  - Course: {course.title}")
        print(f"  - Lesson: {lesson.title}")
        print(f"  - Sentences loaded: {len(sentences)}")
        print(f"  - Vocabulary extracted: {len(vocab_list)}")
        
    except Exception as e:
        print(f"\nError during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()
    



if __name__ == "__main__":
    seed_sanskrit_data()