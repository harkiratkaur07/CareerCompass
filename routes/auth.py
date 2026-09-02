from flask import Blueprint, render_template, request,session,redirect,url_for
from config.database import db
from models.user import User
from models.student_profile import StudentProfile
from models.assessment import Assessment
from models.assessment_question import AssessmentQuestion
from models.assessment_skill_result import AssessmentSkillResult
from models.skill import Skill

from ml.predict import predict_placement
from ml.insights import generate_ml_insights

from flask_bcrypt import Bcrypt

from routes.assessment import (
    get_latest_assessment,
    get_assessment_progress,
    get_skill_progress,
    get_skill_category,
    get_readiness_level,
    get_readiness_explanation,
    generate_recommendations
)

bcrypt=Bcrypt()
auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Required fields
        if not full_name or not email or not password:
            return render_template(
                "register.html",
                error="All fields are required.",
                full_name=full_name,
                email=email
            )

        # Basic email validation
        if "@" not in email or "." not in email.split("@")[-1]:
            return render_template(
                "register.html",
                error="Please enter a valid email address.",
                full_name=full_name,
                email=email
            )

        # Password length
        if len(password) < 8:
            return render_template(
                "register.html",
                error="Password must contain at least 8 characters.",
                full_name=full_name,
                email=email
            )

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return render_template(
                "register.html",
                error="An account with this email already exists.",
                full_name=full_name,
                email=email
            )

        # Create user
        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        new_user = User(
            full_name=full_name,
            email=email,
            password_hash=hashed_password,
            role="student"
        )

        db.session.add(new_user)
        db.session.commit()

        # -----------------------------------------
        # Create empty student profile
        # -----------------------------------------

        new_profile = StudentProfile(
            user_id=new_user.user_id
        )

        db.session.add(new_profile)
        db.session.commit()

        # -----------------------------------------
        # Log the user in automatically
        # -----------------------------------------

        session["user_id"] = new_user.user_id
        session["user_name"] = new_user.full_name

        print("User successfully registered.")
        print("Student profile created.")

        # Send new user to profile setup
        return redirect(url_for("auth.profile"))

    return render_template(
        "register.html",
        full_name="",
        email=""
    )

@auth.route("/profile", methods=["GET", "POST"])
def profile():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    student_profile = StudentProfile.query.filter_by(
        user_id=user_id
    ).first()

    if request.method == "POST":

        try:
            cgpa = request.form.get("cgpa", "").strip()

            if cgpa:
                cgpa = float(cgpa)

                if cgpa < 0 or cgpa > 10:
                    return render_template(
                        "profile.html",
                        profile=student_profile,
                        error="CGPA must be between 0 and 10."
                    )
            else:
                cgpa = None

            active_backlogs = int(
                request.form.get("active_backlogs", 0)
            )

            projects_count = int(
                request.form.get("projects_count", 0)
            )

            internships_count = int(
                request.form.get("internships_count", 0)
            )

            certifications_count = int(
                request.form.get("certifications_count", 0)
            )

            mock_interviews = int(
                request.form.get("mock_interviews", 0)
            )

            if (
                active_backlogs < 0
                or projects_count < 0
                or internships_count < 0
                or certifications_count < 0
                or mock_interviews < 0
            ):
                return render_template(
                    "profile.html",
                    profile=student_profile,
                    error="Counts cannot be negative."
                )

            academic_trend = request.form.get(
                "academic_trend"
            ) or None

            job_applications = request.form.get(
                "job_applications"
            ) or None

            interview_preparation = request.form.get(
                "interview_preparation"
            ) or None

            aptitude_practice = request.form.get(
                "aptitude_practice"
            ) or None

            communication_confidence = request.form.get(
                "communication_confidence"
            ) or None

            real_world_project = (
                request.form.get("real_world_project") == "on"
            )

            deployed_project = (
                request.form.get("deployed_project") == "on"
            )

            relevant_internship = (
                request.form.get("relevant_internship") == "on"
            )

            has_resume = (
                request.form.get("has_resume") == "on"
            )

            resume_optimized = (
                request.form.get("resume_optimized") == "on"
            )

            if student_profile is None:

                student_profile = StudentProfile(
                    user_id=user_id
                )

                db.session.add(student_profile)

            student_profile.cgpa = cgpa
            student_profile.active_backlogs = active_backlogs
            student_profile.academic_trend = academic_trend

            student_profile.projects_count = projects_count
            student_profile.real_world_project = real_world_project
            student_profile.deployed_project = deployed_project

            student_profile.internships_count = internships_count
            student_profile.relevant_internship = relevant_internship

            student_profile.certifications_count = certifications_count

            student_profile.has_resume = has_resume
            student_profile.resume_optimized = resume_optimized

            student_profile.job_applications = job_applications

            student_profile.interview_preparation = (
                interview_preparation
            )

            student_profile.mock_interviews = mock_interviews

            student_profile.aptitude_practice = (
                aptitude_practice
            )

            student_profile.communication_confidence = (
                communication_confidence
            )

            db.session.commit()

            return redirect(url_for("auth.dashboard"))

        except (ValueError, TypeError):

            db.session.rollback()

            return render_template(
                "profile.html",
                profile=student_profile,
                error="Please enter valid values in all numeric fields."
            )

    return render_template(
        "profile.html",
        profile=student_profile
    )

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Basic validation
        if not email or not password:
            return render_template(
                "login.html",
                error="Email and password are required.",
                email=email
            )

        user = User.query.filter_by(email=email).first()

        if not user:
            return render_template(
            "login.html",
            error="Invalid email or password.",
            email=email
        )

        if not bcrypt.check_password_hash(user.password_hash, password):
            return render_template(
                "login.html",
                error="Invalid email or password.",
                email=email
            )

        session["user_id"] = user.user_id
        session["user_name"] = user.full_name

        #check whether the student has a profile
        student_profile=StudentProfile.query.filter_by(
            user_id=user.user_id
        ).first()

        if student_profile is None:
            return redirect(url_for("auth.profile"))
        return redirect(url_for("auth.dashboard"))
    return render_template(
        "login.html",
        email=""
    )

