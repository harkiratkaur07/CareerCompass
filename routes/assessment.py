from flask import Blueprint, session, redirect, url_for,render_template,request

from config.database import db

from models.assessment import Assessment
from models.assessment_question import AssessmentQuestion
from models.assessment_answer import AssessmentAnswer
from models.assessment_skill_result import AssessmentSkillResult
from models.question import Question
from models.question_option import QuestionOption
from models.skill import Skill


assessment = Blueprint("assessment", __name__)
skill_target_score=75

def calculate_skill_results(assessment_id):
    """
    Calculate and save skill-wise performance
    for a completed assessment.
    """

    # Get all questions belonging to this assessment
    assessment_questions = AssessmentQuestion.query.filter_by(
        assessment_id=assessment_id
    ).all()

    # Group question IDs by skill
    skill_data = {}

    for aq in assessment_questions:

        question = Question.query.filter_by(
            question_id=aq.question_id
        ).first()

        if not question:
            continue

        skill_id = question.skill_id

        if skill_id not in skill_data:
            skill_data[skill_id] = {
                "attempted": 0,
                "correct": 0
            }

        # Find student's answer
        answer = AssessmentAnswer.query.filter_by(
            assessment_question_id=aq.assessment_question_id
        ).first()

        if answer:
            skill_data[skill_id]["attempted"] += 1

            if answer.is_correct:
                skill_data[skill_id]["correct"] += 1

    # Save results for each skill
    for skill_id, data in skill_data.items():

        attempted = data["attempted"]
        correct = data["correct"]

        if attempted > 0:
            percentage = round(
                (correct / attempted) * 100,
                2
            )
        else:
            percentage = 0

        # Check if result already exists
        result = AssessmentSkillResult.query.filter_by(
            assessment_id=assessment_id,
            skill_id=skill_id
        ).first()

        if result:
            result.questions_attempted = attempted
            result.correct_answers = correct
            result.score_percentage = percentage

        else:
            result = AssessmentSkillResult(
                assessment_id=assessment_id,
                skill_id=skill_id,
                questions_attempted=attempted,
                correct_answers=correct,
                score_percentage=percentage
            )

            db.session.add(result)

    db.session.commit()

def get_skill_category(score):
    """
    Classify a skill based on its percentage score.
    """

    score = float(score)

    if score >= skill_target_score:
        return "Strong"

    elif score >= 50:
        return "Developing"

    else:
        return "Needs Improvement"

def get_readiness_level(score):
    """
    Classify overall placement readiness
    based on the overall assessment percentage.
    """

    score = float(score)

    if score >= 80:
        return "Highly Ready"

    elif score >= 65:
        return "Moderately Ready"

    elif score >= 50:
        return "Developing"

    else:
        return "Early Preparation"

def get_readiness_explanation(readiness_level, percentage, skill_gaps):
    """
    Generate a personalized explanation for the
    student's overall placement readiness.
    """

    if readiness_level == "Highly Ready":
        explanation = (
            "You demonstrated strong overall performance "
            "across the assessment. Your current results "
            "indicate a strong foundation for placement preparation."
        )

    elif readiness_level == "Moderately Ready":
        explanation = (
            "You have a good foundation across several areas, "
            "but some skills are still below the recommended "
            "target. Strengthening your weaker areas can improve "
            "your placement readiness."
        )

    elif readiness_level == "Developing":
        explanation = (
            "You have developed a foundation in several skills, "
            "but there are important areas that still need improvement. "
            "Focus on your largest skill gaps first to strengthen "
            "your overall placement readiness."
        )

    else:
        explanation = (
            "You are currently building your foundation for placement. "
            "Focus on strengthening the core skills identified in "
            "your assessment before moving toward advanced preparation."
        )

    # Add information about the largest skill gap
    if skill_gaps:
        largest_gap = skill_gaps[0]

        if largest_gap["gap"] > 0:
            explanation += (
                f" Your largest current skill gap is "
                f"{largest_gap['skill_name']} "
                f"({largest_gap['gap']}% below the target)."
            )

    return explanation

