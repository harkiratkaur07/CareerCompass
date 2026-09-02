from flask import Flask, render_template
from config.config import Config
from config.database import db
from models.user import User
from models.skill import Skill
from models.question import Question
from models.question_option import QuestionOption
from models.student_profile import StudentProfile
from routes.auth import auth
from routes.assessment import assessment

from models.assessment import Assessment
from models.assessment_question import AssessmentQuestion
from models.assessment_answer import AssessmentAnswer
from models.assessment_skill_result import AssessmentSkillResult

from models.recommendation import Recommendation



app = Flask(__name__)
app.secret_key=Config.SECRET_KEY
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(auth)

app.register_blueprint(assessment)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)