QUESTIONS = [

    # ============================================================
    # EXCEL & SPREADSHEET ANALYSIS
    # ============================================================

    {
        "skill": "Excel & Spreadsheet Analysis",
        "topic": "Basic formulas",
        "difficulty": "Easy",
        "question_type": "MCQ",
        "question_text": (
            "A sales dataset contains the sales amounts for 10 products "
            "in cells B2:B11. Which Excel formula correctly calculates "
            "the total sales?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The SUM() function adds all numeric values in the specified range."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "=TOTAL(B2:B11)"},
            {"label": "B", "text": "=SUM(B2:B11)"},
            {"label": "C", "text": "=ADD(B2:B11)"},
            {"label": "D", "text": "=COUNT(B2:B11)"}
        ]
    },

    {
        "skill": "Excel & Spreadsheet Analysis",
        "topic": "Lookup functions",
        "difficulty": "Medium",
        "question_type": "Scenario",
        "question_text": (
            "You have an employee table with Employee ID, Name and "
            "Department in columns A, B and C respectively. Cell F2 "
            "contains Employee ID E103. Which VLOOKUP formula retrieves "
            "the corresponding Department?"
        ),
        "correct_answer": "A",
        "explanation": (
            "E103 is searched in the first column of A2:C5, and Department "
            "is the third column. FALSE specifies an exact match."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "=VLOOKUP(F2,A2:C5,3,FALSE)"},
            {"label": "B", "text": "=VLOOKUP(F2,A2:C5,2,FALSE)"},
            {"label": "C", "text": "=VLOOKUP(F2,A2:B5,3,FALSE)"},
            {"label": "D", "text": "=VLOOKUP(F2,B2:C5,3,FALSE)"}
        ]
    },

    {
        "skill": "Excel & Spreadsheet Analysis",
        "topic": "PivotTables",
        "difficulty": "Hard",
        "question_type": "Scenario",
        "question_text": (
            "A company has a sales dataset containing Date, Region, "
            "Product and Sales. The manager wants the average sales value "
            "per transaction for each region. Which Excel approach is most appropriate?"
        ),
        "correct_answer": "A",
        "explanation": (
            "A PivotTable can group transactions by Region and calculate "
            "the average Sales value for each group."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": (
                    "Create a PivotTable, place Region in Rows and Sales "
                    "in Values, then change Sales from Sum to Average."
                )
            },
            {
                "label": "B",
                "text": (
                    "Create a PivotTable, place Sales in Rows and Region "
                    "in Values, then use Count."
                )
            },
            {
                "label": "C",
                "text": (
                    "Sort Sales from largest to smallest and select the "
                    "first transaction from each region."
                )
            },
            {
                "label": "D",
                "text": (
                    "Use COUNTIF() to count the number of transactions "
                    "in each region."
                )
            }
        ]
    },
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "COUNTIF",
    "difficulty": "Easy",
    "question_type": "Code",
    "question_text": (
        "An Excel sheet contains employee departments in cells B2:B101. "
        "Which formula counts how many employees belong to the Sales department?"
    ),
    "correct_answer": "A",
    "explanation": (
        "COUNTIF counts cells that satisfy a specified condition. "
        "Here, it counts cells in B2:B101 whose value is Sales."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": '=COUNTIF(B2:B101,"Sales")'},
        {"label": "B", "text": '=COUNT(B2:B101,"Sales")'},
        {"label": "C", "text": '=SUMIF(B2:B101,"Sales")'},
        {"label": "D", "text": '=COUNTA(B2:B101,"Sales")'}
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "Sorting and filtering",
    "difficulty": "Easy",
    "question_type": "Scenario",
    "question_text": (
        "An analyst has a table containing 5,000 sales transactions and "
        "wants to temporarily view only transactions from the North region "
        "without deleting the other rows. What should they use?"
    ),
    "correct_answer": "B",
    "explanation": (
        "Excel's Filter feature temporarily hides rows that don't meet "
        "the selected condition without deleting the underlying data."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Delete all rows except North"},
        {"label": "B", "text": "Apply a filter to the Region column"},
        {"label": "C", "text": "Sort the entire workbook alphabetically"},
        {"label": "D", "text": "Use Find and Replace to remove other regions"}
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "IF function",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A student's score is stored in cell C2. The analyst wants a new "
        "column to display 'Pass' when the score is at least 40 and "
        "'Fail' otherwise. Which formula is correct?"
    ),
    "correct_answer": "C",
    "explanation": (
        "The IF function checks whether C2 is greater than or equal to 40. "
        "If true, it returns Pass; otherwise it returns Fail."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": '=IF(C2>40,"Pass","Fail")'},
        {"label": "B", "text": '=IF(C2<40,"Pass","Fail")'},
        {"label": "C", "text": '=IF(C2>=40,"Pass","Fail")'},
        {"label": "D", "text": '=IF(C2=40,"Pass","Fail")'}
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "XLOOKUP",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A product table contains Product ID in A2:A100 and Product Name "
        "in B2:B100. Cell E2 contains a Product ID. Which formula retrieves "
        "the corresponding Product Name?"
    ),
    "correct_answer": "A",
    "explanation": (
        "XLOOKUP searches for the value in E2 within A2:A100 and returns "
        "the corresponding value from B2:B100."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "=XLOOKUP(E2,A2:A100,B2:B100)"},
        {"label": "B", "text": "=XLOOKUP(E2,B2:B100,A2:A100)"},
        {"label": "C", "text": "=XLOOKUP(A2:A100,E2,B2:B100)"},
        {"label": "D", "text": "=XLOOKUP(B2:B100,A2:A100,E2)"}
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "Conditional formatting",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "An analyst wants all sales values below ₹10,000 to be automatically "
        "highlighted whenever the data changes. Which Excel feature is most "
        "appropriate?"
    ),
    "correct_answer": "B",
    "explanation": (
        "Conditional Formatting can automatically apply formatting when "
        "cells satisfy a specified condition."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Data Validation"},
        {"label": "B", "text": "Conditional Formatting"},
        {"label": "C", "text": "Text to Columns"},
        {"label": "D", "text": "Flash Fill"}
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "Multiple-condition analysis",
    "difficulty": "Hard",
    "question_type": "Code",
    "question_text": (
        "An analyst wants to calculate the total sales for the North region "
        "during January. Region is stored in A2:A100, Month in B2:B100, "
        "and Sales in C2:C100. Which formula is most appropriate?"
    ),
    "correct_answer": "D",
    "explanation": (
        "SUMIFS can sum values using multiple conditions. Here, it sums "
        "Sales where Region is North and Month is January."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": '=SUMIF(A2:A100,"North",C2:C100)'
        },
        {
            "label": "B",
            "text": '=SUM(C2:C100,"North","January")'
        },
        {
            "label": "C",
            "text": '=COUNTIFS(A2:A100,"North",B2:B100,"January")'
        },
        {
            "label": "D",
            "text": '=SUMIFS(C2:C100,A2:A100,"North",B2:B100,"January")'
        }
    ]
},
{
    "skill": "Excel & Spreadsheet Analysis",
    "topic": "PivotTable analysis",
    "difficulty": "Hard",
    "question_type": "Data Interpretation",
    "question_text": (
        "A PivotTable shows the following average order values: "
        "North = ₹800, South = ₹600, East = ₹900 and West = ₹700. "
        "Which region has the highest average order value, and what "
        "does this metric represent?"
    ),
    "correct_answer": "C",
    "explanation": (
        "East has the highest average order value at ₹900. "
        "Average order value represents the average amount spent per order "
        "within that region."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "North; each North customer spent ₹800"
        },
        {
            "label": "B",
            "text": "South; each South customer spent ₹600"
        },
        {
            "label": "C",
            "text": "East; the average amount per order was ₹900"
        },
        {
            "label": "D",
            "text": "West; the total sales were ₹700"
        }
    ]
},

    # ============================================================
    # SQL & DATABASE ANALYSIS
    # ============================================================

    {
        "skill": "SQL & Database Analysis",
        "topic": "Filtering",
        "difficulty": "Easy",
        "question_type": "Code",
        "question_text": (
            "Consider an employees table containing id, name and salary. "
            "Which SQL query returns employees whose salary is greater than ₹50,000?"
        ),
        "correct_answer": "A",
        "explanation": (
            "WHERE salary > 50000 filters rows whose salary is strictly "
            "greater than ₹50,000."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "SELECT * FROM employees WHERE salary > 50000;"
            },
            {
                "label": "B",
                "text": "SELECT * FROM employees WHERE salary >= 50000;"
            },
            {
                "label": "C",
                "text": "SELECT * FROM employees HAVING salary > 50000;"
            },
            {
                "label": "D",
                "text": "SELECT * FROM employees WHERE salary < 50000;"
            }
        ]
    },

    {
        "skill": "SQL & Database Analysis",
        "topic": "GROUP BY and aggregation",
        "difficulty": "Medium",
        "question_type": "Code",
        "question_text": (
            "A sales table contains region and amount columns. "
            "Which query calculates the total sales for each region?"
        ),
        "correct_answer": "B",
        "explanation": (
            "GROUP BY region creates one group for each region, while "
            "SUM(amount) calculates the total within each group."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "SELECT region, SUM(amount) FROM sales;"
            },
            {
                "label": "B",
                "text": (
                    "SELECT region, SUM(amount) FROM sales "
                    "GROUP BY region;"
                )
            },
            {
                "label": "C",
                "text": (
                    "SELECT SUM(region), amount FROM sales "
                    "GROUP BY amount;"
                )
            },
            {
                "label": "D",
                "text": (
                    "SELECT region, COUNT(amount) FROM sales "
                    "GROUP BY amount;"
                )
            }
        ]
    },

    {
        "skill": "SQL & Database Analysis",
        "topic": "JOIN and aggregation",
        "difficulty": "Hard",
        "question_type": "Scenario",
        "question_text": (
            "A customers table contains customer_id and name. An orders "
            "table contains order_id, customer_id and amount. An analyst "
            "wants to find customers whose total order amount exceeds "
            "₹1,000. Which query correctly produces the result?"
        ),
        "correct_answer": "A",
        "explanation": (
            "The query joins customers and orders, groups orders by customer, "
            "calculates the total with SUM(), and uses HAVING to filter "
            "the grouped results."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": (
                    "SELECT c.name, SUM(o.amount) "
                    "FROM customers c "
                    "JOIN orders o ON c.customer_id = o.customer_id "
                    "GROUP BY c.name "
                    "HAVING SUM(o.amount) > 1000;"
                )
            },
            {
                "label": "B",
                "text": (
                    "SELECT c.name, SUM(o.amount) "
                    "FROM customers c "
                    "JOIN orders o ON c.customer_id = o.customer_id "
                    "WHERE SUM(o.amount) > 1000 "
                    "GROUP BY c.name;"
                )
            },
            {
                "label": "C",
                "text": (
                    "SELECT c.name, o.amount "
                    "FROM customers c "
                    "JOIN orders o ON c.customer_id = o.customer_id "
                    "WHERE o.amount > 1000;"
                )
            },
            {
                "label": "D",
                "text": (
                    "SELECT c.name, SUM(o.amount) "
                    "FROM customers c "
                    "JOIN orders o ON c.customer_id = o.customer_id "
                    "GROUP BY o.amount "
                    "HAVING SUM(o.amount) > 1000;"
                )
            }
        ]
    },

    {
        "skill": "SQL & Database Analysis",
        "topic": "HAVING versus WHERE",
        "difficulty": "Medium",
        "question_type": "Code",
        "question_text": (
            "A sales table contains region and amount columns. "
            "An analyst wants to find regions whose total sales exceed "
            "₹2,000. Which query is correct?"
        ),
        "correct_answer": "B",
        "explanation": (
            "HAVING filters grouped results based on aggregate functions "
            "such as SUM(). WHERE filters individual rows before grouping."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": (
                    "SELECT region, SUM(amount) FROM sales "
                    "WHERE SUM(amount) > 2000 "
                    "GROUP BY region;"
                )
            },
            {
                "label": "B",
                "text": (
                    "SELECT region, SUM(amount) FROM sales "
                    "GROUP BY region "
                    "HAVING SUM(amount) > 2000;"
                )
            },
            {
                "label": "C",
                "text": (
                    "SELECT region, amount FROM sales "
                    "WHERE amount > 2000;"
                )
            },
            {
                "label": "D",
                "text": (
                    "SELECT region, SUM(amount) FROM sales "
                    "WHERE amount > 2000 "
                    "GROUP BY region;"
                )
            }
        ]
    },
    {
    "skill": "SQL & Database Analysis",
    "topic": "ORDER BY",
    "difficulty": "Easy",
    "question_type": "Code",
    "question_text": (
        "An employees table contains employee_id, name and salary. "
        "Which query displays all employees from the highest salary "
        "to the lowest salary?"
    ),
    "correct_answer": "B",
    "explanation": (
        "ORDER BY salary DESC sorts the salary values from the largest "
        "to the smallest."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "SELECT * FROM employees ORDER BY salary ASC;"
        },
        {
            "label": "B",
            "text": "SELECT * FROM employees ORDER BY salary DESC;"
        },
        {
            "label": "C",
            "text": "SELECT * FROM employees GROUP BY salary DESC;"
        },
        {
            "label": "D",
            "text": "SELECT * FROM employees SORT BY salary DESC;"
        }
    ]
},