def get_recommendation_priority(skill_gap, mistakes, base_priority):
    """
    Calculate a student-specific recommendation priority
    using skill gap, number of mistakes, and base priority.
    """

    skill_gap = float(skill_gap)
    mistakes = int(mistakes)
    base_priority = int(base_priority)

    if skill_gap >= 40 or mistakes >= 3:
        return "High"

    elif skill_gap >= 15 or mistakes >= 2:
        return "Medium"

    else:
        return "Low"

def get_assessment_progress(user_id, current_assessment_id):
    """
    Get completed assessment history for the current student.
    Returns assessment percentages in chronological order.
    """

    assessments = Assessment.query.filter(
        Assessment.user_id == user_id,
        Assessment.status == "Completed"
    ).order_by(
        Assessment.completed_at.asc()
    ).all()

    progress = []

    for assessment_record in assessments:

        # Count questions in this assessment
        total_questions = AssessmentQuestion.query.filter_by(
            assessment_id=assessment_record.assessment_id
        ).count()

        if total_questions == 0:
            continue

        percentage = round(
            (float(assessment_record.total_score) /
             total_questions) * 100,
            2
        )

        progress.append({
            "assessment_id": assessment_record.assessment_id,
            "percentage": percentage,
            "completed_at": assessment_record.completed_at
        })

    return progress

def get_latest_assessment(user_id):
    """
    Get the student's most recently completed assessment.
    """

    return Assessment.query.filter(
        Assessment.user_id == user_id,
        Assessment.status == "Completed"
    ).order_by(
        Assessment.completed_at.desc()
    ).first()

def get_skill_progress(user_id):
    """
    Get skill-wise performance across all completed assessments
    for the current student.
    """

    assessments = Assessment.query.filter(
        Assessment.user_id == user_id,
        Assessment.status == "Completed"
    ).order_by(
        Assessment.completed_at.asc()
    ).all()

    skill_progress = {}

    for assessment_record in assessments:

        results = (
            db.session.query(
                AssessmentSkillResult,
                Skill.skill_name
            )
            .join(
                Skill,
                AssessmentSkillResult.skill_id == Skill.skill_id
            )
            .filter(
                AssessmentSkillResult.assessment_id
                == assessment_record.assessment_id
            )
            .order_by(Skill.skill_id)
            .all()
        )

        for result, skill_name in results:

            if skill_name not in skill_progress:
                skill_progress[skill_name] = {
                    "assessments": [],
                    "scores": []
                }

            skill_progress[skill_name]["assessments"].append(
                assessment_record.assessment_id
            )

            skill_progress[skill_name]["scores"].append(
                float(result.score_percentage)
            )

    return skill_progress

def get_latest_assessment(user_id):
    """
    Get the latest completed assessment for a student.
    """

    latest_assessment = Assessment.query.filter(
        Assessment.user_id == user_id,
        Assessment.status == "Completed"
    ).order_by(
        Assessment.completed_at.desc()
    ).first()

    return latest_assessment

def generate_recommendations(assessment_id):

    query = db.session.execute(
        db.text("""
            SELECT
                q.skill_id,
                q.topic,
                COUNT(*) AS mistakes
            FROM assessment_answers aa
            JOIN assessment_questions aq
                ON aa.assessment_question_id =
                   aq.assessment_question_id
            JOIN questions q
                ON aq.question_id = q.question_id
            WHERE aq.assessment_id = :assessment_id
              AND aa.is_correct = 0
            GROUP BY q.skill_id, q.topic
            ORDER BY mistakes DESC
        """),
        {
            "assessment_id": assessment_id
        }
    ).mappings().all()

    recommendations = []

    for row in query:

        recommendation = db.session.execute(
            db.text("""
                SELECT
                    recommendation_id,
                    skill_id,
                    topic,
                    recommendation_text,
                    priority
                FROM recommendations
                WHERE skill_id = :skill_id
                  AND LOWER(TRIM(topic)) = LOWER(TRIM(:topic))
                ORDER BY priority ASC
                LIMIT 1
            """),
            {
                "skill_id": row["skill_id"],
                "topic": row["topic"]
            }
        ).mappings().first()

        if recommendation:
            skill_result=AssessmentSkillResult.query.filter_by(
                assessment_id=assessment_id,
                skill_id=row["skill_id"]
            ).first()

            if skill_result:
                skill_score=float(
                    skill_result.score_percentage
                )

                skill_gap=max(
                    0,skill_target_score-skill_score
                )
            else:
                skill_gap=0

            student_priority=get_recommendation_priority(
                skill_gap,
                row["mistakes"],
                recommendation["priority"]
            )
            recommendations.append({
                "skill_id": row["skill_id"],
                "topic": row["topic"],
                "mistakes": row["mistakes"],
                "skill_gap":round(skill_gap,2),
                "recommendation_text":
                    recommendation["recommendation_text"],
                "priority":
                    recommendation["priority"],
                "student_priority":student_priority
            })
    priority_order={
        "High":1,
        "Medium":2,
        "Low":3
    }
    recommendations.sort(
        key=lambda x: (
            priority_order[x["student_priority"]],
            x["mistakes"],
            -x["skill_gap"]
        )
    )

    return recommendations

