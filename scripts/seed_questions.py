from app import app
from config.database import db

from data.question_bank import QUESTIONS

from models.skill import Skill
from models.question import Question
from models.question_option import QuestionOption


def seed_questions():
    inserted_questions = 0
    inserted_options = 0
    skipped_questions = 0

    print("Starting question bank seeding...")
    print()

    for q in QUESTIONS:

        # Find the skill
        skill = Skill.query.filter_by(
            skill_name=q["skill"]
        ).first()

        if not skill:
            print(f"ERROR: Skill not found: {q['skill']}")
            continue

        # Prevent duplicate questions
        existing_question = Question.query.filter_by(
            question_text=q["question_text"]
        ).first()

        if existing_question:
            print(
                f"SKIPPED: Question already exists - "
                f"{q['question_text'][:60]}..."
            )
            skipped_questions += 1
            continue

        # Create question
        question = Question(
            skill_id=skill.skill_id,
            topic=q["topic"],
            difficulty=q["difficulty"],
            question_type=q["question_type"],
            question_text=q["question_text"],
            correct_answer=q["correct_answer"],
            explanation=q["explanation"],
            marks=q["marks"]
        )

        db.session.add(question)

        # Flush so MySQL generates question_id
        db.session.flush()

        inserted_questions += 1

        # Create the four options
        for option in q["options"]:

            question_option = QuestionOption(
                question_id=question.question_id,
                option_label=option["label"],
                option_text=option["text"]
            )

            db.session.add(question_option)

            inserted_options += 1

        print(
            f"Inserted: {q['skill']} | "
            f"{q['difficulty']} | "
            f"{q['topic']}"
        )

    db.session.commit()

    print()
    print("=" * 50)
    print("QUESTION BANK SEEDING COMPLETED")
    print("=" * 50)
    print(f"Questions inserted : {inserted_questions}")
    print(f"Options inserted   : {inserted_options}")
    print(f"Questions skipped   : {skipped_questions}")
    print("=" * 50)


if __name__ == "__main__":

    with app.app_context():
        seed_questions()