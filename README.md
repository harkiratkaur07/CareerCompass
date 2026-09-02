# CareerCompass

**CareerCompass** is a Placement Readiness Analytics Platform designed to help students evaluate their readiness for Data Analyst roles through skill-based assessments, performance tracking, personalized recommendations, and machine learning-based placement prediction.

## Features

* Student registration and login
* Student profile management
* Skill-based placement assessments
* Automatic assessment scoring
* Skill-wise performance analysis
* Personalized recommendations based on skill gaps
* Progress tracking across assessments
* Interactive performance visualizations
* Placement readiness evaluation
* Machine learning-based placement probability prediction
* ML insights based on academic, background, skill, and improvement data

## Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Bcrypt
* MySQL

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js
* Jinja2

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Logistic Regression

## Machine Learning

CareerCompass uses a **hybrid rule-based + machine learning approach**.

The rule-based system evaluates a student's current assessment performance, identifies skill gaps, and generates personalized recommendations.

The machine learning component uses **Logistic Regression** to predict placement status based on:

* CGPA
* Internships
* Projects
* Certifications
* Aptitude score
* Communication score
* Skill scores
* Improvement rate

The final model achieved:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 63.90% |
| Precision | 63.11% |
| Recall    | 62.99% |
| F1 Score  | 63.05% |
| ROC-AUC   | 69.00% |

## Skills Assessed

CareerCompass evaluates students across seven skill areas:

1. Excel & Spreadsheet Analysis
2. SQL & Database Analysis
3. Python for Data Analysis
4. Statistics & Probability
5. Data Cleaning & Preparation
6. Data Visualization & BI
7. Analytical Thinking

## Project Structure

```text
CareerCompass/
│
├── app.py
├── config/
├── data/
├── ml/
├── models/
├── routes/
├── scripts/
├── templates/
├── static/
├── requirements.txt
├── test_ml.py
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harkiratkaur07/CareerCompass.git
cd CareerCompass
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your local database configuration.

**Do not commit the `.env` file to GitHub.**

### 5. Run the application

```bash
python app.py
```

Then open the local Flask URL shown in the terminal.

## Project Goal

The goal of CareerCompass is to provide students with a data-driven understanding of their placement preparation by combining assessment performance, skill-gap analysis, progress tracking, personalized recommendations, and machine learning-based placement prediction.