{
    "skill": "SQL & Database Analysis",
    "topic": "NULL values",
    "difficulty": "Easy",
    "question_type": "Code",
    "question_text": (
        "An employees table contains a manager_id column. Some employees "
        "do not have a manager, so manager_id is NULL. Which query correctly "
        "finds employees who do not have a manager?"
    ),
    "correct_answer": "C",
    "explanation": (
        "SQL uses IS NULL to test for NULL values. Using "
        "= NULL does not correctly identify NULL values."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "SELECT * FROM employees WHERE manager_id = NULL;"
        },
        {
            "label": "B",
            "text": "SELECT * FROM employees WHERE manager_id == NULL;"
        },
        {
            "label": "C",
            "text": "SELECT * FROM employees WHERE manager_id IS NULL;"
        },
        {
            "label": "D",
            "text": "SELECT * FROM employees WHERE manager_id LIKE NULL;"
        }
    ]
},

{
    "skill": "SQL & Database Analysis",
    "topic": "CASE WHEN",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "An analyst wants to classify employees based on salary: "
        "salary >= 80000 as 'High', salary >= 50000 as 'Medium', "
        "and anything below 50000 as 'Low'. Which SQL expression "
        "correctly performs this classification?"
    ),
    "correct_answer": "A",
    "explanation": (
        "CASE WHEN evaluates conditions in order. The first matching "
        "condition determines the returned value."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": (
                "CASE "
                "WHEN salary >= 80000 THEN 'High' "
                "WHEN salary >= 50000 THEN 'Medium' "
                "ELSE 'Low' END"
            )
        },
        {
            "label": "B",
            "text": (
                "CASE salary "
                "WHEN >= 80000 THEN 'High' "
                "WHEN >= 50000 THEN 'Medium' "
                "ELSE 'Low' END"
            )
        },
        {
            "label": "C",
            "text": (
                "IF salary >= 80000 'High' "
                "ELSE IF salary >= 50000 'Medium' "
                "ELSE 'Low'"
            )
        },
        {
            "label": "D",
            "text": (
                "CASE "
                "WHEN salary < 50000 THEN 'High' "
                "WHEN salary < 80000 THEN 'Medium' "
                "ELSE 'Low' END"
            )
        }
    ]
},

