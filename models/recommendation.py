from config.database import db


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    recommendation_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.skill_id"),
        nullable=False
    )

    topic = db.Column(
        db.String(100),
        nullable=False
    )

    recommendation_text = db.Column(
        db.Text,
        nullable=False
    )

    priority = db.Column(
        db.Integer,
        nullable=True,
        default=1
    )