@assessment.route("/start-assessment")
def start_assessment():

    # Student must be logged in
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # Import here to avoid circular import
    from scripts.generate_question import generate_assessment

    user_id = session["user_id"]

    # Temporary: Data Analyst career
    career_id = 1

    assessment_id = generate_assessment(user_id, career_id)

    return redirect(
        url_for(
            "assessment.take_assessment",
            assessment_id=assessment_id,
            question_number=1
        )
    )


@assessment.route("/assessment/<int:assessment_id>/<int:question_number>", methods=["GET", "POST"])
def take_assessment(assessment_id,question_number):

    # Student must be logged in
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # Find the assessment belonging to this student
    assessment_record = Assessment.query.filter_by(
        assessment_id=assessment_id,
        user_id=session["user_id"]
    ).first()

    if not assessment_record:
        return "Assessment not found.", 404

    # Get total number of questions
    total_questions = AssessmentQuestion.query.filter_by(
        assessment_id=assessment_id
    ).count()

    # Make sure question number is valid
    if question_number < 1 or question_number > total_questions:
        return "Invalid question number.", 404

    # Get the requested question
    assessment_question = AssessmentQuestion.query.filter_by(
        assessment_id=assessment_id,
        question_order=question_number
    ).first()

    if not assessment_question:
        return "Question not found.", 404

    # Get the actual question
    question = Question.query.filter_by(
        question_id=assessment_question.question_id
    ).first()

    if not question:
        return "Question not found.", 404

    # Get options
    options = QuestionOption.query.filter_by(
        question_id=question.question_id
    ).order_by(
        QuestionOption.option_label
    ).all()

    # Handle submitted answer
    if request.method == "POST":

        selected_answer = request.form.get("answer")

        if not selected_answer:
            return render_template(
                "assessment.html",
                assessment=assessment_record,
                question=question,
                options=options,
                question_number=question_number,
                total_questions=total_questions,
                error="Please select an answer."
            )

        # Find selected option
        selected_option = QuestionOption.query.filter_by(
            question_id=question.question_id,
            option_label=selected_answer
        ).first()

        if not selected_option:
            return "Invalid answer.", 400

        # Compare option text with stored correct answer
        is_correct = (
            selected_option.option_text.strip()
            == question.correct_answer.strip()
        )

        marks_obtained = question.marks if is_correct else 0

        # Check whether this question has already been answered
        existing_answer = AssessmentAnswer.query.filter_by(
            assessment_question_id=assessment_question.assessment_question_id
        ).first()

        if existing_answer:
            # Update the existing answer instead of creating a duplicate
            existing_answer.selected_answer = selected_answer
            existing_answer.is_correct = is_correct
            existing_answer.marks_obtained = marks_obtained
            existing_answer.answered_at = db.func.now()

        else:
            # Save a new answer
            answer = AssessmentAnswer(
                assessment_question_id=(
                    assessment_question.assessment_question_id
                ),
                selected_answer=selected_answer,
                is_correct=is_correct,
                marks_obtained=marks_obtained,
                answered_at=db.func.now()
            )

            db.session.add(answer)
       
        db.session.commit()

        # Move to next question
        if question_number < total_questions:
            return redirect(
                url_for(
                    "assessment.take_assessment",
                    assessment_id=assessment_id,
                    question_number=question_number + 1
                )
            )

        # Calculate final score
        total_score = db.session.query(
            db.func.coalesce(
                db.func.sum(AssessmentAnswer.marks_obtained),
                0
            )
        ).join(
            AssessmentQuestion,
            AssessmentAnswer.assessment_question_id
            == AssessmentQuestion.assessment_question_id
        ).filter(
            AssessmentQuestion.assessment_id == assessment_id
        ).scalar()

        # Update assessment
        assessment_record.total_score = total_score
        assessment_record.status = "Completed"
        assessment_record.completed_at = db.func.now()

        db.session.commit()

        #Calculate Skill-wise results
        calculate_skill_results(assessment_id)

        return redirect(
            url_for(
                "assessment.results",
                assessment_id=assessment_id
            )
        )
    return render_template(
        "assessment.html",
        assessment=assessment_record,
        question=question,
        options=options,
        question_number=question_number,
        total_questions=total_questions
    )