{
    "skill": "SQL & Database Analysis",
    "topic": "JOIN",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A customers table contains customer_id and customer_name. "
        "An orders table contains order_id, customer_id and amount. "
        "Which JOIN is most appropriate if the analyst wants only "
        "customers who have placed at least one order?"
    ),
    "correct_answer": "B",
    "explanation": (
        "An INNER JOIN returns only rows where the join condition "
        "matches in both tables."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": (
                "SELECT * FROM customers c "
                "LEFT JOIN orders o "
                "ON c.customer_id = o.customer_id;"
            )
        },
        {
            "label": "B",
            "text": (
                "SELECT * FROM customers c "
                "INNER JOIN orders o "
                "ON c.customer_id = o.customer_id;"
            )
        },
        {
            "label": "C",
            "text": (
                "SELECT * FROM customers c "
                "RIGHT JOIN orders o "
                "ON c.customer_id = o.customer_id;"
            )
        },
        {
            "label": "D",
            "text": (
                "SELECT * FROM customers c "
                "CROSS JOIN orders o;"
            )
        }
    ]
},

{
    "skill": "SQL & Database Analysis",
    "topic": "Subqueries",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "An employees table contains salary. Which query finds employees "
        "whose salary is greater than the average salary of all employees?"
    ),
    "correct_answer": "A",
    "explanation": (
        "The subquery calculates the average salary first. The outer query "
        "then returns employees whose salary is greater than that value."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": (
                "SELECT * FROM employees "
                "WHERE salary > (SELECT AVG(salary) FROM employees);"
            )
        },
        {
            "label": "B",
            "text": (
                "SELECT * FROM employees "
                "WHERE salary > AVG(salary);"
            )
        },
        {
            "label": "C",
            "text": (
                "SELECT * FROM employees "
                "HAVING salary > AVG(salary);"
            )
        },
        {
            "label": "D",
            "text": (
                "SELECT * FROM employees "
                "WHERE AVG(salary) > salary;"
            )
        }
    ]
},

