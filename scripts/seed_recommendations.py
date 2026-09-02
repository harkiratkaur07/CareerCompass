from app import app
from config.database import db
from models.recommendation import Recommendation


recommendations = [
    # --------------------------------------------------
    # Excel & Spreadsheet Analysis — Skill 1
    # --------------------------------------------------

    {
        "skill_id": 1,
        "topic": "Basic Excel Formulas",
        "recommendation_text":
            "Practice core Excel formulas such as SUM, COUNT, AVERAGE, MIN, and MAX. Focus on understanding when each formula should be used.",
        "priority": 1
    },

    {
        "skill_id": 1,
        "topic": "IF function",
        "recommendation_text":
            "Practice Excel IF formulas and conditional logic. Focus on correctly defining the condition, value when true, and value when false.",
        "priority": 1
    },

    {
        "skill_id": 1,
        "topic": "Lookup functions",
        "recommendation_text":
            "Practice lookup functions such as VLOOKUP and XLOOKUP. Focus on lookup values, return columns, and exact versus approximate matching.",
        "priority": 1
    },

    {
        "skill_id": 1,
        "topic": "PivotTable analysis",
        "recommendation_text":
            "Practice using PivotTables to summarize and analyze data. Focus on grouping, aggregation, and interpreting summarized results.",
        "priority": 2
    },


    # --------------------------------------------------
    # SQL & Database Analysis — Skill 2
    # --------------------------------------------------

    {
        "skill_id": 2,
        "topic": "Aggregation",
        "recommendation_text":
            "Practice SQL aggregate functions such as COUNT, SUM, AVG, MIN, and MAX, and understand how they summarize data.",
        "priority": 1
    },

    {
        "skill_id": 2,
        "topic": "Filtering with WHERE",
        "recommendation_text":
            "Practice filtering SQL records using WHERE conditions. Pay attention to comparison operators and combining conditions correctly.",
        "priority": 1
    },

    {
        "skill_id": 2,
        "topic": "Subqueries",
        "recommendation_text":
            "Practice SQL subqueries, especially queries that compare values against aggregate results such as AVG, MIN, or MAX.",
        "priority": 1
    },

    {
        "skill_id": 2,
        "topic": "JOIN",
        "recommendation_text":
            "Practice SQL JOIN operations and understand how related rows from multiple tables are combined.",
        "priority": 2
    },


    # --------------------------------------------------
    # Python for Data Analysis — Skill 3
    # --------------------------------------------------

    {
        "skill_id": 3,
        "topic": "Pandas DataFrame Column Selection",
        "recommendation_text":
            "Practice selecting columns from Pandas DataFrames using correct column-selection syntax.",
        "priority": 1
    },

    {
        "skill_id": 3,
        "topic": "Pandas DataFrame Filtering",
        "recommendation_text":
            "Practice filtering Pandas DataFrames using boolean conditions and comparison operators.",
        "priority": 1
    },

    {
        "skill_id": 3,
        "topic": "Pandas Multiple-Condition Filtering",
        "recommendation_text":
            "Practice filtering Pandas DataFrames using multiple conditions. Pay attention to the use of &, |, and parentheses.",
        "priority": 1
    },

    {
        "skill_id": 3,
        "topic": "Pandas groupby",
        "recommendation_text":
            "Practice Pandas groupby operations for grouping records and calculating aggregate results.",
        "priority": 2
    },


    # --------------------------------------------------
    # Statistics & Probability — Skill 4
    # --------------------------------------------------

    {
        "skill_id": 4,
        "topic": "Mean Calculation",
        "recommendation_text":
            "Practice calculating and interpreting the mean of a dataset. Make sure you can apply the formula correctly to different datasets.",
        "priority": 1
    },

    {
        "skill_id": 4,
        "topic": "Median Calculation",
        "recommendation_text":
            "Practice finding the median for datasets with both odd and even numbers of observations.",
        "priority": 1
    },

    {
        "skill_id": 4,
        "topic": "Mode Calculation",
        "recommendation_text":
            "Practice identifying the mode of a dataset and understanding situations where a dataset can have more than one mode.",
        "priority": 1
    },

    {
        "skill_id": 4,
        "topic": "Standard Deviation Interpretation",
        "recommendation_text":
            "Practice interpreting standard deviation as a measure of variability and comparing the spread of different datasets.",
        "priority": 1
    },


    # --------------------------------------------------
    # Data Cleaning & Preparation — Skill 5
    # --------------------------------------------------

    {
        "skill_id": 5,
        "topic": "Missing Value Handling",
        "recommendation_text":
            "Practice identifying missing values and selecting appropriate techniques to handle them, including removal and suitable imputation.",
        "priority": 1
    },

    {
        "skill_id": 5,
        "topic": "Duplicate Record Handling",
        "recommendation_text":
            "Practice detecting and handling duplicate records so that repeated observations do not distort analysis.",
        "priority": 1
    },

    {
        "skill_id": 5,
        "topic": "Inconsistent Value Handling",
        "recommendation_text":
            "Practice identifying inconsistent values and standardizing categories, formats, and representations before analysis.",
        "priority": 1
    },

    {
        "skill_id": 5,
        "topic": "Data validation",
        "recommendation_text":
            "Practice validating datasets for incorrect, missing, inconsistent, or unexpected values before performing analysis.",
        "priority": 2
    },


    # --------------------------------------------------
    # Data Visualization & BI — Skill 6
    # --------------------------------------------------

    {
        "skill_id": 6,
        "topic": "Chart selection",
        "recommendation_text":
            "Practice choosing appropriate charts based on the type of data and the analytical question you want to answer.",
        "priority": 1
    },

    {
        "skill_id": 6,
        "topic": "Business Visualization Choice",
        "recommendation_text":
            "Practice selecting visualizations that communicate business metrics and comparisons clearly to decision-makers.",
        "priority": 1
    },

    {
        "skill_id": 6,
        "topic": "Dashboard design",
        "recommendation_text":
            "Practice designing dashboards with clear KPIs, appropriate visual hierarchy, and a logical arrangement of information.",
        "priority": 1
    },

    {
        "skill_id": 6,
        "topic": "Visualization Interpretation",
        "recommendation_text":
            "Practice interpreting charts and identifying trends, comparisons, and meaningful patterns from visual data.",
        "priority": 1
    },


    # --------------------------------------------------
    # Analytical Thinking — Skill 7
    # --------------------------------------------------

    {
        "skill_id": 7,
        "topic": "Basic Data Insight",
        "recommendation_text":
            "Practice examining data and identifying the most relevant observations, trends, and insights that can support a conclusion.",
        "priority": 1
    },

    {
        "skill_id": 7,
        "topic": "Business Decision Analysis",
        "recommendation_text":
            "Practice using data-driven evidence to evaluate business situations and select appropriate decisions.",
        "priority": 1
    },

    {
        "skill_id": 7,
        "topic": "Comparative analysis",
        "recommendation_text":
            "Practice comparing groups, products, or metrics and explaining the differences using relevant evidence from the data.",
        "priority": 1
    },

    {
        "skill_id": 7,
        "topic": "Root-cause analysis",
        "recommendation_text":
            "Practice identifying possible underlying causes of observed problems rather than focusing only on the immediate symptoms.",
        "priority": 2
    }
]


with app.app_context():

    inserted = 0
    skipped = 0

    for item in recommendations:

        existing = Recommendation.query.filter_by(
            skill_id=item["skill_id"],
            topic=item["topic"]
        ).first()

        if existing:
            skipped += 1
            continue

        recommendation = Recommendation(
            skill_id=item["skill_id"],
            topic=item["topic"],
            recommendation_text=item["recommendation_text"],
            priority=item["priority"]
        )

        db.session.add(recommendation)
        inserted += 1

    db.session.commit()

    print("===================================")
    print("RECOMMENDATION SEED COMPLETE")
    print("===================================")
    print("Recommendations inserted :", inserted)
    print("Recommendations skipped  :", skipped)