import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
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
print("CAREERCOMPASS ML TRAINING")
print("=" * 70)

print(f"\nDataset shape: {df.shape}")


# ============================================================
# TARGET
# ============================================================

target_column = "placement_status"

y = df[target_column]


# ============================================================
# FEATURE GROUPS
# ============================================================

background_features = [
    "cgpa",
    "internships",
    "projects",
    "certifications",
    "aptitude_score",
    "communication_score"
]


skill_features = [
    "excel_score",
    "sql_score",
    "python_score",
    "statistics_score",
    "data_cleaning_score",
    "visualization_score",
    "analytical_thinking_score"
]


combined_features = background_features + skill_features


feature_groups = {
    "Background Only": background_features,
    "CareerCompass Skills Only": skill_features,
    "Combined": combined_features
}


# ============================================================
# MODELS
# ============================================================

models = {

    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        (
            "model",
            LogisticRegression(
                random_state=RANDOM_STATE,
                max_iter=1000
            )
        )
    ]),

    "Decision Tree": DecisionTreeClassifier(
        random_state=RANDOM_STATE,
        max_depth=6
    ),

    "Random Forest": RandomForestClassifier(
        random_state=RANDOM_STATE,
        n_estimators=200,
        max_depth=8,
        min_samples_split=5,
        n_jobs=-1
    )
}


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

train_indices, test_indices = train_test_split(
    df.index,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)


# ============================================================
# RESULTS STORAGE
# ============================================================

results = []


# ============================================================
# TRAIN ALL EXPERIMENTS
# ============================================================

for group_name, features in feature_groups.items():

    print("\n" + "=" * 70)
    print(group_name)
    print("=" * 70)

    X = df[features]

    X_train = X.loc[train_indices]
    X_test = X.loc[test_indices]

    y_train = y.loc[train_indices]
    y_test = y.loc[test_indices]

    print(f"\nNumber of features: {len(features)}")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    for model_name, model in models.items():

        print(f"\nTraining: {model_name}")

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions,
            zero_division=0
        )

        recall = recall_score(
            y_test,
            predictions,
            zero_division=0
        )

        f1 = f1_score(
            y_test,
            predictions,
            zero_division=0
        )

        matrix = confusion_matrix(
            y_test,
            predictions
        )

        results.append({
            "Feature Group": group_name,
            "Model": model_name,
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1 Score": f1
        })

        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1 Score:  {f1:.4f}")

        print("Confusion Matrix:")
        print(matrix)


# ============================================================
# RESULTS TABLE
# ============================================================

results_df = pd.DataFrame(results)

print("\n\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(
    results_df
    .sort_values(
        by="F1 Score",
        ascending=False
    )
    .to_string(index=False)
)


# ============================================================
# SAVE RESULTS
# ============================================================

results_path = (
    Path(__file__).parent
    / "model_results.csv"
)

results_df.to_csv(
    results_path,
    index=False
)

print("\n\nResults saved to:")
print(results_path)

print("\n" + "=" * 70)
print("TRAINING COMPLETE")
print("=" * 70)