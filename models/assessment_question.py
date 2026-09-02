from config.database import db


class AssessmentQuestion(db.Model):
    __tablename__ = "assessment_questions"

    assessment_question_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    assessment_id = db.Column(
        db.Integer,
        db.ForeignKey("assessments.assessment_id"),
        nullable=False
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.question_id"),
        nullable=False
    )

    question_order = db.Column(
        db.Integer,
        nullable=False
    )