{
    "skill": "SQL & Database Analysis",
    "topic": "Window functions",
    "difficulty": "Hard",
    "question_type": "Code",
    "question_text": (
        "An analyst wants to rank employees by salary within each "
        "department, with the highest salary receiving rank 1. "
        "Which expression correctly performs this calculation?"
    ),
    "correct_answer": "C",
    "explanation": (
        "RANK() OVER partitions the data by department and orders salaries "
        "from highest to lowest within each department."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": (
                "RANK(salary) GROUP BY department "
                "ORDER BY salary DESC"
            )
        },
        {
            "label": "B",
            "text": (
                "RANK() OVER (ORDER BY department, salary)"
            )
        },
        {
            "label": "C",
            "text": (
                "RANK() OVER "
                "(PARTITION BY department ORDER BY salary DESC)"
            )
        },
        {
            "label": "D",
            "text": (
                "RANK() OVER "
                "(PARTITION BY salary ORDER BY department DESC)"
            )
        }
    ]
},



    # ============================================================
    # PYTHON FOR DATA ANALYSIS
    # ============================================================

    {
        "skill": "Python for Data Analysis",
        "topic": "Python fundamentals",
        "difficulty": "Easy",
        "question_type": "Code",
        "question_text": (
            "Consider the following Python code: "
            "sales = [1200, 1500, 900, 1800, 1100]. "
            "total = sum(sales). What will total contain?"
        ),
        "correct_answer": "C",
        "explanation": (
            "1200 + 1500 + 900 + 1800 + 1100 = 6500."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "5500"},
            {"label": "B", "text": "6000"},
            {"label": "C", "text": "6500"},
            {"label": "D", "text": "7000"}
        ]
    },

    {
        "skill": "Python for Data Analysis",
        "topic": "Pandas filtering",
        "difficulty": "Medium",
        "question_type": "Code",
        "question_text": (
            "A Pandas DataFrame contains students Aman, Riya, Karan and "
            "Simran with scores 65, 82, 74 and 91 respectively. "
            "If result = df[df['Score'] >= 80], which students will be present?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The condition keeps scores greater than or equal to 80. "
            "Riya scored 82 and Simran scored 91."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Aman and Karan"},
            {"label": "B", "text": "Riya and Simran"},
            {"label": "C", "text": "Aman and Simran"},
            {"label": "D", "text": "Karan and Riya"}
        ]
    },

    {
        "skill": "Python for Data Analysis",
        "topic": "Pandas grouping and aggregation",
        "difficulty": "Hard",
        "question_type": "Code",
        "question_text": (
            "A Pandas DataFrame contains Department values Sales, Sales, "
            "HR, HR and IT, with corresponding salaries 40000, 60000, "
            "45000, 55000 and 70000. What is the average salary for Sales "
            "when using df.groupby('Department')['Salary'].mean()?"
        ),
        "correct_answer": "B",
        "explanation": (
            "Sales has salaries of ₹40,000 and ₹60,000. "
            "Their average is ₹50,000."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "₹40,000"},
            {"label": "B", "text": "₹50,000"},
            {"label": "C", "text": "₹55,000"},
            {"label": "D", "text": "₹60,000"}
        ]
    },
    {
    "skill": "Python for Data Analysis",
    "topic": "Python lists",
    "difficulty": "Easy",
    "question_type": "Code",
    "question_text": (
        "Consider the following Python code:\n"
        "sales = [100, 200, 300, 400]\n"
        "sales.append(500)\n"
        "What will len(sales) return?"
    ),
    "correct_answer": "C",
    "explanation": (
        "append() adds one new element to the end of the list. "
        "The original list has 4 elements, so it now contains 5."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "3"},
        {"label": "B", "text": "4"},
        {"label": "C", "text": "5"},
        {"label": "D", "text": "6"}
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Pandas DataFrame",
    "difficulty": "Easy",
    "question_type": "Code",
    "question_text": (
        "A Pandas DataFrame named df contains thousands of rows. "
        "Which command displays the first five rows by default?"
    ),
    "correct_answer": "A",
    "explanation": (
        "The head() method returns the first five rows of a DataFrame "
        "when no number is specified."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "df.head()"},
        {"label": "B", "text": "df.first()"},
        {"label": "C", "text": "df.top()"},
        {"label": "D", "text": "df.start()"}
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Missing values with Pandas",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A DataFrame df contains missing values in the Salary column. "
        "Which Pandas expression replaces missing Salary values with "
        "the median salary of that column?"
    ),
    "correct_answer": "B",
    "explanation": (
        "median() calculates the column median, and fillna() replaces "
        "missing values with the supplied value."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "df['Salary'].fillna(df['Salary'].mean())"
        },
        {
            "label": "B",
            "text": "df['Salary'].fillna(df['Salary'].median())"
        },
        {
            "label": "C",
            "text": "df['Salary'].replace(df['Salary'].median())"
        },
        {
            "label": "D",
            "text": "df['Salary'].dropna(df['Salary'].median())"
        }
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Pandas filtering",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A DataFrame contains Department and Salary columns. "
        "Which expression selects employees who belong to the IT "
        "department AND have a salary greater than ₹60,000?"
    ),
    "correct_answer": "C",
    "explanation": (
        "Pandas uses & for an element-wise AND between conditions. "
        "Each condition must be placed inside parentheses."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "df[df['Department'] == 'IT' and df['Salary'] > 60000]"
        },
        {
            "label": "B",
            "text": "df[df['Department'] = 'IT' & df['Salary'] > 60000]"
        },
        {
            "label": "C",
            "text": (
                "df[(df['Department'] == 'IT') & "
                "(df['Salary'] > 60000)]"
            )
        },
        {
            "label": "D",
            "text": (
                "df[(df['Department'] == 'IT') | "
                "(df['Salary'] > 60000)]"
            )
        }
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Pandas groupby",
    "difficulty": "Medium",
    "question_type": "Code",
    "question_text": (
        "A DataFrame contains Department and Salary columns. "
        "Which expression calculates the average salary for each department?"
    ),
    "correct_answer": "A",
    "explanation": (
        "groupby('Department') creates groups for each department, "
        "and ['Salary'].mean() calculates the average salary within each group."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "df.groupby('Department')['Salary'].mean()"
        },
        {
            "label": "B",
            "text": "df.groupby('Salary')['Department'].mean()"
        },
        {
            "label": "C",
            "text": "df['Department'].mean('Salary')"
        },
        {
            "label": "D",
            "text": "df.groupby('Department')['Salary'].sum('mean')"
        }
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Pandas merge",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "You have two DataFrames: customers contains customer_id and "
        "customer_name, while orders contains customer_id and order_amount. "
        "You want to combine matching customer information with their orders "
        "using customer_id. Which Pandas operation is most appropriate?"
    ),
    "correct_answer": "B",
    "explanation": (
        "pd.merge() combines DataFrames using one or more common columns. "
        "Here, customer_id is the key shared by both DataFrames."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "pd.concat([customers, orders])"
        },
        {
            "label": "B",
            "text": (
                "pd.merge(customers, orders, on='customer_id')"
            )
        },
        {
            "label": "C",
            "text": "customers.append(orders, on='customer_id')"
        },
        {
            "label": "D",
            "text": "pd.group(customers, orders, by='customer_id')"
        }
    ]
},
{
    "skill": "Python for Data Analysis",
    "topic": "Pandas sorting",
    "difficulty": "Hard",
    "question_type": "Code",
    "question_text": (
        "A DataFrame df contains Product and Sales columns. "
        "An analyst wants to find the three products with the highest "
        "sales. Which approach is correct?"
    ),
    "correct_answer": "D",
    "explanation": (
        "Sorting Sales in descending order places the highest values first, "
        "and head(3) selects the first three rows."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "df.sort_values('Sales').head(3)"
        },
        {
            "label": "B",
            "text": "df.sort_values('Sales', ascending=True).tail(3)"
        },
        {
            "label": "C",
            "text": "df.nlargest(3, 'Product')"
        },
        {
            "label": "D",
            "text": "df.sort_values('Sales', ascending=False).head(3)"
        }
    ]
},


    # ============================================================
    # STATISTICS & PROBABILITY
    # ============================================================

    {
        "skill": "Statistics & Probability",
        "topic": "Mean",
        "difficulty": "Easy",
        "question_type": "Data Interpretation",
        "question_text": (
            "A dataset contains the values 10, 12, 15, 18 and 20. "
            "What is the mean?"
        ),
        "correct_answer": "B",
        "explanation": (
            "(10 + 12 + 15 + 18 + 20) / 5 = 75 / 5 = 15."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "12"},
            {"label": "B", "text": "15"},
            {"label": "C", "text": "16"},
            {"label": "D", "text": "18"}
        ]
    },

    {
        "skill": "Statistics & Probability",
        "topic": "Correlation",
        "difficulty": "Medium",
        "question_type": "Scenario",
        "question_text": (
            "An analyst finds that the correlation coefficient between "
            "hours studied and exam score is r = 0.85. What does this "
            "most strongly indicate?"
        ),
        "correct_answer": "A",
        "explanation": (
            "A correlation of +0.85 indicates a strong positive linear "
            "association. Correlation alone does not prove causation."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": (
                    "There is a strong positive linear relationship "
                    "between the two variables."
                )
            },
            {
                "label": "B",
                "text": (
                    "There is a strong negative linear relationship."
                )
            },
            {
                "label": "C",
                "text": (
                    "Studying more hours definitely causes higher scores."
                )
            },
            {
                "label": "D",
                "text": (
                    "There is no relationship between the variables."
                )
            }
        ]
    },

    {
        "skill": "Statistics & Probability",
        "topic": "Outliers and descriptive statistics",
        "difficulty": "Hard",
        "question_type": "Data Interpretation",
        "question_text": (
            "A company's employee salaries are ₹30,000, ₹32,000, ₹34,000, "
            "₹35,000, ₹36,000 and ₹2,00,000. Which measure would generally "
            "be more appropriate for representing the typical salary?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The ₹2,00,000 salary is an extreme value that strongly affects "
            "the mean. The median is less affected by extreme values."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Mean"},
            {"label": "B", "text": "Median"},
            {"label": "C", "text": "Maximum"},
            {"label": "D", "text": "Range"}
        ]
    },

    {
        "skill": "Statistics & Probability",
        "topic": "Probability",
        "difficulty": "Medium",
        "question_type": "Scenario",
        "question_text": (
            "A company has 100 customers. 60 purchased Product A, "
            "40 purchased Product B, and 25 purchased both A and B. "
            "If a customer is selected at random, what is the probability "
            "that they purchased A or B?"
        ),
        "correct_answer": "C",
        "explanation": (
            "Using the union formula: A or B = A + B - both. "
            "Therefore, 60 + 40 - 25 = 75 customers, giving a probability of 75%."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "25%"},
            {"label": "B", "text": "50%"},
            {"label": "C", "text": "75%"},
            {"label": "D", "text": "100%"}
        ]
    },
    {
    "skill": "Statistics & Probability",
    "topic": "Mean and Median",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "A dataset contains employee salaries where a few employees earn "
        "extremely high salaries compared with the rest. Which measure "
        "of central tendency is generally more appropriate for representing "
        "a typical salary?"
    ),
    "correct_answer": "B",
    "explanation": (
        "The median is less affected by extreme values or outliers than "
        "the mean, making it more appropriate for highly skewed salary data."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Mean"},
        {"label": "B", "text": "Median"},
        {"label": "C", "text": "Variance"},
        {"label": "D", "text": "Standard deviation"}
    ]
},
{
    "skill": "Statistics & Probability",
    "topic": "Standard deviation",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "What does a higher standard deviation generally indicate "
        "about a dataset?"
    ),
    "correct_answer": "C",
    "explanation": (
        "A higher standard deviation indicates that the observations "
        "are more spread out from the mean."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "The mean is always higher"},
        {"label": "B", "text": "There are no outliers"},
        {"label": "C", "text": "The data has greater variability"},
        {"label": "D", "text": "The dataset contains fewer observations"}
    ]
},

