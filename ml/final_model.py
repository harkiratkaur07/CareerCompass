import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)


# ============================================================
# CONFIGURATION
# ============================================================

RANDOM_STATE = 42
TEST_SIZE = 0.20


# ============================================================
# LOAD DATASET
# ============================================================

dataset_path = (
    Path(__file__).parent
    / "dataset"
    / "careercompass_students.csv"
)

df = pd.read_csv(dataset_path)

print("=" * 70)
print("CAREERCOMPASS FINAL ML MODEL")
print("=" * 70)

print(f"\nDataset shape: {df.shape}")


# ============================================================
# TARGET
# ============================================================

target_column = "placement_status"

y = df[target_column]


# ============================================================
# FINAL FEATURES
# ============================================================

features = [
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


X = df[features]


print("\nNumber of features:", len(features))

print("\nFeatures used:")

for feature in features:
    print("-", feature)


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)


print("\n" + "=" * 70)
print("TRAIN / TEST SPLIT")
print("=" * 70)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))

print("\nTraining placement distribution:")
print(y_train.value_counts())

print("\nTesting placement distribution:")
print(y_test.value_counts())


# ============================================================
# FINAL MODEL
# ============================================================

model = Pipeline([
    (
        "scaler",
        StandardScaler()
    ),

    (
        "logistic_regression",
        LogisticRegression(
            random_state=RANDOM_STATE,
            max_iter=1000
        )
    )
])


# ============================================================
# TRAIN
# ============================================================

print("\n" + "=" * 70)
print("TRAINING FINAL MODEL")
print("=" * 70)

model.fit(
    X_train,
    y_train
)

print("\nModel training completed.")


# ============================================================
# PREDICTION
# ============================================================

y_pred = model.predict(X_test)

y_probability = model.predict_proba(X_test)[:, 1]


# ============================================================
# EVALUATION
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

confusion = confusion_matrix(
    y_test,
    y_pred
)


print("\n" + "=" * 70)
print("FINAL MODEL PERFORMANCE")
print("=" * 70)

print(f"\nAccuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")


# ============================================================
# CONFUSION MATRIX
# ============================================================

print("\nConfusion Matrix:")

print(confusion)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Not Placed",
            "Placed"
        ]
    )
)


# ============================================================
# SAVE MODEL
# ============================================================

model_path = (
    Path(__file__).parent
    / "placement_model.pkl"
)

joblib.dump(
    model,
    model_path
)


print("\n" + "=" * 70)
print("MODEL SAVED")
print("=" * 70)

print("\nModel location:")
print(model_path)


# ============================================================
# SAMPLE PREDICTIONS
# ============================================================

print("\n" + "=" * 70)
print("SAMPLE PREDICTIONS")
print("=" * 70)

sample_results = pd.DataFrame({
    "Actual": y_test.values[:10],
    "Predicted": y_pred[:10],
    "Placement Probability": y_probability[:10]
})

print(
    sample_results.round(4).to_string(index=False)
)


print("\n" + "=" * 70)
print("FINAL MODEL COMPLETE")
print("=" * 70)