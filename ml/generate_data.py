import numpy as np
import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

NUM_STUDENTS = 5000
RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clipped_normal(mean, std, minimum, maximum, size):
    """
    Generate normally distributed values while keeping
    them inside the specified range.
    """
    values = np.random.normal(mean, std, size)
    return np.clip(values, minimum, maximum)


def generate_count(mean, minimum, maximum, size):
    """
    Generate integer count values using a Poisson distribution.
    """
    values = np.random.poisson(mean, size)
    return np.clip(values, minimum, maximum).astype(int)


# ============================================================
# GENERATE STUDENT ATTRIBUTES
# ============================================================

def generate_dataset(num_students=NUM_STUDENTS):

    student_ids = [
        f"CC{str(i).zfill(4)}"
        for i in range(1, num_students + 1)
    ]

    # --------------------------------------------------------
    # Academic / background attributes
    # --------------------------------------------------------

    cgpa = np.round(
        clipped_normal(
            mean=7.4,
            std=0.9,
            minimum=5.0,
            maximum=10.0,
            size=num_students
        ),
        2
    )

    internships = generate_count(
        mean=1.2,
        minimum=0,
        maximum=4,
        size=num_students
    )

    projects = generate_count(
        mean=2.2,
        minimum=0,
        maximum=6,
        size=num_students
    )

    certifications = generate_count(
        mean=2.0,
        minimum=0,
        maximum=6,
        size=num_students
    )

    aptitude_score = np.round(
        clipped_normal(
            mean=68,
            std=15,
            minimum=25,
            maximum=100,
            size=num_students
        ),
        2
    )

    communication_score = np.round(
        clipped_normal(
            mean=70,
            std=13,
            minimum=30,
            maximum=100,
            size=num_students
        ),
        2
    )

    # --------------------------------------------------------
    # CareerCompass skill scores
    # --------------------------------------------------------
    #
    # We generate a general underlying ability factor first.
    # This creates realistic correlation between skills.
    # --------------------------------------------------------

    underlying_ability = clipped_normal(
        mean=70,
        std=12,
        minimum=35,
        maximum=95,
        size=num_students
    )

    excel_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(3, 10, num_students),
            0,
            100
        ),
        2
    )

    sql_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(2, 11, num_students),
            0,
            100
        ),
        2
    )

    python_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(0, 12, num_students),
            0,
            100
        ),
        2
    )

    statistics_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(-2, 11, num_students),
            0,
            100
        ),
        2
    )

    data_cleaning_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(0, 12, num_students),
            0,
            100
        ),
        2
    )

    visualization_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(2, 10, num_students),
            0,
            100
        ),
        2
    )

    analytical_thinking_score = np.round(
        np.clip(
            underlying_ability + np.random.normal(1, 11, num_students),
            0,
            100
        ),
        2
    )

    # --------------------------------------------------------
    # Aggregate CareerCompass features
    # --------------------------------------------------------

    skill_columns = [
        excel_score,
        sql_score,
        python_score,
        statistics_score,
        data_cleaning_score,
        visualization_score,
        analytical_thinking_score
    ]

    overall_skill_score = np.round(
        np.mean(skill_columns, axis=0),
        2
    )

    target_score = 75

    skill_gap_average = np.round(
        np.maximum(target_score - overall_skill_score, 0),
        2
    )

    number_of_strong_skills = np.sum(
        np.array(skill_columns) >= 75,
        axis=0
    )

    number_of_weak_skills = np.sum(
        np.array(skill_columns) < 50,
        axis=0
    )

    # --------------------------------------------------------
    # Improvement rate
    # --------------------------------------------------------
    #
    # This represents historical improvement.
    # Positive values indicate improvement.
    # --------------------------------------------------------

    improvement_rate = np.round(
        clipped_normal(
            mean=5,
            std=8,
            minimum=-20,
            maximum=30,
            size=num_students
        ),
        2
    )

    # ========================================================
    # PLACEMENT PROBABILITY
    # ========================================================
    #
    # IMPORTANT:
    #
    # We do NOT use the existing CareerCompass readiness
    # categories to determine placement.
    #
    # Instead, placement probability is influenced by
    # multiple independent factors with noise.
    #
    # This gives the ML model an actual pattern to learn.
    # ========================================================

    score = (
        -1.5

        + 0.35 * (cgpa - 7)

        + 0.20 * internships

        + 0.12 * projects

        + 0.08 * certifications

        + 0.015 * (aptitude_score - 60)

        + 0.012 * (communication_score - 60)

        + 0.012 * (overall_skill_score - 60)

        + 0.025 * improvement_rate

        + 0.08 * number_of_strong_skills

        - 0.10 * number_of_weak_skills

        + np.random.normal(0, 0.8, num_students)
    )

    placement_probability = 1 / (1 + np.exp(-score))

    placement_status = np.random.binomial(
        1,
        placement_probability
    )

    # ========================================================
    # CREATE DATAFRAME
    # ========================================================

    df = pd.DataFrame({
        "student_id": student_ids,

        "cgpa": cgpa,
        "internships": internships,
        "projects": projects,
        "certifications": certifications,

        "aptitude_score": aptitude_score,
        "communication_score": communication_score,

        "excel_score": excel_score,
        "sql_score": sql_score,
        "python_score": python_score,
        "statistics_score": statistics_score,
        "data_cleaning_score": data_cleaning_score,
        "visualization_score": visualization_score,
        "analytical_thinking_score": analytical_thinking_score,

        "overall_skill_score": overall_skill_score,
        "skill_gap_average": skill_gap_average,
        "number_of_strong_skills": number_of_strong_skills,
        "number_of_weak_skills": number_of_weak_skills,

        "improvement_rate": improvement_rate,

        "placement_status": placement_status
    })

    return df


# ============================================================
# SAVE DATASET
# ============================================================

def main():

    df = generate_dataset()

    output_directory = Path(__file__).parent / "dataset"
    output_directory.mkdir(parents=True, exist_ok=True)

    output_file = output_directory / "careercompass_students.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("CareerCompass ML Dataset Generated")
    print("=" * 60)

    print(f"\nRows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nDataset location:")
    print(output_file)

    print("\nPlacement distribution:")
    print(df["placement_status"].value_counts())

    print("\nPlacement percentage:")
    print(
        df["placement_status"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())


if __name__ == "__main__":
    main()