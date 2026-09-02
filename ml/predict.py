import os
import joblib
import pandas as pd


# --------------------------------------------------
# Model configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "placement_model.pkl"
)


FEATURE_COLUMNS = [
    "cgpa",
    "internships",
    "projects",
    "certifications",
    "aptitude_score",
    "communication_score",
    "excel_score",
    "sql_score",
    "python_score",
    "statistics_score",
    "data_cleaning_score",
    "visualization_score",
    "analytical_thinking_score",
    "improvement_rate"
]


# --------------------------------------------------
# Categorical → numerical conversions
# --------------------------------------------------

def get_aptitude_score(aptitude_practice):
    """
    Convert the student's aptitude-practice level
    into the 0–100 scale used by the ML dataset.
    """

    mapping = {
        "None": 0,
        "Beginner": 40,
        "Moderate": 70,
        "Strong": 90
    }

    return mapping.get(aptitude_practice, 0)


def get_communication_score(communication_confidence):
    """
    Convert communication confidence into
    the 0–100 scale used by the ML dataset.
    """

    mapping = {
        "Low": 30,
        "Moderate": 60,
        "High": 90
    }

    return mapping.get(communication_confidence, 0)


# --------------------------------------------------
# Improvement calculation
# --------------------------------------------------

def calculate_improvement_rate(previous_average, latest_average):
    """
    Calculate percentage improvement between
    the previous and latest assessment.

    If there is no previous assessment, improvement
    rate is treated as 0.
    """

    if previous_average is None:
        return 0.0

    if previous_average == 0:
        return 0.0

    improvement = (
        (latest_average - previous_average)
        / previous_average
    ) * 100

    return round(improvement, 2)


# --------------------------------------------------
# Build ML feature vector
# --------------------------------------------------

def build_feature_vector(
    student_profile,
    skill_scores,
    previous_average=None,
    latest_average=0
):
    """
    Build the 14 features expected by the trained
    placement prediction model.
    """

    features = {
        "cgpa": float(student_profile.cgpa or 0),

        "internships": int(
            student_profile.internships_count or 0
        ),

        "projects": int(
            student_profile.projects_count or 0
        ),

        "certifications": int(
            student_profile.certifications_count or 0
        ),

        "aptitude_score": get_aptitude_score(
            student_profile.aptitude_practice
        ),

        "communication_score": get_communication_score(
            student_profile.communication_confidence
        ),

        "excel_score": float(
            skill_scores.get("Excel & Spreadsheet Analysis", 0)
        ),

        "sql_score": float(
            skill_scores.get("SQL & Database Analysis", 0)
        ),

        "python_score": float(
            skill_scores.get("Python for Data Analysis", 0)
        ),

        "statistics_score": float(
            skill_scores.get("Statistics & Probability", 0)
        ),

        "data_cleaning_score": float(
            skill_scores.get("Data Cleaning & Preparation", 0)
        ),

        "visualization_score": float(
            skill_scores.get("Data Visualization & BI", 0)
        ),

        "analytical_thinking_score": float(
            skill_scores.get("Analytical Thinking", 0)
        ),

        "improvement_rate": calculate_improvement_rate(
            previous_average,
            latest_average
        )
    }

    return pd.DataFrame(
        [[features[column] for column in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS
    )


# --------------------------------------------------
# Load model
# --------------------------------------------------

def load_model():
    """
    Load the trained Logistic Regression model.
    """

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"ML model not found at: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


# --------------------------------------------------
# Make prediction
# --------------------------------------------------

def predict_placement(
    student_profile,
    skill_scores,
    previous_average=None,
    latest_average=0
):
    """
    Predict placement status and probability.
    """

    model = load_model()

    features = build_feature_vector(
        student_profile=student_profile,
        skill_scores=skill_scores,
        previous_average=previous_average,
        latest_average=latest_average
    )

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    placement_probability = float(
        probabilities[1] * 100
    )

    return {
        "prediction": int(prediction),
        "probability": round(
            placement_probability,
            2
        )
    }