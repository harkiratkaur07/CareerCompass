from config.database import db


class Question(db.Model):
    __tablename__ = "questions"

    question_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.skill_id"),
        nullable=False
    )

    topic = db.Column(db.String(100), nullable=False)

    difficulty = db.Column(
        db.String(20),
        nullable=False
    )

    question_type = db.Column(
        db.String(50),
        nullable=False
    )

    question_text = db.Column(
        db.Text,
        nullable=False
    )

    correct_answer = db.Column(
        db.String(255),
        nullable=False
    )

    explanation = db.Column(
        db.Text,
        nullable=True
    )

    marks = db.Column(
        db.Integer,
        nullable=True,
        default=1
    )

    created_at = db.Column(
        db.DateTime,
        nullable=True
    )