{
    "skill": "Statistics & Probability",
    "topic": "Percentiles",
    "difficulty": "Medium",
    "question_type": "MCQ",
    "question_text": (
        "A student's test score is at the 90th percentile. "
        "What does this approximately mean?"
    ),
    "correct_answer": "A",
    "explanation": (
        "A 90th percentile score means the student scored higher than "
        "approximately 90% of the observations in the reference dataset."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "The score is higher than approximately 90% of the observations"
        },
        {
            "label": "B",
            "text": "The student answered exactly 90% of questions correctly"
        },
        {
            "label": "C",
            "text": "The score is exactly 90 marks"
        },
        {
            "label": "D",
            "text": "The student belongs to the top 90% of all possible students"
        }
    ]
},
{
    "skill": "Statistics & Probability",
    "topic": "Correlation",
    "difficulty": "Medium",
    "question_type": "MCQ",
    "question_text": (
        "An analyst finds a strong positive correlation between the "
        "number of hours students spend studying and their exam scores. "
        "What can the analyst conclude from this correlation alone?"
    ),
    "correct_answer": "D",
    "explanation": (
        "Correlation indicates that two variables move together, but "
        "correlation alone does not establish that one variable causes "
        "the other."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Studying definitely causes higher exam scores"
        },
        {
            "label": "B",
            "text": "Exam scores cause students to study more"
        },
        {
            "label": "C",
            "text": "There is no relationship between the variables"
        },
        {
            "label": "D",
            "text": "The variables are positively associated, but causation is not established"
        }
    ]
},
{
    "skill": "Statistics & Probability",
    "topic": "Probability",
    "difficulty": "Medium",
    "question_type": "MCQ",
    "question_text": (
        "A dataset contains 200 customer records. 50 customers made a "
        "purchase. If one customer is selected at random, what is the "
        "probability that the selected customer made a purchase?"
    ),
    "correct_answer": "B",
    "explanation": (
        "Probability = favorable outcomes / total outcomes = 50 / 200 = 0.25, "
        "or 25%."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "10%"},
        {"label": "B", "text": "25%"},
        {"label": "C", "text": "50%"},
        {"label": "D", "text": "75%"}
    ]
},
{
    "skill": "Statistics & Probability",
    "topic": "Sampling bias",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "A company wants to understand customer satisfaction. "
        "An analyst surveys only customers who contacted customer support "
        "during the previous week. What is the main statistical concern "
        "with this sampling approach?"
    ),
    "correct_answer": "C",
    "explanation": (
        "Customers who contacted support may have experiences that differ "
        "from customers who did not contact support. Therefore, surveying "
        "only this group can introduce sampling bias and may not represent "
        "the entire customer population."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "The sample is automatically too large"
        },
        {
            "label": "B",
            "text": "The data cannot contain numerical values"
        },
        {
            "label": "C",
            "text": "The sample may not represent the entire customer population"
        },
        {
            "label": "D",
            "text": "The mean cannot be calculated from the sample"
        }
    ]
},


    # ============================================================
    # DATA CLEANING & PREPARATION
    # ============================================================

    {
        "skill": "Data Cleaning & Preparation",
        "topic": "Missing values",
        "difficulty": "Easy",
        "question_type": "Scenario",
        "question_text": (
            "A dataset contains a City column with values Delhi, Mumbai, "
            "NULL and Delhi. What is the most appropriate first step when "
            "dealing with the missing value?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The analyst should first investigate why the value is missing "
            "and then determine an appropriate treatment based on the context."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "Replace it with Delhi because Delhi is most common."
            },
            {
                "label": "B",
                "text": (
                    "Investigate why the value is missing and determine "
                    "an appropriate treatment."
                )
            },
            {
                "label": "C",
                "text": "Delete the entire dataset."
            },
            {
                "label": "D",
                "text": "Replace every city with Unknown."
            }
        ]
    },

    {
        "skill": "Data Cleaning & Preparation",
        "topic": "Duplicate records",
        "difficulty": "Medium",
        "question_type": "Scenario",
        "question_text": (
            "An employee dataset contains the same Employee ID, name and "
            "department twice. What should an analyst generally do before "
            "removing the duplicate?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The analyst should determine whether the repeated record is "
            "actually a duplicate or represents a legitimate repeated event."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Immediately delete one row."},
            {
                "label": "B",
                "text": (
                    "Investigate whether the duplicate represents an actual "
                    "duplicate or a legitimate repeated record."
                )
            },
            {"label": "C", "text": "Change the employee ID."},
            {"label": "D", "text": "Replace the department with NULL."}
        ]
    },

    {
        "skill": "Data Cleaning & Preparation",
        "topic": "Data transformation",
        "difficulty": "Hard",
        "question_type": "Scenario",
        "question_text": (
            "A Salary column contains values such as '₹45,000', '₹52,000' "
            "and '₹60,000', but the values are stored as text. Numerical "
            "calculations such as average salary are not working. What "
            "should the analyst do?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The currency symbols and separators should be handled appropriately "
            "and the values converted into a suitable numeric format."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Delete the Salary column."},
            {
                "label": "B",
                "text": (
                    "Convert the values into a suitable numeric format after "
                    "cleaning the currency symbols and separators."
                )
            },
            {"label": "C", "text": "Replace all values with row numbers."},
            {"label": "D", "text": "Convert the values to dates."}
        ]
    },
    {
    "skill": "Data Cleaning & Preparation",
    "topic": "Missing values",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "A dataset contains missing values in the Age column. "
        "Which approach should an analyst consider first before deciding "
        "how to handle the missing values?"
    ),
    "correct_answer": "C",
    "explanation": (
        "Before choosing a treatment, the analyst should understand why "
        "values are missing, how many values are missing, and whether the "
        "missingness has a meaningful pattern."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Always replace missing values with zero"},
        {"label": "B", "text": "Always delete every row containing a missing value"},
        {
            "label": "C",
            "text": "Analyze the amount and pattern of missing values"
        },
        {"label": "D", "text": "Convert all missing values to text"}
    ]
},
{
    "skill": "Data Cleaning & Preparation",
    "topic": "Duplicate records",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "A customer dataset contains the same customer record twice. "
        "What is this issue commonly called?"
    ),
    "correct_answer": "A",
    "explanation": (
        "When the same record appears more than once unintentionally, "
        "it is considered a duplicate record."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Duplicate data"},
        {"label": "B", "text": "Normalized data"},
        {"label": "C", "text": "Categorical data"},
        {"label": "D", "text": "Aggregated data"}
    ]
},
{
    "skill": "Data Cleaning & Preparation",
    "topic": "Data types",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A Sales column contains values such as '1500', '2500', and '3000', "
        "but the column has been imported as text. What problem can this "
        "cause during analysis?"
    ),
    "correct_answer": "B",
    "explanation": (
        "If numeric values are stored as text, mathematical operations "
        "and numerical calculations may not work correctly until the "
        "column is converted to an appropriate numeric type."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "The values automatically become dates"},
        {
            "label": "B",
            "text": "Numerical calculations may not work correctly"
        },
        {"label": "C", "text": "The dataset becomes automatically duplicated"},
        {"label": "D", "text": "The column can only contain missing values"}
    ]
},
{
    "skill": "Data Cleaning & Preparation",
    "topic": "Data consistency",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A Gender column contains the values 'Male', 'male', 'M', and "
        "'MALE'. What type of data-quality problem does this represent?"
    ),
    "correct_answer": "D",
    "explanation": (
        "The values represent the same category but use different formats. "
        "This is an inconsistency problem and should be standardized before analysis."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Missing data"},
        {"label": "B", "text": "Duplicate rows"},
        {"label": "C", "text": "Numerical overflow"},
        {"label": "D", "text": "Inconsistent categorical values"}
    ]
},
{
    "skill": "Data Cleaning & Preparation",
    "topic": "Outliers",
    "difficulty": "Medium",
    "question_type": "MCQ",
    "question_text": (
        "Which of the following is a common method for identifying "
        "potential outliers in a numerical dataset?"
    ),
    "correct_answer": "C",
    "explanation": (
        "The IQR method can identify observations that fall unusually far "
        "below or above the middle 50% of the data."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Counting the number of columns"},
        {"label": "B", "text": "Checking only the column names"},
        {"label": "C", "text": "Using the IQR method"},
        {"label": "D", "text": "Removing every value above the mean"}
    ]
},
{
    "skill": "Data Cleaning & Preparation",
    "topic": "Text cleaning",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A City column contains values such as 'Delhi', ' Delhi ', "
        "and 'DELHI'. What would be an appropriate cleaning step?"
    ),
    "correct_answer": "A",
    "explanation": (
        "Removing unnecessary whitespace and standardizing text case can "
        "make values consistent before grouping or analysis."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Trim whitespace and standardize the text format"
        },
        {"label": "B", "text": "Delete the entire City column"},
        {"label": "C", "text": "Convert every city into a number randomly"},
        {"label": "D", "text": "Replace every city with a missing value"}
    ]
},

