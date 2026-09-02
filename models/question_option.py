from config.database import db


class QuestionOption(db.Model):
    __tablename__ = "question_options"

    option_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.question_id"),
        nullable=False
    )

    option_label = db.Column(
        db.String(1),
        nullable=False
    )

    option_text = db.Column(
        db.Text,
        nullable=False
    )