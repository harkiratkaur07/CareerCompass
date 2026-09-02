from config.database import db


class Skill(db.Model):
    __tablename__ = "skills"

    skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skill_name = db.Column(db.String(150), unique=True, nullable=False)
    skill_category = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)