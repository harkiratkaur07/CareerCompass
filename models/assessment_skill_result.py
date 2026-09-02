from config.database import db


class AssessmentSkillResult(db.Model):
    __tablename__ = "assessment_skill_results"

    result_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    assessment_id = db.Column(
        db.Integer,
        db.ForeignKey("assessments.assessment_id"),
        nullable=False
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.skill_id"),
        nullable=False
    )

    questions_attempted = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    correct_answers = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    score_percentage = db.Column(
        db.Numeric(5, 2),
        nullable=True,
        default=0.00
    )

    self_rating = db.Column(
        db.Numeric(3, 2),
        nullable=True
    )