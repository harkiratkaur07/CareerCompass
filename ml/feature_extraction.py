from config.database import db
from models.student_profile import StudentProfile
from models.assessment import Assessment
from models.assessment_skill_result import AssessmentSkillResult
from models.skill import Skill


def get_student_ml_features(user_id):
    """
    Extract the 14 features required by the CareerCompass
    placement prediction model for a single student.
    """

    # ---------------------------------------------------------
    # 1. Get student profile
    # ---------------------------------------------------------

    profile = StudentProfile.query.filter_by(
        user_id=user_id
    ).first()

    if not profile:
        raise ValueError(
            f"No student profile found for user_id={user_id}"
        )

    # ---------------------------------------------------------
    # 2. Get latest completed assessment
    # ---------------------------------------------------------

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

    if not latest_assessment:
        raise ValueError(
            f"No completed assessment found for user_id={user_id}"
        )

    # ---------------------------------------------------------
    # 3. Get skill results from latest assessment
    # ---------------------------------------------------------

    skill_results = (
        db.session.query(
            Skill.skill_name,
            AssessmentSkillResult.score_percentage
        )
        .join(
            AssessmentSkillResult,
            AssessmentSkillResult.skill_id == Skill.skill_id
        )
        .filter(
            AssessmentSkillResult.assessment_id
            == latest_assessment.assessment_id
        )
        .all()
    )

    # Convert database results into a dictionary
    skill_scores = {}

    for skill_name, score in skill_results:
        skill_scores[skill_name.strip().lower()] = float(score or 0)

    # ---------------------------------------------------------
    # 4. Map CareerCompass skill names to ML features
    # ---------------------------------------------------------

    excel_score = skill_scores.get(
        "excel & spreadsheet analysis",
        0
    )

    sql_score = skill_scores.get(
        "sql & database analysis",
        0
    )

    python_score = skill_scores.get(
        "python for data analysis",
        0
    )

    statistics_score = skill_scores.get(
        "statistics & probability",
        0
    )

    data_cleaning_score = skill_scores.get(
        "data cleaning & preparation",
        0
    )

    visualization_score = skill_scores.get(
        "data visualization & bi",
        0
    )

    analytical_thinking_score = skill_scores.get(
        "analytical thinking",
        0
    )

    # ---------------------------------------------------------
    # 5. Calculate improvement rate
    # ---------------------------------------------------------

    completed_assessments = (
        Assessment.query
        .filter_by(
            user_id=user_id,
            status="Completed"
        )
        .order_by(
            Assessment.completed_at.asc()
        )
        .all()
    )

    improvement_rate = 0.0

    if len(completed_assessments) >= 2:

        first_assessment = completed_assessments[0]
        previous_assessment = completed_assessments[-2]

        first_questions = AssessmentSkillResult.query.filter_by(
            assessment_id=first_assessment.assessment_id
        ).all()

        previous_questions = AssessmentSkillResult.query.filter_by(
            assessment_id=previous_assessment.assessment_id
        ).all()

        # Calculate average skill score for previous assessment
        if previous_questions:
            previous_average = sum(
                float(result.score_percentage or 0)
                for result in previous_questions
            ) / len(previous_questions)
        else:
            previous_average = 0

        # Calculate average skill score for first assessment
        if first_questions:
            first_average = sum(
                float(result.score_percentage or 0)
                for result in first_questions
            ) / len(first_questions)
        else:
            first_average = 0

        improvement_rate = round(
            previous_average - first_average,
            2
        )

    # ---------------------------------------------------------
    # 6. Build the final 14-feature dictionary
    # ---------------------------------------------------------

    features = {
        "cgpa": float(profile.cgpa or 0),

        "internships": int(
            profile.internships_count or 0
        ),

        "projects": int(
            profile.projects_count or 0
        ),

        "certifications": int(
            profile.certifications_count or 0
        ),

        "aptitude_score": float(
            profile.aptitude_score or 0
        ),

        "communication_score": float(
            profile.communication_score or 0
        ),

        "excel_score": excel_score,
        "sql_score": sql_score,
        "python_score": python_score,
        "statistics_score": statistics_score,
        "data_cleaning_score": data_cleaning_score,
        "visualization_score": visualization_score,
        "analytical_thinking_score": analytical_thinking_score,

        "improvement_rate": improvement_rate
    }

    return features