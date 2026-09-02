import pandas as pd

from pathlib import Path

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


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
print("CAREERCOMPASS FEATURE ANALYSIS")
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


combined_with_improvement = (
    combined_features
    + ["improvement_rate"]
)


feature_groups = {
    "Combined": combined_features,
    "Combined + Improvement Rate": combined_with_improvement
}


# ============================================================
# MODEL
# ============================================================

model = Pipeline([
    ("scaler", StandardScaler()),
    (
        "model",
        LogisticRegression(
            random_state=RANDOM_STATE,
            max_iter=1000
        )
    )
])


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
# COMPARE FEATURE SETS
# ============================================================

results = []


for group_name, features in feature_groups.items():

    print("\n" + "=" * 70)
    print(group_name)
    print("=" * 70)

    X = df[features]

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
        "Accuracy Mean": accuracy_mean,
        "Accuracy Std": accuracy_std,
        "Precision Mean": precision_mean,
        "Precision Std": precision_std,
        "Recall Mean": recall_mean,
        "Recall Std": recall_std,
        "F1 Mean": f1_mean,
        "F1 Std": f1_std
    })

    print(f"\nNumber of features: {len(features)}")

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
print("FEATURE SET COMPARISON")
print("=" * 70)

print(
    results_df
    .round(4)
    .to_string(index=False)
)


# ============================================================
# TRAIN FINAL CANDIDATE MODEL
# ============================================================

print("\n\n" + "=" * 70)
print("LOGISTIC REGRESSION COEFFICIENT ANALYSIS")
print("=" * 70)


# We will analyze the improved feature set.
final_features = combined_with_improvement

X = df[final_features]


model.fit(X, y)


# ============================================================
# EXTRACT COEFFICIENTS
# ============================================================

logistic_model = model.named_steps["model"]

coefficients = logistic_model.coef_[0]


coefficient_df = pd.DataFrame({
    "Feature": final_features,
    "Coefficient": coefficients
})


# Add absolute coefficient for sorting
coefficient_df["Absolute Coefficient"] = (
    coefficient_df["Coefficient"].abs()
)


coefficient_df = (
    coefficient_df
    .sort_values(
        by="Absolute Coefficient",
        ascending=False
    )
)


print("\nFeature coefficients:")
print(
    coefficient_df[
        [
            "Feature",
            "Coefficient"
        ]
    ]
    .round(4)
    .to_string(index=False)
)


# ============================================================
# INTERPRETATION
# ============================================================

print("\n\n" + "=" * 70)
print("COEFFICIENT INTERPRETATION")
print("=" * 70)


print("\nPositive coefficients:")
print(
    coefficient_df[
        coefficient_df["Coefficient"] > 0
    ][
        ["Feature", "Coefficient"]
    ]
    .round(4)
    .to_string(index=False)
)


print("\nNegative coefficients:")
print(
    coefficient_df[
        coefficient_df["Coefficient"] < 0
    ][
        ["Feature", "Coefficient"]
    ]
    .round(4)
    .to_string(index=False)
)


# ============================================================
# SAVE RESULTS
# ============================================================

results_path = (
    Path(__file__).parent
    / "feature_set_comparison.csv"
)

coefficients_path = (
    Path(__file__).parent
    / "logistic_coefficients.csv"
)


results_df.to_csv(
    results_path,
    index=False
)


coefficient_df.to_csv(
    coefficients_path,
    index=False
)


print("\n\nFeature comparison saved to:")
print(results_path)

print("\nCoefficients saved to:")
print(coefficients_path)


print("\n" + "=" * 70)
print("FEATURE ANALYSIS COMPLETE")
print("=" * 70)