{
    "skill": "Data Cleaning & Preparation",
    "topic": "Data validation",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "A student dataset contains an Age column. During validation, "
        "the analyst finds values such as -5 and 250. What is the most "
        "appropriate interpretation?"
    ),
    "correct_answer": "B",
    "explanation": (
        "These values are outside any reasonable age range and should be "
        "flagged as invalid data for investigation or correction."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "They are normal outliers that should always be kept"},
        {
            "label": "B",
            "text": "They are likely invalid values that require investigation"
        },
        {"label": "C", "text": "They should automatically be converted to dates"},
        {"label": "D", "text": "They prove that the dataset has no missing values"}
    ]
},

    # ============================================================
    # DATA VISUALIZATION & BI
    # ============================================================

    {
        "skill": "Data Visualization & BI",
        "topic": "Chart selection",
        "difficulty": "Easy",
        "question_type": "Scenario",
        "question_text": (
            "A company wants to compare the total sales of five different "
            "product categories. Which visualization would generally be "
            "most appropriate?"
        ),
        "correct_answer": "A",
        "explanation": (
            "A bar chart is well suited for comparing values across "
            "discrete categories."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Bar chart"},
            {"label": "B", "text": "Scatter plot"},
            {"label": "C", "text": "Line chart"},
            {"label": "D", "text": "Histogram"}
        ]
    },

    {
        "skill": "Data Visualization & BI",
        "topic": "Data interpretation",
        "difficulty": "Medium",
        "question_type": "Data Interpretation",
        "question_text": (
            "A company's monthly sales are ₹40,000 in January, ₹45,000 "
            "in February, ₹42,000 in March, ₹55,000 in April and ₹60,000 "
            "in May. Which statement is best supported by the data?"
        ),
        "correct_answer": "B",
        "explanation": (
            "Sales increased overall from January to May, although there "
            "was a temporary decline in March."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "Sales decreased continuously from January to May."
            },
            {
                "label": "B",
                "text": (
                    "Sales generally increased over the period, despite "
                    "a small decline in March."
                )
            },
            {"label": "C", "text": "March had the highest sales."},
            {"label": "D", "text": "Sales remained constant."}
        ]
    },

    {
        "skill": "Data Visualization & BI",
        "topic": "Dashboard design",
        "difficulty": "Hard",
        "question_type": "Scenario",
        "question_text": (
            "A manager wants a dashboard showing total revenue, number of "
            "orders, average order value, monthly revenue trend and revenue "
            "by region. Which design would be most appropriate?"
        ),
        "correct_answer": "B",
        "explanation": (
            "Different information should use visuals appropriate to its "
            "purpose. KPI cards work well for summary metrics, while trends "
            "and regional comparisons need suitable charts."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "Use a single pie chart containing all five metrics."
            },
            {
                "label": "B",
                "text": (
                    "Use KPI cards for key summary metrics, a line chart "
                    "for the monthly trend, and a suitable categorical "
                    "visual for regional revenue."
                )
            },
            {
                "label": "C",
                "text": (
                    "Use only a table containing every individual transaction."
                )
            },
            {
                "label": "D",
                "text": "Use a scatter plot for all five metrics."
            }
        ]
    },
    {
    "skill": "Data Visualization & BI",
    "topic": "Chart selection",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "An analyst wants to compare the sales of five different products. "
        "Which visualization would generally be most appropriate?"
    ),
    "correct_answer": "B",
    "explanation": (
        "A bar chart is effective for comparing values across discrete "
        "categories such as different products."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Pie chart with hundreds of slices"},
        {"label": "B", "text": "Bar chart"},
        {"label": "C", "text": "Scatter plot"},
        {"label": "D", "text": "Histogram"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "Time-series visualization",
    "difficulty": "Easy",
    "question_type": "MCQ",
    "question_text": (
        "A company wants to understand how its monthly revenue changed "
        "over the past two years. Which visualization is generally most "
        "appropriate?"
    ),
    "correct_answer": "A",
    "explanation": (
        "A line chart clearly shows changes and trends over time."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Line chart"},
        {"label": "B", "text": "Treemap"},
        {"label": "C", "text": "Donut chart"},
        {"label": "D", "text": "Gauge only"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "KPIs",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A sales manager wants a dashboard element that immediately shows "
        "whether the current month's sales target has been achieved. "
        "Which type of visualization would be most suitable?"
    ),
    "correct_answer": "C",
    "explanation": (
        "A KPI visualization can compare an actual value with a target "
        "and communicate performance quickly."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "A detailed table containing every transaction"},
        {"label": "B", "text": "A scatter plot"},
        {"label": "C", "text": "A KPI card or KPI visual"},
        {"label": "D", "text": "A histogram"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "Dashboard interactivity",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A Power BI dashboard contains sales data for several regions. "
        "The manager wants to select one or more regions and have the "
        "visualizations update accordingly. What feature would be useful?"
    ),
    "correct_answer": "D",
    "explanation": (
        "A slicer allows users to interactively filter dashboard data "
        "based on selected values."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Calculated column only"},
        {"label": "B", "text": "Data dictionary"},
        {"label": "C", "text": "Database index"},
        {"label": "D", "text": "Slicer"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "Visualization integrity",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A bar chart compares two products, but the vertical axis starts "
        "at 90 instead of 0, making a small difference appear extremely large. "
        "What is the main concern?"
    ),
    "correct_answer": "A",
    "explanation": (
        "Truncating the axis can exaggerate visual differences and potentially "
        "mislead the audience about the magnitude of the difference."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "The visualization may exaggerate the difference"},
        {"label": "B", "text": "The data automatically becomes inaccurate"},
        {"label": "C", "text": "The chart becomes a database"},
        {"label": "D", "text": "The values can no longer be calculated"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "Data storytelling",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "A dashboard contains 25 different charts, but the manager cannot "
        "quickly determine which factors are affecting declining sales. "
        "What would be the best improvement?"
    ),
    "correct_answer": "B",
    "explanation": (
        "A good analytical dashboard should prioritize the most relevant "
        "insights and provide a clear visual hierarchy rather than overwhelming "
        "the user with unnecessary charts."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Add another 20 charts"},
        {
            "label": "B",
            "text": "Remove unnecessary visuals and emphasize the key insights"
        },
        {"label": "C", "text": "Use as many colors as possible"},
        {"label": "D", "text": "Replace every chart with raw data"}
    ]
},
{
    "skill": "Data Visualization & BI",
    "topic": "Dashboard design",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "A business dashboard is intended for senior managers who need "
        "to make quick decisions. Which design approach is generally best?"
    ),
    "correct_answer": "C",
    "explanation": (
        "Decision-focused dashboards should prioritize important KPIs, "
        "clear trends, relevant comparisons, and easy-to-understand visuals."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Display every available field and metric"
        },
        {
            "label": "B",
            "text": "Use complex visualizations even when simpler ones work"
        },
        {
            "label": "C",
            "text": "Prioritize relevant KPIs and clear, actionable insights"
        },
        {
            "label": "D",
            "text": "Avoid filters so users cannot change the view"
        }
    ]
},


    # ============================================================
    # ANALYTICAL THINKING
    # ============================================================

    {
        "skill": "Analytical Thinking",
        "topic": "Identifying relevant information",
        "difficulty": "Easy",
        "question_type": "Scenario",
        "question_text": (
            "An online store notices that sales have fallen during the "
            "last month. Which information would be most useful as an "
            "initial step in investigating the decline?"
        ),
        "correct_answer": "B",
        "explanation": (
            "Product, regional and time-based sales data can help identify "
            "where and when the decline occurred."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "The color of the company's logo."},
            {
                "label": "B",
                "text": (
                    "Previous and current sales data broken down by "
                    "product, region and time."
                )
            },
            {
                "label": "C",
                "text": (
                    "The number of employees in the company's HR department."
                )
            },
            {"label": "D", "text": "The company's founding year."}
        ]
    },

    {
        "skill": "Analytical Thinking",
        "topic": "Pattern identification",
        "difficulty": "Medium",
        "question_type": "Data Interpretation",
        "question_text": (
            "A website has 10,000 visits and 500 orders in January, "
            "12,000 visits and 600 orders in February, 15,000 visits "
            "and 750 orders in March, and 20,000 visits but only 400 "
            "orders in April. What should the analyst investigate first?"
        ),
        "correct_answer": "B",
        "explanation": (
            "April has the highest traffic but significantly fewer orders. "
            "This suggests a possible change in conversion rate, user "
            "experience, product availability or another factor."
        ),
        "marks": 1,
        "options": [
            {"label": "A", "text": "Why website visits stopped increasing."},
            {
                "label": "B",
                "text": (
                    "Why orders decreased despite a large increase "
                    "in website visits."
                )
            },
            {
                "label": "C",
                "text": "Why January had the highest number of orders."
            },
            {
                "label": "D",
                "text": "Why February had fewer visits than April."
            }
        ]
    },

    {
        "skill": "Analytical Thinking",
        "topic": "Business problem solving",
        "difficulty": "Hard",
        "question_type": "Scenario",
        "question_text": (
            "A company's overall sales have fallen by 15%. However, "
            "Region A increased by 20%, Region B increased by 15%, "
            "and Region C decreased by 60%. What would be the most "
            "appropriate next step?"
        ),
        "correct_answer": "B",
        "explanation": (
            "The dramatic decline in Region C should be investigated "
            "to understand what caused the regional drop before making "
            "a broader business recommendation."
        ),
        "marks": 1,
        "options": [
            {
                "label": "A",
                "text": "Conclude that the entire business is performing poorly."
            },
            {
                "label": "B",
                "text": (
                    "Focus the investigation on Region C to identify "
                    "what caused its decline."
                )
            },
            {
                "label": "C",
                "text": (
                    "Ignore regional differences and analyze only total sales."
                )
            },
            {
                "label": "D",
                "text": "Immediately increase prices in all regions."
            }
        ]
    },
    {
    "skill": "Analytical Thinking",
    "topic": "Metric selection",
    "difficulty": "Easy",
    "question_type": "Scenario",
    "question_text": (
        "An e-commerce company wants to know how many visitors actually "
        "completed a purchase. Which metric would be most directly useful?"
    ),
    "correct_answer": "B",
    "explanation": (
        "The conversion rate measures the proportion of visitors who "
        "complete the desired action, such as making a purchase."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "Average page loading time"},
        {"label": "B", "text": "Conversion rate"},
        {"label": "C", "text": "Number of website colors"},
        {"label": "D", "text": "Average customer age"}
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Comparative analysis",
    "difficulty": "Easy",
    "question_type": "Scenario",
    "question_text": (
        "A company's sales increased from ₹10 lakh to ₹12 lakh this year. "
        "Which additional information would be most useful for determining "
        "whether this growth is actually strong?"
    ),
    "correct_answer": "C",
    "explanation": (
        "Comparing the company's growth with previous periods, targets, "
        "or relevant benchmarks provides context for interpreting the increase."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "The company's logo design"},
        {"label": "B", "text": "The number of columns in the sales database"},
        {
            "label": "C",
            "text": "Previous sales performance or an appropriate benchmark"
        },
        {"label": "D", "text": "The names of all employees"}
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Root-cause analysis",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A dashboard suddenly shows that sales dropped by 40% compared "
        "with the previous month. What should an analyst do first?"
    ),
    "correct_answer": "A",
    "explanation": (
        "Before drawing conclusions, the analyst should validate the data "
        "and investigate whether the change is genuine or caused by an "
        "issue such as missing records, changed definitions, or data errors."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Check the data and investigate possible causes"
        },
        {
            "label": "B",
            "text": "Immediately conclude that customers dislike the product"
        },
        {
            "label": "C",
            "text": "Delete the month from the dataset"
        },
        {
            "label": "D",
            "text": "Change the dashboard until the decrease disappears"
        }
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Confounding factors",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A company notices that ice cream sales and electricity usage "
        "both increase during certain months. What is a reasonable factor "
        "that could influence both?"
    ),
    "correct_answer": "D",
    "explanation": (
        "Temperature or season can influence both ice cream consumption "
        "and electricity usage, for example through increased use of air conditioning."
    ),
    "marks": 1,
    "options": [
        {"label": "A", "text": "The company's database password"},
        {"label": "B", "text": "The number of spreadsheet columns"},
        {"label": "C", "text": "The employee ID format"},
        {"label": "D", "text": "Season or temperature"}
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Problem definition",
    "difficulty": "Medium",
    "question_type": "Scenario",
    "question_text": (
        "A food-delivery company reports that customer retention is falling. "
        "Which question would be most useful for an analyst investigating "
        "the problem?"
    ),
    "correct_answer": "B",
    "explanation": (
        "Breaking the problem into measurable factors such as delivery time, "
        "pricing, order experience, and customer segments can help identify "
        "potential drivers of declining retention."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "How many colors are used in the company's application?"
        },
        {
            "label": "B",
            "text": "Which customer segments and factors are associated with lower retention?"
        },
        {
            "label": "C",
            "text": "Which employee has the longest name?"
        },
        {
            "label": "D",
            "text": "How many tables exist in the database?"
        }
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Interpreting results",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "An analyst finds that students who participate in more coding "
        "practice sessions tend to receive higher placement-test scores. "
        "Which conclusion is most appropriate?"
    ),
    "correct_answer": "C",
    "explanation": (
        "The data shows an association between practice frequency and scores, "
        "but other factors may also influence performance. The relationship "
        "alone does not prove that practice is the only cause."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Coding practice is definitely the only reason for higher scores"
        },
        {
            "label": "B",
            "text": "Students with fewer sessions cannot improve their scores"
        },
        {
            "label": "C",
            "text": "More practice is associated with higher scores, but other factors may also matter"
        },
        {
            "label": "D",
            "text": "The dataset proves that every student should practice the same number of hours"
        }
    ]
},
{
    "skill": "Analytical Thinking",
    "topic": "Actionable insights",
    "difficulty": "Hard",
    "question_type": "Scenario",
    "question_text": (
        "An analysis shows that a company's customers who experience "
        "long delivery times are much more likely to stop ordering. "
        "Which recommendation is the most directly actionable?"
    ),
    "correct_answer": "A",
    "explanation": (
        "The recommendation should address the factor identified in the "
        "analysis. Investigating and reducing excessive delivery times is "
        "more directly connected to the observed retention problem."
    ),
    "marks": 1,
    "options": [
        {
            "label": "A",
            "text": "Investigate and reduce excessive delivery times"
        },
        {
            "label": "B",
            "text": "Change the company logo"
        },
        {
            "label": "C",
            "text": "Collect unrelated customer information"
        },
        {
            "label": "D",
            "text": "Remove delivery data from future analysis"
        }
    ]
}
]