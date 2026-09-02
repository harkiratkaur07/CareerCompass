import pandas as pd
from pathlib import Path


# Load dataset
dataset_path = (
    Path(__file__).parent
    / "dataset"
    / "careercompass_students.csv"
)

df = pd.read_csv(dataset_path)


print("=" * 60)
print("CAREERCOMPASS DATASET INSPECTION")
print("=" * 60)


# ------------------------------------------------------------
# Basic information
# ------------------------------------------------------------

print("\nDataset shape:")
print(df.shape)


print("\nColumns:")
for column in df.columns:
    print("-", column)


# ------------------------------------------------------------
# Statistical summary
# ------------------------------------------------------------

print("\n\nStatistical summary:")
print(df.describe().round(2))


# ------------------------------------------------------------
# Placement means
# ------------------------------------------------------------

print("\n\nAverage values by placement status:")

placement_means = (
    df.groupby("placement_status")
    .mean(numeric_only=True)
    .round(2)
)

print(placement_means)


# ------------------------------------------------------------
# Correlation with placement
# ------------------------------------------------------------

print("\n\nCorrelation with placement:")

correlations = (
    df.select_dtypes(include="number")
    .corr()["placement_status"]
    .drop("placement_status")
    .sort_values(ascending=False)
)

print(correlations.round(3))


# ------------------------------------------------------------
# Skill statistics
# ------------------------------------------------------------

skill_columns = [
    "excel_score",
    "sql_score",
    "python_score",
    "statistics_score",
    "data_cleaning_score",
    "visualization_score",
    "analytical_thinking_score"
]

print("\n\nSkill statistics:")

print(
    df[skill_columns]
    .describe()
    .loc[["mean", "std", "min", "max"]]
    .round(2)
)


# ------------------------------------------------------------
# Placement count
# ------------------------------------------------------------

print("\n\nPlacement counts:")

print(
    df["placement_status"]
    .value_counts()
    .sort_index()
)


print("\n" + "=" * 60)
print("INSPECTION COMPLETE")
print("=" * 60)