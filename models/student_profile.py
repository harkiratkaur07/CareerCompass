from config.database import db


class StudentProfile(db.Model):
    __tablename__ = "student_profiles"

    profile_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False,
        unique=True
    )

    cgpa = db.Column(
        db.Numeric(4, 2),
        nullable=True
    )

    active_backlogs = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    academic_trend = db.Column(
        db.Enum("Improving", "Stable", "Declining"),
        nullable=True
    )

    projects_count = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    real_world_project = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    deployed_project = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    internships_count = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    relevant_internship = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    certifications_count = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    has_resume = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    resume_optimized = db.Column(
        db.Boolean,
        nullable=True,
        default=False
    )

    job_applications = db.Column(
        db.Enum("Never", "Occasionally", "Regularly"),
        nullable=True
    )

    interview_preparation = db.Column(
        db.Enum("Not Started", "Basic", "Moderate", "Strong"),
        nullable=True
    )

    mock_interviews = db.Column(
        db.Integer,
        nullable=True,
        default=0
    )

    aptitude_practice = db.Column(
        db.Enum("None", "Beginner", "Moderate", "Strong"),
        nullable=True
    )

    communication_confidence = db.Column(
        db.Enum("Low", "Moderate", "High"),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        nullable=True
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=True
    )