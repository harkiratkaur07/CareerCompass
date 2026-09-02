import json
import random

from app import app
from config.database import db


def generate_sql_aggregation_question(template):
    variables = template["variables"]

    aggregation_map = {
        "AVG": "average",
        "SUM": "total",
        "MAX": "maximum",
        "MIN": "minimum"
    }

    aggregation = random.choice(variables["aggregation"])
    department = random.choice(variables["department"])

    aggregation_name = aggregation_map[aggregation]

    question = (
        f"Given an employees table with columns employee_name, "
        f"department, and salary, which SQL query correctly finds "
        f"the {aggregation_name} salary for employees in the "
        f"{department} department?"
    )

    correct_answer = (
        f"SELECT {aggregation}(salary) "
        f"FROM employees "
        f"WHERE department = '{department}';"
    )

    distractors = [
        (
            f"SELECT {wrong}(salary) "
            f"FROM employees "
            f"WHERE department = '{department}';"
        )
        for wrong in ["SUM", "AVG", "MAX", "MIN"]
        if wrong != aggregation
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    explanation = (
        f"{aggregation} is used to calculate the "
        f"{aggregation_name} salary. The WHERE condition "
        f"restricts the calculation to employees in the "
        f"{department} department."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }


def get_template(template_id):
    query = db.session.execute(
        db.text("""
            SELECT
                template_id,
                skill_id,
                topic,
                difficulty,
                question_type,
                generation_strategy,
                template_text,
                variables,
                answer_rule,
                explanation_rule
            FROM question_templates
            WHERE template_id = :template_id
              AND is_active = TRUE
        """),
        {"template_id": template_id}
    )

    template = query.mappings().first()

    if template is None:
        raise ValueError(
            f"No active template found with ID {template_id}"
        )

    template = dict(template)

    if isinstance(template["variables"], str):
        template["variables"] = json.loads(template["variables"])

    return template

def save_generated_question(generated):
    # Check whether this exact question already exists
    existing = db.session.execute(
        db.text("""
            SELECT question_id
            FROM questions
            WHERE template_id = :template_id
              AND question_text = :question_text
            LIMIT 1
        """),
        {
            "template_id": generated["template_id"],
            "question_text": generated["question"]
        }
    ).first()

    if existing:
        print("\nQuestion already exists. Skipping insertion.")
        return existing[0]

    # Insert question
    result = db.session.execute(
        db.text("""
            INSERT INTO questions (
                skill_id,
                topic,
                difficulty,
                question_type,
                question_text,
                correct_answer,
                explanation,
                marks,
                template_id
            )
            VALUES (
                :skill_id,
                :topic,
                :difficulty,
                :question_type,
                :question_text,
                :correct_answer,
                :explanation,
                :marks,
                :template_id
            )
        """),
        {
            "skill_id": generated["skill_id"],
            "topic": generated["topic"],
            "difficulty": generated["difficulty"],
            "question_type": generated["question_type"],
            "question_text": generated["question"],
            "correct_answer": generated["correct_answer"],
            "explanation": generated["explanation"],
            "marks": generated["marks"],
            "template_id": generated["template_id"]
        }
    )

    question_id = result.lastrowid

    # Insert options
    for i, option in enumerate(generated["options"]):
        label = chr(ord("A") + i)

        db.session.execute(
            db.text("""
                INSERT INTO question_options (
                    question_id,
                    option_label,
                    option_text
                )
                VALUES (
                    :question_id,
                    :option_label,
                    :option_text
                )
            """),
            {
                "question_id": question_id,
                "option_label": label,
                "option_text": option
            }
        )

    db.session.commit()

    print(f"\nQuestion saved successfully!")
    print(f"Question ID: {question_id}")

    return question_id

def generate_pandas_filter_question(template):
    variables = template["variables"]

    column = random.choice(variables["columns"])
    operator = random.choice(variables["operators"])
    value = random.choice(variables["values"][column])

    data = [
        {"employee": "A", "salary": 25000, "experience": 1, "age": 22},
        {"employee": "B", "salary": 40000, "experience": 2, "age": 25},
        {"employee": "C", "salary": 55000, "experience": 4, "age": 30},
        {"employee": "D", "salary": 70000, "experience": 6, "age": 35}
    ]

    dataframe_text = (
        "employee | salary | experience | age\n"
        "---------|--------|------------|----\n"
    )

    for row in data:
        dataframe_text += (
            f"{row['employee']} | "
            f"{row['salary']} | "
            f"{row['experience']} | "
            f"{row['age']}\n"
        )

    correct_answer = (
        f'df[df["{column}"] {operator} {value}]'
    )

    wrong_operators = [
        op for op in variables["operators"]
        if op != operator
    ]

    distractors = [
        f'df[df["{column}"] {wrong_operator} {value}]'
        for wrong_operator in wrong_operators
    ]

    # Ensure exactly 3 distractors
    while len(distractors) < 3:
        alternative_value = random.choice(
            variables["values"][column]
        )

        candidate = (
            f'df[df["{column}"] {operator} '
            f'{alternative_value}]'
        )

        if candidate != correct_answer and candidate not in distractors:
            distractors.append(candidate)

    distractors = distractors[:3]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"Given the following DataFrame:\n\n"
        f"{dataframe_text}\n"
        f"Which Pandas statement correctly selects rows "
        f"where {column} {operator} {value}?"
    )

    explanation = (
        f'The correct Pandas statement is '
        f'df[df["{column}"] {operator} {value}]. '
        f'The condition inside the brackets filters the DataFrame '
        f'and returns only the rows that satisfy the specified condition.'
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_mean_question(template):
    variables = template["variables"]

    dataset_size = random.choice(variables["dataset_size"])
    min_value, max_value = variables["value_range"]

    # Generate integer values
    values = [
        random.randint(min_value, max_value)
        for _ in range(dataset_size)
    ]

    # Calculate the mean
    mean = sum(values) / len(values)

    # Keep the answer easy to read
    mean = round(mean, 2)

    # Create plausible distractors
    distractors = {
        round(mean + 2, 2),
        round(mean - 2, 2),
        round(mean + 5, 2),
        round(mean - 5, 2)
    }

    # Remove the correct answer if it somehow appears
    distractors.discard(mean)

    distractors = list(distractors)[:3]

    # Make sure we have exactly 3 distractors
    while len(distractors) < 3:
        candidate = round(
            mean + random.choice([-1, 1, -3, 3, -4, 4]),
            2
        )

        if candidate != mean and candidate not in distractors:
            distractors.append(candidate)

    correct_answer = str(mean)

    options = [correct_answer] + [
        str(value) for value in distractors
    ]

    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    values_text = ", ".join(str(value) for value in values)

    question = (
        f"Given the following set of values:\n\n"
        f"[{values_text}]\n\n"
        f"What is the arithmetic mean?"
    )

    explanation = (
        f"Add all the values and divide the total by the "
        f"number of values. The sum is {sum(values)} and "
        f"there are {len(values)} values, giving a mean "
        f"of {mean}."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_median_question(template):
    variables = template["variables"]

    dataset_size = random.choice(variables["dataset_size"])
    min_value, max_value = variables["value_range"]

    values = [
        random.randint(min_value, max_value)
        for _ in range(dataset_size)
    ]

    # Sort values to calculate the median
    sorted_values = sorted(values)

    n = len(sorted_values)

    if n % 2 == 1:
        median = sorted_values[n // 2]
    else:
        middle1 = sorted_values[(n // 2) - 1]
        middle2 = sorted_values[n // 2]
        median = (middle1 + middle2) / 2

    median = round(median, 2)

    # Generate plausible distractors
    distractor_candidates = set()

    distractor_candidates.add(
        round(median + 2, 2)
    )
    distractor_candidates.add(
        round(median - 2, 2)
    )
    distractor_candidates.add(
        round(median + 5, 2)
    )
    distractor_candidates.add(
        round(median - 5, 2)
    )

    distractor_candidates.discard(median)

    distractors = list(distractor_candidates)[:3]

    while len(distractors) < 3:
        candidate = round(
            median + random.choice(
                [-1, 1, -3, 3, -4, 4]
            ),
            2
        )

        if (
            candidate != median
            and candidate not in distractors
        ):
            distractors.append(candidate)

    correct_answer = str(median)

    options = [correct_answer] + [
        str(value) for value in distractors
    ]

    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    values_text = ", ".join(
        str(value) for value in values
    )

    question = (
        f"Given the following set of values:\n\n"
        f"[{values_text}]\n\n"
        f"What is the median?"
    )

    explanation = (
        f"First, arrange the values in ascending order: "
        f"{', '.join(map(str, sorted_values))}. "
        f"The median is the middle value of the ordered "
        f"dataset."
    )

    if n % 2 == 0:
        explanation += (
            f" Since there are {n} values, take the average "
            f"of the two middle values. The median is "
            f"{median}."
        )
    else:
        explanation += (
            f" Since there are {n} values, the middle value "
            f"is {median}."
        )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_excel_formula_question(template):
    variables = template["variables"]

    ranges = variables["ranges"]

    selected_range = random.choice(ranges)

    correct_answer = f"=SUM({selected_range})"

    distractors = [
        f"=AVERAGE({selected_range})",
        f"=COUNT({selected_range})",
        f"=MAX({selected_range})"
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"Which Excel formula correctly calculates the "
        f"total of the values in the range {selected_range}?"
    )

    explanation = (
        f"The SUM function adds all numeric values in "
        f"the selected range. Therefore, "
        f"{correct_answer} is the correct formula."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_excel_if_question(template):
    variables = template["variables"]

    thresholds = variables["thresholds"]
    threshold = random.choice(thresholds)

    correct_answer = (
        f'=IF(B2>={threshold},"Pass","Fail")'
    )

    distractors = [
        f'=IF(B2>{threshold},"Pass","Fail")',
        f'=IF(B2<={threshold},"Pass","Fail")',
        f'=IF(B2>={threshold},"Fail","Pass")'
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"A student's score is stored in cell B2. "
        f"A score of {threshold} or above is considered "
        f"a Pass. Which Excel formula correctly displays "
        f"\"Pass\" or \"Fail\"?"
    )

    explanation = (
        f"The IF function checks whether B2 is greater than "
        f"or equal to {threshold}. If the condition is true, "
        f"it returns \"Pass\"; otherwise, it returns \"Fail\"."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_excel_lookup_question(template):
    variables = template["variables"]

    products = variables["products"]
    selected_product = random.choice(products)

    product_code = selected_product["code"]
    product_name = selected_product["name"]

    correct_answer = (
        f'=VLOOKUP("{product_code}",A2:C5,3,FALSE)'
    )

    distractors = [
        f'=VLOOKUP("{product_code}",A2:C5,2,FALSE)',
        f'=VLOOKUP("{product_code}",A2:C5,3,TRUE)',
        f'=VLOOKUP("{product_name}",A2:C5,3,FALSE)'
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    table_text = (
        "Product Code | Product Name | Price\n"
        "-------------|--------------|------\n"
    )

    for product in products:
        table_text += (
            f"{product['code']} | "
            f"{product['name']} | "
            f"{product['price']}\n"
        )

    question = (
        f"Given the following Excel table:\n\n"
        f"{table_text}\n"
        f"Which VLOOKUP formula correctly returns the "
        f"price of product {product_name} "
        f"using product code {product_code}?"
    )

    explanation = (
        f"The first argument searches for the product code "
        f"{product_code}. The range A2:C5 contains the lookup "
        f"table, column 3 contains the price, and FALSE "
        f"ensures an exact match."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_sql_filter_question(template):
    variables = template["variables"]

    column_values={
        "salary":[30000,50000,60000],
        "age":[25,30,35],
        "experience":[2,3,5]
    }

    column = random.choice(variables["columns"])
    operator = random.choice(variables["operators"])
    value = random.choice(column_values[column])

    correct_answer = (
        f"SELECT * FROM employees "
        f"WHERE {column} {operator} {value};"
    )

    wrong_operators = [
        op for op in variables["operators"]
        if op != operator
    ]

    distractors = [
        (
            f"SELECT * FROM employees "
            f"WHERE {column} {wrong_operator} {value};"
        )
        for wrong_operator in wrong_operators[:3]
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"Given an employees table, which SQL query correctly "
        f"selects employees where {column} {operator} {value}?"
    )

    explanation = (
        f"The WHERE clause filters rows based on a condition. "
        f"Here, the condition is {column} {operator} {value}."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_sql_subquery_question(template):
    variables = template["variables"]

    aggregation = random.choice(variables["aggregation"])

    aggregation_map = {
        "AVG": "average",
        "MAX": "maximum",
        "MIN": "minimum"
    }

    aggregation_name = aggregation_map[aggregation]

    correct_answer = (
        f"SELECT employee_name, salary "
        f"FROM employees "
        f"WHERE salary > "
        f"(SELECT {aggregation}(salary) FROM employees);"
    )

    distractors = [
        (
            f"SELECT employee_name, salary "
            f"FROM employees "
            f"WHERE salary {operator} "
            f"(SELECT {aggregation}(salary) FROM employees);"
        )
        for operator in ["<", "<=", "="]
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"Which SQL query correctly finds employees whose "
        f"salary is greater than the {aggregation_name} "
        f"salary of all employees?"
    )

    explanation = (
        f"The subquery calculates the {aggregation_name} "
        f"salary using {aggregation}(salary). The outer "
        f"query then selects employees whose salary is "
        f"greater than that value."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_pandas_column_selection_question(template):
    variables = template["variables"]

    selection_type = random.choice(variables["selection_types"])

    data = [
        {"employee": "A", "salary": 25000, "experience": 1, "age": 22},
        {"employee": "B", "salary": 40000, "experience": 2, "age": 25},
        {"employee": "C", "salary": 55000, "experience": 4, "age": 30},
        {"employee": "D", "salary": 70000, "experience": 6, "age": 35}
    ]

    dataframe_text = (
        "employee | salary | experience | age\n"
        "---------|--------|------------|----\n"
    )

    for row in data:
        dataframe_text += (
            f"{row['employee']} | "
            f"{row['salary']} | "
            f"{row['experience']} | "
            f"{row['age']}\n"
        )

    if selection_type == "single":
        column = random.choice(variables["columns"])

        correct_answer = f'df["{column}"]'

        distractors = [
            f"df[{column}]",
            f'df.{column}()',
            f'df.select("{column}")'
        ]

        question = (
            f"Given the following DataFrame:\n\n"
            f"{dataframe_text}\n"
            f"Which Pandas statement correctly selects the "
            f"`{column}` column?"
        )

        explanation = (
            f'df["{column}"] correctly selects the `{column}` '
            f'column from the DataFrame. Pandas uses square '
            f'brackets with the column name to access a column.'
        )

    else:
        selected_columns = random.sample(
            variables["columns"], 2
        )

        col1, col2 = selected_columns

        correct_answer = (
            f'df[["{col1}", "{col2}"]]'
        )

        distractors = [
            f'df["{col1}", "{col2}"]',
            f'df[{col1}, {col2}]',
            f'df.select("{col1}", "{col2}")'
        ]

        question = (
            f"Given the following DataFrame:\n\n"
            f"{dataframe_text}\n"
            f"Which Pandas statement correctly selects both "
            f"the `{col1}` and `{col2}` columns?"
        )

        explanation = (
            f'df[["{col1}", "{col2}"]] correctly selects multiple '
            f'columns from the DataFrame. Pandas requires a list '
            f'of column names inside the square brackets.'
        )

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_pandas_multi_filter_question(template):
    variables = template["variables"]

    column1, column2 = random.sample(variables["columns"], 2)

    conditions = {
        "salary": [
            (">", 40000),
            (">=", 50000),
            ("<", 60000),
            ("<=", 55000)
        ],
        "experience": [
            (">", 2),
            (">=", 3),
            ("<", 5),
            ("<=", 4)
        ],
        "age": [
            (">", 25),
            (">=", 30),
            ("<", 35),
            ("<=", 30)
        ]
    }

    operator1, value1 = random.choice(conditions[column1])
    operator2, value2 = random.choice(conditions[column2])

    logical_operator = random.choice(["&", "|"])

    data = [
        {"employee": "A", "salary": 25000, "experience": 1, "age": 22},
        {"employee": "B", "salary": 40000, "experience": 2, "age": 25},
        {"employee": "C", "salary": 55000, "experience": 4, "age": 30},
        {"employee": "D", "salary": 70000, "experience": 6, "age": 35}
    ]

    dataframe_text = (
        "employee | salary | experience | age\n"
        "---------|--------|------------|----\n"
    )

    for row in data:
        dataframe_text += (
            f"{row['employee']} | "
            f"{row['salary']} | "
            f"{row['experience']} | "
            f"{row['age']}\n"
        )

    question = (
        f"Given the following DataFrame:\n\n"
        f"{dataframe_text}\n"
        f"Which Pandas statement correctly selects rows where "
        f"{column1} {operator1} {value1} "
        f"{logical_operator} "
        f"{column2} {operator2} {value2}?"
    )

    correct_answer = (
        f'df[(df["{column1}"] {operator1} {value1}) '
        f'{logical_operator} '
        f'(df["{column2}"] {operator2} {value2})]'
    )

    wrong_logical_operator = "|" if logical_operator == "&" else "&"

    distractors = [
        f'df[df["{column1}"] {operator1} {value1} '
        f'{logical_operator} df["{column2}"] {operator2} {value2}]',

        f'df[(df["{column1}"] {operator1} {value1}) '
        f'{wrong_logical_operator} '
        f'(df["{column2}"] {operator2} {value2})]',

        f'df[(df["{column1}"] {operator1} {value1}) '
        f'and (df["{column2}"] {operator2} {value2})]'
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    explanation = (
        "Pandas uses boolean conditions inside DataFrame filtering. "
        "When combining multiple conditions, each condition should be "
        "placed in parentheses and Pandas uses '&' for AND or '|' for OR."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_mode_question(template):
    variables = template["variables"]

    min_value, max_value = variables["value_range"]
    dataset_size = random.choice(variables["dataset_size"])

    # Choose a value that will appear multiple times
    mode = random.randint(min_value, max_value)

    # Generate the remaining values
    values = []

    while len(values) < dataset_size - 3:
        value = random.randint(min_value, max_value)

        if value != mode:
            values.append(value)

    # Add the mode three times
    values.extend([mode, mode, mode])

    # Shuffle the dataset
    random.shuffle(values)

    # Generate plausible distractors
    distractors = set()

    distractors.add(mode + 1)
    distractors.add(mode - 1)
    distractors.add(mode + 5)
    distractors.add(mode - 5)

    distractors.discard(mode)

    distractors = list(distractors)[:3]

    # Make sure we have exactly 3 distractors
    while len(distractors) < 3:
        candidate = mode + random.choice(
            [-2, 2, -3, 3, -4, 4]
        )

        if (
            candidate != mode
            and candidate not in distractors
            and min_value <= candidate <= max_value
        ):
            distractors.append(candidate)

    correct_answer = str(mode)

    options = [correct_answer] + [
        str(value) for value in distractors
    ]

    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    values_text = ", ".join(
        str(value) for value in values
    )

    question = (
        f"Given the following set of values:\n\n"
        f"[{values_text}]\n\n"
        f"What is the mode?"
    )

    explanation = (
        f"The mode is the value that occurs most frequently "
        f"in a dataset. In this dataset, {mode} occurs "
        f"three times, making {mode} the mode."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_std_interpretation_question(template):
    variables = template["variables"]

    mean = random.choice(variables["means"])
    std_a = random.choice(variables["std_values"])
    std_b = random.choice(
        [value for value in variables["std_values"] if value != std_a]
    )

    # Make sure Dataset B has the larger standard deviation
    if std_a > std_b:
        std_a, std_b = std_b, std_a

    question = (
        f"Two datasets have the same mean of {mean}. "
        f"Dataset A has a standard deviation of {std_a}, "
        f"while Dataset B has a standard deviation of {std_b}. "
        f"Which statement is correct?"
    )

    correct_answer = (
        "Dataset B has greater variability because its "
        "standard deviation is higher."
    )

    distractors = [
        "Dataset A has greater variability because its "
        "standard deviation is lower.",
        "Both datasets have the same variability because "
        "their means are the same.",
        "Standard deviation cannot be used to compare "
        "the variability of two datasets."
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    explanation = (
        f"Standard deviation measures how spread out values are "
        f"around the mean. Dataset B has a standard deviation of "
        f"{std_b}, which is greater than Dataset A's {std_a}. "
        f"Therefore, Dataset B has greater variability."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_pandas_missing_value_question(template):
    variables = template["variables"]

    column = random.choice(variables["columns"])
    method = random.choice(variables["replacement_methods"])

    data = {
        "salary": [25000, None, 55000, 70000],
        "age": [22, None, 30, 35],
        "experience": [1, None, 4, 6]
    }

    values = data[column]

    if method == "mean":
        correct_answer = (
            f'df["{column}"].fillna(df["{column}"].mean())'
        )
        method_text = "the column's mean"

    elif method == "median":
        correct_answer = (
            f'df["{column}"].fillna(df["{column}"].median())'
        )
        method_text = "the column's median"

    else:
        correct_answer = f'df["{column}"].fillna(0)'
        method_text = "0"

    all_possible_answers = [
        f'df["{column}"].fillna(df["{column}"].mean())',
        f'df["{column}"].fillna(df["{column}"].median())',
        f'df["{column}"].fillna(0)',
        f'df["{column}"].dropna()'
    ]

    distractors = [
        answer
        for answer in all_possible_answers
        if answer != correct_answer
    ]

    random.shuffle(distractors)
    distractors = distractors[:3]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    dataframe_text = (
        f"employee | {column}\n"
        f"---------|-------\n"
    )

    for i, value in enumerate(values):
        value_text = "NaN" if value is None else str(value)
        employee = chr(ord("A") + i)
        dataframe_text += f"{employee} | {value_text}\n"

    question = (
        f"Given the following DataFrame:\n\n"
        f"{dataframe_text}\n"
        f"Which Pandas statement correctly replaces missing "
        f"values in the {column} column with {method_text}?"
    )

    explanation = (
        f'fillna() replaces missing values. The expression '
        f'df["{column}"].fillna(...) uses the specified replacement '
        f'value for missing entries.'
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_pandas_duplicate_question(template):
    variables = template["variables"]

    operation = random.choice(variables["operations"])

    data = [
        {"employee": "A", "salary": 25000, "department": "HR"},
        {"employee": "B", "salary": 40000, "department": "IT"},
        {"employee": "B", "salary": 40000, "department": "IT"},
        {"employee": "C", "salary": 55000, "department": "Finance"}
    ]

    dataframe_text = (
        "employee | salary | department\n"
        "---------|--------|-----------\n"
    )

    for row in data:
        dataframe_text += (
            f"{row['employee']} | "
            f"{row['salary']} | "
            f"{row['department']}\n"
        )

    if operation == "drop_duplicates":
        correct_answer = "df.drop_duplicates()"

        question = (
            f"Given the following DataFrame:\n\n"
            f"{dataframe_text}\n"
            f"Which Pandas statement correctly removes "
            f"duplicate rows from the DataFrame?"
        )

        explanation = (
            "The drop_duplicates() method removes duplicate "
            "rows from a DataFrame. The duplicate record for "
            "employee B appears twice, so one duplicate row "
            "is removed."
        )

    else:
        correct_answer = "df.duplicated()"

        question = (
            f"Given the following DataFrame:\n\n"
            f"{dataframe_text}\n"
            f"Which Pandas statement identifies duplicate "
            f"rows in the DataFrame?"
        )

        explanation = (
            "The duplicated() method identifies duplicate rows "
            "and returns a Boolean Series indicating which rows "
            "are duplicates."
        )

    all_possible_answers = [
        "df.drop_duplicates()",
        "df.duplicated()",
        "df.dropna()",
        "df.drop_duplicates(axis=1)"
    ]

    distractors = [
        answer
        for answer in all_possible_answers
        if answer != correct_answer
    ]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_pandas_inconsistent_values_question(template):
    variables = template["variables"]

    column = random.choice(variables["columns"])
    method = random.choice(variables["standardization_methods"])

    data = [
        " Delhi ",
        "delhi",
        "DELHI ",
        " Mumbai",
        "mumbai "
    ]

    if method == "strip_lower":
        correct_answer = (
            f'df["{column}"] = '
            f'df["{column}"].str.strip().str.lower()'
        )

        method_text = (
            "removing extra spaces and converting values "
            "to lowercase"
        )

        explanation = (
            "The .str.strip() method removes leading and "
            "trailing spaces, while .str.lower() converts "
            "text to lowercase."
        )

    else:
        correct_answer = (
            f'df["{column}"] = '
            f'df["{column}"].str.strip().str.upper()'
        )

        method_text = (
            "removing extra spaces and converting values "
            "to uppercase"
        )

        explanation = (
            "The .str.strip() method removes leading and "
            "trailing spaces, while .str.upper() converts "
            "text to uppercase."
        )

    all_possible_answers = [
        f'df["{column}"] = df["{column}"].str.strip().str.lower()',
        f'df["{column}"] = df["{column}"].str.strip().str.upper()',
        f'df["{column}"] = df["{column}"].drop_duplicates()',
        f'df["{column}"] = df["{column}"].fillna("")'
    ]

    distractors = [
        answer
        for answer in all_possible_answers
        if answer != correct_answer
    ]

    random.shuffle(distractors)
    distractors = distractors[:3]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    dataframe_text = (
        f"{column}\n"
        f"{'-' * len(column)}\n"
    )

    for value in data:
        dataframe_text += f"{value}\n"

    question = (
        f"Given the following DataFrame, the {column} column "
        f"contains inconsistent capitalization and extra spaces:\n\n"
        f"{dataframe_text}\n"
        f"Which Pandas statement correctly standardizes the "
        f"{column} values by {method_text}?"
    )

    explanation += (
        f" Together, these methods standardize inconsistent "
        f"categorical values in the {column} column."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_chart_selection_question(template):
    variables = template["variables"]

    scenario = random.choice(variables["scenarios"])

    chart = scenario["correct_chart"]
    wrong_charts = scenario["wrong_charts"]

    correct_answer = chart

    distractors = random.sample(
        wrong_charts,
        min(3, len(wrong_charts))
    )

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = (
        f"{scenario['question']}"
    )

    explanation = (
        f"A {chart.lower()} is appropriate because "
        f"{scenario['explanation']}"
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_visualization_interpretation_question(template):
    variables = template["variables"]

    categories = variables["categories"]
    min_value, max_value = variables["value_range"]

    values = [
        random.randint(min_value, max_value)
        for _ in categories
    ]

    # Find the category with the highest value
    max_index = values.index(max(values))
    correct_answer = categories[max_index]

    # Create distractors from the other categories
    distractors = [
        category
        for category in categories
        if category != correct_answer
    ]

    distractors = random.sample(
        distractors,
        min(3, len(distractors))
    )

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    visualization_text = "Category | Value\n"
    visualization_text += "---------|------\n"

    for category, value in zip(categories, values):
        visualization_text += (
            f"{category} | {value}\n"
        )

    question = (
        f"The following table represents values shown in a "
        f"visualization:\n\n"
        f"{visualization_text}\n"
        f"Which category has the highest value?"
    )

    explanation = (
        f"{correct_answer} has the highest value of "
        f"{values[max_index]}. Therefore, it represents "
        f"the highest value in the visualization."
    )

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_business_visualization_question(template):
    variables = template["variables"]

    scenario = random.choice(variables["scenarios"])

    correct_answer = scenario["correct_chart"]

    distractors = scenario["wrong_charts"]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = scenario["question"]

    explanation = scenario["explanation"]

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_basic_data_insight_question(template):
    variables = template["variables"]

    scenario = random.choice(variables["scenarios"])

    correct_answer = scenario["correct_answer"]

    distractors = scenario["wrong_answers"]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = scenario["question"]
    explanation = scenario["explanation"]

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_comparative_analysis_question(template):
    variables = template["variables"]

    scenario = random.choice(variables["scenarios"])

    correct_answer = scenario["correct_answer"]
    distractors = scenario["wrong_answers"]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = scenario["question"]
    explanation = scenario["explanation"]

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_business_decision_question(template):
    variables = template["variables"]

    scenario = random.choice(variables["scenarios"])

    correct_answer = scenario["correct_answer"]
    distractors = scenario["wrong_answers"]

    options = [correct_answer] + distractors
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_label = chr(ord("A") + correct_index)

    question = scenario["question"]
    explanation = scenario["explanation"]

    return {
        "template_id": template["template_id"],
        "skill_id": template["skill_id"],
        "topic": template["topic"],
        "difficulty": template["difficulty"],
        "question_type": template["question_type"],
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "correct_label": correct_label,
        "explanation": explanation,
        "marks": 1
    }

def generate_question_from_template(template):

    strategy = template["generation_strategy"]

    if strategy == "QUERY":
        return generate_sql_aggregation_question(template)
    elif strategy=="SQL_FILTER":
        return generate_sql_filter_question(template)
    elif strategy=="SQL_SUBQUERY":
        return generate_sql_subquery_question(template)

    elif strategy == "CODE":
        if template["topic"]=="Pandas DataFrame Column Selection":
            return generate_pandas_column_selection_question(template)
        elif template["topic"]=="Pandas Multiple-Condition Filtering":
            return generate_pandas_multi_filter_question(template)
        elif template["topic"]=="Missing Value Handling":
            return generate_pandas_missing_value_question(template)
        elif template["topic"]=="Duplicate Record Handling":
            return generate_pandas_duplicate_question(template)
        elif template["topic"]=="Inconsistent Value Handling":
            return generate_pandas_inconsistent_values_question(template)
        else:
            return generate_pandas_filter_question(template)

    elif strategy == "NUMERICAL":
        return generate_mean_question(template)

    elif strategy == "NUMERICAL_MEDIAN":
        return generate_median_question(template)
    elif strategy=="NUMERICAL_MODE":
        return generate_mode_question(template)
    elif strategy=="STATISTICAL_INTERPRETATION":
        return generate_std_interpretation_question(template)

    elif strategy == "EXCEL_FORMULA":
        return generate_excel_formula_question(template)
    elif strategy=="EXCEL_IF":
        return generate_excel_if_question(template)
    elif strategy=="EXCEL_LOOKUP":
        return generate_excel_lookup_question(template)

    elif strategy=="CHART_SELECTION":
        return generate_chart_selection_question(template)
    elif strategy=="VISUALIZATION_INTERPRETATION":
        return generate_visualization_interpretation_question(template)
    elif strategy=="BUSINESS_VISUALIZATION":
        return generate_business_visualization_question(template)

    elif strategy=="BASIC_DATA_INSIGHT":
        return generate_basic_data_insight_question(template)
    elif strategy=="COMPARATIVE_ANALYSIS":
        return generate_comparative_analysis_question(template)
    elif strategy=="BUSINESS_DECISION":
        return generate_business_decision_question(template)

    else:
        raise ValueError(
            f"Unsupported generation strategy: {strategy}"
        )

def get_random_template(skill_id,difficulty=None,template_id=None):
    query="""
            SELECT
                template_id,
                skill_id,
                topic,
                difficulty,
                question_type,
                generation_strategy,
                template_text,
                variables,
                answer_rule,
                explanation_rule
            FROM question_templates
            WHERE skill_id = :skill_id
              AND is_active = TRUE
        """
    params={"skill_id": skill_id}
    if template_id is not None:
        query +=" AND template_id = :template_id"
        params["template_id"]=template_id
    if difficulty is not None:
        query += " AND difficulty = :difficulty"
        params["difficulty"] = difficulty

    result = db.session.execute(
        db.text(query),
        params
    )

    templates = result.mappings().all()

    if not templates:
        raise ValueError(
            f"No active templates found for "
            f"skill_id= {skill_id},difficulty={difficulty}"
        )

    template = dict(random.choice(templates))

    if isinstance(template["variables"], str):
        template["variables"] = json.loads(template["variables"])

    return template

def generate_questions(skill_id,difficulty, count):
    questions = []

    for _ in range(count):
        template = get_random_template(skill_id,difficulty)

        generated = generate_question_from_template(template)

        questions.append(generated)

    return questions

def generate_and_save_questions(skill_id, difficulty,count):
    inserted = 0
    skipped = 0

    for _ in range(count):

        template = get_random_template(skill_id,difficulty)

        generated = generate_question_from_template(template)

        # Check for duplicate
        existing = db.session.execute(
            db.text("""
                SELECT question_id
                FROM questions
                WHERE template_id = :template_id
                  AND question_text = :question_text
                LIMIT 1
            """),
            {
                "template_id": generated["template_id"],
                "question_text": generated["question"]
            }
        ).first()

        if existing:
            skipped += 1
            continue

        # Save question
        result = db.session.execute(
            db.text("""
                INSERT INTO questions (
                    skill_id,
                    topic,
                    difficulty,
                    question_type,
                    question_text,
                    correct_answer,
                    explanation,
                    marks,
                    template_id
                )
                VALUES (
                    :skill_id,
                    :topic,
                    :difficulty,
                    :question_type,
                    :question_text,
                    :correct_answer,
                    :explanation,
                    :marks,
                    :template_id
                )
            """),
            {
                "skill_id": generated["skill_id"],
                "topic": generated["topic"],
                "difficulty": generated["difficulty"],
                "question_type": generated["question_type"],
                "question_text": generated["question"],
                "correct_answer": generated["correct_answer"],
                "explanation": generated["explanation"],
                "marks": generated["marks"],
                "template_id": generated["template_id"]
            }
        )

        question_id = result.lastrowid

        # Save options
        for i, option in enumerate(generated["options"]):
            label = chr(ord("A") + i)

            db.session.execute(
                db.text("""
                    INSERT INTO question_options (
                        question_id,
                        option_label,
                        option_text
                    )
                    VALUES (
                        :question_id,
                        :option_label,
                        :option_text
                    )
                """),
                {
                    "question_id": question_id,
                    "option_label": label,
                    "option_text": option
                }
            )

        inserted += 1

    db.session.commit()

    print("\n========== GENERATION SUMMARY ==========")
    print(f"Requested questions : {count}")
    print(f"Difficulty          : {difficulty}")
    print(f"Questions inserted  : {inserted}")
    print(f"Duplicates skipped  : {skipped}")

    return inserted, skipped

def validate_blueprint_templates(blueprint_rows):
    """
    Check whether at least one active question template exists
    for every skill and difficulty required by a blueprint.
    """

    missing = []

    for row in blueprint_rows:
        skill_id = row["skill_id"]

        required = {
            "Easy": row["easy_count"] or 0,
            "Medium": row["medium_count"] or 0,
            "Hard": row["hard_count"] or 0
        }

        for difficulty, required_count in required.items():

            if required_count == 0:
                continue

            result = db.session.execute(
                db.text("""
                    SELECT COUNT(*) AS template_count
                    FROM question_templates
                    WHERE skill_id = :skill_id
                      AND difficulty = :difficulty
                      AND is_active = TRUE
                """),
                {
                    "skill_id": skill_id,
                    "difficulty": difficulty
                }
            ).mappings().first()

            available = result["template_count"]

            if available == 0:
                missing.append({
                    "skill_id": skill_id,
                    "difficulty": difficulty,
                    "required_questions": required_count,
                    "available_templates": available
                })

    return missing

def generate_assessment(user_id, career_id):
    """
    Generate an assessment from the career's blueprint.

    The assessment is created only if all required
    question templates are available.
    """

    # -----------------------------------------
    # 1. Get blueprint
    # -----------------------------------------

    result = db.session.execute(
        db.text("""
            SELECT
                blueprint_id,
                career_id,
                skill_id,
                question_count,
                easy_count,
                medium_count,
                hard_count
            FROM assessment_blueprints
            WHERE career_id = :career_id
            ORDER BY skill_id
        """),
        {
            "career_id": career_id
        }
    )

    blueprint_rows = result.mappings().all()

    if not blueprint_rows:
        raise ValueError(
            f"No assessment blueprint found for career_id={career_id}"
        )

    # -----------------------------------------
    # 2. Validate templates
    # -----------------------------------------

    missing = validate_blueprint_templates(
        blueprint_rows
    )

    if missing:

        print("\n========== ASSESSMENT GENERATION BLOCKED ==========")
        print("Required question templates are missing.\n")

        for item in missing:
            print(
                f"Skill {item['skill_id']} | "
                f"{item['difficulty']} | "
                f"Required questions: "
                f"{item['required_questions']} | "
                f"Available templates: "
                f"{item['available_templates']}"
            )

        print("\nAssessment was NOT created.")

        return None

    # -----------------------------------------
    # 3. Create assessment
    # -----------------------------------------

    result = db.session.execute(
        db.text("""
            INSERT INTO assessments (
                user_id,
                career_id,
                status,
                total_score
            )
            VALUES (
                :user_id,
                :career_id,
                'In Progress',
                0.00
            )
        """),
        {
            "user_id": user_id,
            "career_id": career_id
        }
    )

    assessment_id = result.lastrowid

    # -----------------------------------------
    # 4. Generate questions
    # -----------------------------------------

    question_order = 1

    for row in blueprint_rows:

        skill_id = row["skill_id"]

        difficulty_counts = {
            "Easy": row["easy_count"] or 0,
            "Medium": row["medium_count"] or 0,
            "Hard": row["hard_count"] or 0
        }

        for difficulty, count in difficulty_counts.items():

            for _ in range(count):

                template = get_random_template(
                    skill_id,
                    difficulty
                )

                generated = generate_question_from_template(
                    template
                )

                # -----------------------------------------
                # 5. Save generated question
                # -----------------------------------------

                result = db.session.execute(
                    db.text("""
                        INSERT INTO questions (
                            skill_id,
                            topic,
                            difficulty,
                            question_type,
                            question_text,
                            correct_answer,
                            explanation,
                            marks,
                            template_id
                        )
                        VALUES (
                            :skill_id,
                            :topic,
                            :difficulty,
                            :question_type,
                            :question_text,
                            :correct_answer,
                            :explanation,
                            :marks,
                            :template_id
                        )
                    """),
                    {
                        "skill_id": generated["skill_id"],
                        "topic": generated["topic"],
                        "difficulty": generated["difficulty"],
                        "question_type": generated["question_type"],
                        "question_text": generated["question"],
                        "correct_answer": generated["correct_answer"],
                        "explanation": generated["explanation"],
                        "marks": generated["marks"],
                        "template_id": generated["template_id"]
                    }
                )

                question_id = result.lastrowid

                # -----------------------------------------
                # 6. Save options
                # -----------------------------------------

                for i, option in enumerate(
                    generated["options"]
                ):

                    label = chr(ord("A") + i)

                    db.session.execute(
                        db.text("""
                            INSERT INTO question_options (
                                question_id,
                                option_label,
                                option_text
                            )
                            VALUES (
                                :question_id,
                                :option_label,
                                :option_text
                            )
                        """),
                        {
                            "question_id": question_id,
                            "option_label": label,
                            "option_text": option
                        }
                    )

                # -----------------------------------------
                # 7. Attach question to assessment
                # -----------------------------------------

                db.session.execute(
                    db.text("""
                        INSERT INTO assessment_questions (
                            assessment_id,
                            question_id,
                            question_order
                        )
                        VALUES (
                            :assessment_id,
                            :question_id,
                            :question_order
                        )
                    """),
                    {
                        "assessment_id": assessment_id,
                        "question_id": question_id,
                        "question_order": question_order
                    }
                )

                question_order += 1

    # -----------------------------------------
    # 8. Commit everything
    # -----------------------------------------

    db.session.commit()

    print("\n========== ASSESSMENT GENERATED ==========")
    print(f"Assessment ID : {assessment_id}")
    print(f"Questions     : {question_order - 1}")
    print("Status        : In Progress")

    return assessment_id

def create_assessment(user_id, career_id):
    """
    Create a new assessment record and return its assessment_id.
    """

    result = db.session.execute(
        db.text("""
            INSERT INTO assessments (
                user_id,
                career_id,
                status,
                total_score
            )
            VALUES (
                :user_id,
                :career_id,
                'In Progress',
                0.00
            )
        """),
        {
            "user_id": user_id,
            "career_id": career_id
        }
    )

    assessment_id = result.lastrowid

    db.session.commit()

    print("\nAssessment created successfully!")
    print(f"Assessment ID: {assessment_id}")
    print(f"User ID: {user_id}")
    print(f"Career ID: {career_id}")

    return assessment_id

# if __name__ == "__main__":
#     with app.app_context():

#         generate_and_save_questions(
#             skill_id=3,
#             difficulty="Hard",
#             count=3
#         )
# if __name__ == "__main__":
#     with app.app_context():
#         for difficulty in ["Easy", "Medium", "Hard"]:
#             print(
#                 f"\n========== DATA CLEANING | "
#                 f"{difficulty.upper()} =========="
#             )

#             generate_and_save_questions(
#                 skill_id=5,
#                 difficulty=difficulty,
#                 count=3
#             )
if __name__ == "__main__":
    with app.app_context():
        assessment_id = generate_assessment(
            user_id=1,
            career_id=1
        )

        print("\nAssessment ID:", assessment_id)
