def generate_ml_insights(
    student_profile,
    skill_scores,
    previous_average,
    latest_average
):
    """
    Generate explainable insights from the student's
    profile and assessment data.

    These are supporting indicators, not claims that
    individual features caused the ML prediction.
    """

    strengths = []
    focus_areas = []

    # ---------------------------------------------
    # Skill-based insights
    # ---------------------------------------------

    for skill_name, score in skill_scores.items():

        if score >= 75:
            strengths.append({
                "name": skill_name,
                "value": f"{score:.2f}%"
            })

        elif score < 50:
            focus_areas.append({
                "name": skill_name,
                "value": f"{score:.2f}%"
            })

    # ---------------------------------------------
    # Profile-based insights
    # ---------------------------------------------

    if student_profile.cgpa is not None:

        if float(student_profile.cgpa) >= 8:
            strengths.append({
                "name": "CGPA",
                "value": f"{float(student_profile.cgpa):.2f}"
            })

        elif float(student_profile.cgpa) < 6:
            focus_areas.append({
                "name": "CGPA",
                "value": f"{float(student_profile.cgpa):.2f}"
            })

    if student_profile.internships_count == 0:

        focus_areas.append({
            "name": "Internship Experience",
            "value": "0 internships"
        })

    elif student_profile.internships_count >= 2:

        strengths.append({
            "name": "Internship Experience",
            "value": f"{student_profile.internships_count} internships"
        })

    if student_profile.projects_count >= 2:

        strengths.append({
            "name": "Projects",
            "value": f"{student_profile.projects_count} projects"
        })

    elif student_profile.projects_count == 0:

        focus_areas.append({
            "name": "Projects",
            "value": "No projects recorded"
        })

    if student_profile.certifications_count >= 2:

        strengths.append({
            "name": "Certifications",
            "value": f"{student_profile.certifications_count} certifications"
        })

    # ---------------------------------------------
    # Communication
    # ---------------------------------------------

    if student_profile.communication_confidence == "High":

        strengths.append({
            "name": "Communication",
            "value": "High"
        })

    elif student_profile.communication_confidence == "Low":

        focus_areas.append({
            "name": "Communication",
            "value": "Low"
        })

    # ---------------------------------------------
    # Improvement trend
    # ---------------------------------------------

    if previous_average is not None:

        improvement_rate = (
            (
                latest_average - previous_average
            )
            / previous_average
        ) * 100 if previous_average != 0 else 0

        if improvement_rate > 5:

            strengths.append({
                "name": "Improvement Trend",
                "value": f"+{improvement_rate:.2f}%"
            })

        elif improvement_rate < -5:

            focus_areas.append({
                "name": "Improvement Trend",
                "value": f"{improvement_rate:.2f}%"
            })

    # ---------------------------------------------
    # Sort skills / indicators
    # ---------------------------------------------

    focus_areas = focus_areas[:5]
    strengths = strengths[:5]

    return {
        "strengths": strengths,
        "focus_areas": focus_areas
    }