@assessment.route("/assessment/<int:assessment_id>/results")
def results(assessment_id):
    print("========== RESULTS ROUTE HIT ==========")
    print("ASSESSMENT ID:", assessment_id)
    # Student must be logged in
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # Find the completed assessment belonging to this student
    assessment_record = Assessment.query.filter_by(
        assessment_id=assessment_id,
        user_id=session["user_id"]
    ).first()

    if not assessment_record:
        return "Assessment not found.", 404

    progress=get_assessment_progress(
        session["user_id"],
        assessment_id
    )

    progress_change = None
    #get skill-wise progress
    skill_progress=get_skill_progress(
        session["user_id"]
    )

    if len(progress) >= 2:
        previous_score = progress[-2]["percentage"]
        current_score = progress[-1]["percentage"]

        progress_change = round(
            current_score - previous_score,
            2
        )

    # Get total number of questions
    total_questions = AssessmentQuestion.query.filter_by(
        assessment_id=assessment_id
    ).count()

    if total_questions == 0:
        return "No questions found for this assessment.", 404

    # Calculate overall percentage
    percentage = round(
        (float(assessment_record.total_score) / total_questions) * 100,
        2
    )

    #it will determine overall placement readiness
    readiness_level=get_readiness_level(percentage)

    # Get skill-wise results
    skill_results = (
        db.session.query(
            AssessmentSkillResult,
            Skill.skill_name
        )
        .join(
            Skill,
            AssessmentSkillResult.skill_id == Skill.skill_id
        )
        .filter(
            AssessmentSkillResult.assessment_id == assessment_id
        )
        .order_by(Skill.skill_id)
        .all()
    )

    categorized_results = []

    for result, skill_name in skill_results:
        score=float(result.score_percentage)
        category = get_skill_category(score
        )
        skill_gap=max(0,skill_target_score-score)
        categorized_results.append({
            "skill_name": skill_name,
            "score": score,
            "correct": result.correct_answers,
            "attempted": result.questions_attempted,
            "category": category,
            "target":skill_target_score,
            "gap":round(skill_gap,2)
        })

    # Categorize skills AFTER processing all skill results
    strong_skills = [
        result for result in categorized_results
        if result["category"] == "Strong"
    ]

    developing_skills = [
        result for result in categorized_results
        if result["category"] == "Developing"
    ]

    needs_improvement = [
        result for result in categorized_results
        if result["category"] == "Needs Improvement"
    ]
    skill_gaps=sorted(
        categorized_results,
        key=lambda x:x["gap"],
        reverse=True
    )
    readiness_explanation=get_readiness_explanation(
        readiness_level,percentage,skill_gaps
    )

    # Generate personalized recommendations
    recommendations = generate_recommendations(
        assessment_id
    )

    print("\n========== RECOMMENDATIONS ==========")

    for recommendation in recommendations:
        print(
            recommendation["topic"],
            "| Mistakes:",
            recommendation["mistakes"],
            "| Priority:",
            recommendation["priority"]
        )

    return render_template(
        "results.html",
        assessment=assessment_record,
        total_questions=total_questions,
        percentage=percentage,
        readiness_level=readiness_level,
        readiness_explanation=readiness_explanation,
        skill_results=categorized_results,
        strong_skills=strong_skills,
        developing_skills=developing_skills,
        needs_improvement=needs_improvement,
        skill_gaps=skill_gaps,
        skill_target=skill_target_score,
        recommendations=recommendations,
        progress=progress,
        progress_change=progress_change,
        skill_progress=skill_progress
    )