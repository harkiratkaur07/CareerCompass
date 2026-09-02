from ml.predict import build_feature_vector, predict_placement


# Temporary test profile
class TestProfile:
    cgpa = 8.2
    internships_count = 2
    projects_count = 3
    certifications_count = 2
    aptitude_practice = "Strong"
    communication_confidence = "High"


# Skill scores from a sample student
skill_scores = {
    "Excel & Spreadsheet Analysis": 80,
    "SQL & Database Analysis": 75,
    "Python for Data Analysis": 70,
    "Statistics & Probability": 65,
    "Data Cleaning & Preparation": 60,
    "Data Visualization & BI": 75,
    "Analytical Thinking": 80
}


# Build feature vector
features = build_feature_vector(
    student_profile=TestProfile(),
    skill_scores=skill_scores,
    previous_average=65,
    latest_average=72
)

print("\nFEATURE VECTOR")
print("-------------------------")
print(features)


# Make prediction
result = predict_placement(
    student_profile=TestProfile(),
    skill_scores=skill_scores,
    previous_average=65,
    latest_average=72
)

print("\nML PREDICTION")
print("-------------------------")
print("Prediction:", result["prediction"])
print("Placement Probability:", result["probability"], "%")