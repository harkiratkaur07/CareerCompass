from config.database import db


class AssessmentAnswer(db.Model):
    __tablename__ = "assessment_answers"

    answer_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    assessment_question_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "assessment_questions.assessment_question_id"
        ),
        nullable=False,
        unique=True
    )

    selected_answer = db.Column(
        db.String(255),
        nullable=True
    )

    is_correct = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    marks_obtained = db.Column(
        db.Numeric(5, 2),
        nullable=True,
        default=0.00
    )

    answered_at = db.Column(
        db.DateTime,
        nullable=True
    )