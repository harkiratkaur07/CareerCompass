import pandas as pd

from pathlib import Path

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# ============================================================
# CONFIGURATION
# ============================================================

RANDOM_STATE = 42
N_SPLITS = 5


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
print("CAREERCOMPASS CROSS-VALIDATION")
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
# CROSS-VALIDATION
# ============================================================

cv = StratifiedKFold(
    n_splits=N_SPLITS,
    shuffle=True,
    random_state=RANDOM_STATE
)


scoring = [
    "accuracy",
    "precision",
    "recall",
    "f1"
]


# ============================================================
# RESULTS
# ============================================================

results = []


# ============================================================
# RUN EXPERIMENTS
# ============================================================

for group_name, features in feature_groups.items():

    print("\n" + "=" * 70)
    print(group_name)
    print("=" * 70)

    X = df[features]

    for model_name, model in models.items():

        print(f"\nTesting: {model_name}")

        scores = cross_validate(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            n_jobs=-1
        )

        accuracy_mean = scores["test_accuracy"].mean()
        accuracy_std = scores["test_accuracy"].std()

        precision_mean = scores["test_precision"].mean()
        precision_std = scores["test_precision"].std()

        recall_mean = scores["test_recall"].mean()
        recall_std = scores["test_recall"].std()

        f1_mean = scores["test_f1"].mean()
        f1_std = scores["test_f1"].std()

        results.append({
            "Feature Group": group_name,
            "Model": model_name,

            "Accuracy Mean": accuracy_mean,
            "Accuracy Std": accuracy_std,

            "Precision Mean": precision_mean,
            "Precision Std": precision_std,

            "Recall Mean": recall_mean,
            "Recall Std": recall_std,

            "F1 Mean": f1_mean,
            "F1 Std": f1_std
        })

        print(
            f"Accuracy : {accuracy_mean:.4f} "
            f"(± {accuracy_std:.4f})"
        )

        print(
            f"Precision: {precision_mean:.4f} "
            f"(± {precision_std:.4f})"
        )

        print(
            f"Recall   : {recall_mean:.4f} "
            f"(± {recall_std:.4f})"
        )

        print(
            f"F1 Score : {f1_mean:.4f} "
            f"(± {f1_std:.4f})"
        )


# ============================================================
# COMPARISON TABLE
# ============================================================

results_df = pd.DataFrame(results)

print("\n\n" + "=" * 70)
print("CROSS-VALIDATION MODEL COMPARISON")
print("=" * 70)

display_columns = [
    "Feature Group",
    "Model",
    "Accuracy Mean",
    "Precision Mean",
    "Recall Mean",
    "F1 Mean"
]

print(
    results_df[
        display_columns
    ]
    .sort_values(
        by="F1 Mean",
        ascending=False
    )
    .round(4)
    .to_string(index=False)
)


# ============================================================
# SAVE RESULTS
# ============================================================

results_path = (
    Path(__file__).parent
    / "cross_validation_results.csv"
)

results_df.to_csv(
    results_path,
    index=False
)

print("\n\nResults saved to:")
print(results_path)

print("\n" + "=" * 70)
print("CROSS-VALIDATION COMPLETE")
print("=" * 70)