@auth.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    user_id = session["user_id"]
    student_profile=StudentProfile.query.filter_by(user_id=user_id).first()
    # Get latest completed assessment
    latest_assessment = (
        Assessment.query
        .filter_by(
            user_id=user_id,
            status="Completed"
        )
        .order_by(
            Assessment.completed_at.desc()
        )
        .first()
    )
    # Default values
    total_questions = 0
    percentage = 0
    readiness_level = None
    skill_results = []
    progress = []
    recommendations=[]

    skill_scores={}
    ml_prediction=None
    ml_probability=None

    ml_insights = {
        "strengths": [],
        "focus_areas": []
    }
    if latest_assessment:
        # Total questions in latest assessment
        total_questions = AssessmentQuestion.query.filter_by(
            assessment_id=latest_assessment.assessment_id
        ).count()
        # Overall percentage
        if total_questions > 0:
            percentage = round(
                (
                    float(latest_assessment.total_score)
                    / total_questions
                ) * 100,
                2
            )
        # Placement readiness
        readiness_level = get_readiness_level(
            percentage
        )
        # Get skill-wise results for latest assessment
        skill_results_query = (
            db.session.query(
                AssessmentSkillResult,
                Skill.skill_name
            )
            .join(
                Skill,
                AssessmentSkillResult.skill_id
                == Skill.skill_id
            )
            .filter(
                AssessmentSkillResult.assessment_id
                == latest_assessment.assessment_id
            )
            .order_by(Skill.skill_id)
            .all()
        )
        
        # ---------------------------------------------
        # Prepare skill scores for ML model
        # ---------------------------------------------

        skill_scores = {}

        for result, skill_name in skill_results_query:
            skill_scores[skill_name] = float(
                result.score_percentage or 0
            )

        # Latest assessment average
        latest_average = (
            sum(skill_scores.values())
            / len(skill_scores)
            if skill_scores
            else 0
        )
        for result, skill_name in skill_results_query:
            score = float(result.score_percentage)
            skill_results.append({
                "skill_name": skill_name,
                "score": score,
                "category": get_skill_category(score),
                "correct": result.correct_answers,
                "attempted": result.questions_attempted
            })

        #personalised recommendations
        recommendations=generate_recommendations(
            latest_assessment.assessment_id
        )

        # ---------------------------------------------
        # Find previous completed assessment
        # ---------------------------------------------

        previous_assessment = (
            Assessment.query
            .filter(
                Assessment.user_id == user_id,
                Assessment.status == "Completed",
                Assessment.assessment_id != latest_assessment.assessment_id,
                Assessment.completed_at < latest_assessment.completed_at
            )
            .order_by(
                Assessment.completed_at.desc()
            )
            .first()
        )
        previous_average = None

        if previous_assessment:

            previous_results = (
                AssessmentSkillResult.query
                .filter_by(
                    assessment_id=previous_assessment.assessment_id
                )
                .all()
            )

            previous_scores = [
                float(result.score_percentage or 0)
                for result in previous_results
            ]

            if previous_scores:
                previous_average = (
                    sum(previous_scores)
                    / len(previous_scores)
                )

        # ---------------------------------------------
        # ML placement prediction
        # ---------------------------------------------
    
        if student_profile:
            ml_result = predict_placement(
                student_profile=student_profile,
                skill_scores=skill_scores,
                previous_average=previous_average,
                latest_average=latest_average
            )

            ml_prediction = ml_result["prediction"]
            ml_probability = ml_result["probability"]
            
            ml_insights = generate_ml_insights(
                student_profile=student_profile,
                skill_scores=skill_scores,
                previous_average=previous_average,
                latest_average=latest_average
            )
    # Overall assessment progress
    progress = get_assessment_progress(
        user_id,
        latest_assessment.assessment_id
        if latest_assessment
        else None
    )
    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        latest_assessment=latest_assessment,
        total_questions=total_questions,
        percentage=percentage,
        readiness_level=readiness_level,
        skill_results=skill_results,
        progress=progress,
        recommendations=recommendations,
        ml_prediction=ml_prediction,
        ml_probability=ml_probability,
        ml_insights=ml_insights
    )

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))