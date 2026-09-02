from config.database import db


class Assessment(db.Model):
    __tablename__ = "assessments"

    assessment_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    career_id = db.Column(
        db.Integer,
        nullable=False
    )

    started_at = db.Column(
        db.DateTime,
        nullable=True
    )

    completed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    total_score = db.Column(
        db.Numeric(5, 2),
        nullable=True,
        default=0.00
    )

    status = db.Column(
        db.String(20),
        nullable=True,
        default="In Progress"
    )