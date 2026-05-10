# Employee Attrition Analysis

## Overview

Employee Attrition Analysis is a Machine Learning and HR Analytics project designed to predict whether an employee is likely to leave an organization. The project uses employee-related information such as salary, overtime, job satisfaction, and years at company to analyze attrition patterns and provide predictive insights.

The project includes:

* Exploratory Data Analysis (EDA)
* Machine Learning model training
* Model evaluation and comparison
* Feature importance analysis
* Interactive Streamlit dashboard
* Attrition prediction system

---

# Problem Statement

Employee attrition is one of the major challenges faced by organizations. High employee turnover increases:

* Recruitment costs
* Employee training expenses
* Productivity loss
* Team instability

The goal of this project is to identify factors influencing attrition and predict employees who are at higher risk of leaving.

---

# Objectives

* Analyze employee attrition patterns
* Identify important factors affecting attrition
* Build machine learning models for prediction
* Compare multiple classification algorithms
* Deploy an interactive HR analytics dashboard using Streamlit

---

# Dataset

Dataset Used:
IBM HR Analytics Employee Attrition Dataset

The dataset contains employee-related features such as:

* Age
* Monthly Income
* Job Satisfaction
* Years at Company
* Department
* Overtime
* Job Level
* Attrition Status

Dataset Size:

* Rows: 1470
* Columns: 35

---

# Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* Joblib
* Streamlit

## Tools

* Google Colab
* Visual Studio Code
* GitHub

---

# Exploratory Data Analysis

The following analyses were performed:

* Attrition Distribution
* Overtime vs Attrition
* Monthly Income vs Attrition
* Department-wise Attrition
* Age Distribution
* Correlation Heatmap

## Key Insights

* Employees working overtime show higher attrition.
* Lower monthly income is associated with higher employee turnover.
* Sales department has comparatively higher attrition.
* Younger employees are more likely to leave the organization.

---

# Machine Learning Models

The following models were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

## Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score

---

# Final Model Selection

After comparing all models, Logistic Regression was selected as the final model because it achieved the best overall performance and generalization capability on the dataset.

## Final Model Performance

* Accuracy: 87%
* ROC-AUC Score: 0.67+

---

# Features Used for Final Deployment

The final deployed model uses the following features:

* Age
* Monthly Income
* Years At Company
* Job Level
* Job Satisfaction
* Overtime

---

# Streamlit Dashboard Features

The Streamlit dashboard includes:

* HR Analytics Dashboard
* Attrition Distribution Charts
* Department-wise Analysis
* Salary Analysis
* Employee Attrition Prediction Form
* Attrition Risk Prediction
* Probability Score Display

---

# Project Structure

```text
employee-attrition-analysis/
│
├── app.py
├── attrition_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── WA_Fn-UseC_-HR-Employee-Attrition.csv
```

---

# How to Run the Project

## Step 1: Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Step 2: Open Project Folder

```bash
cd employee-attrition-analysis
```

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Run Streamlit App

```bash
streamlit run app.py
```

---

# Screenshots

Add project screenshots here:

* Dashboard Home Page
* Attrition Graphs
* Prediction Page
* KPI Metrics

---

# Business Impact

This project can help HR departments:

* Identify employees at risk of leaving
* Improve employee retention strategies
* Reduce hiring and training costs
* Improve workforce planning
* Enhance employee satisfaction

---

# Future Improvements

Possible future enhancements:

* SHAP Explainability
* Advanced Deep Learning Models
* Real-time HR Analytics
* Employee Recommendation System
* Cloud Deployment
* Database Integration

---

# Conclusion

Employee Attrition Analysis demonstrates how Machine Learning and HR Analytics can help organizations understand employee behavior and reduce attrition.

The project successfully:

* Identified important attrition factors
* Built predictive machine learning models
* Compared multiple algorithms
* Developed an interactive analytics dashboard
* Enabled real-time attrition prediction

This project highlights the practical application of Artificial Intelligence in Human Resource Management.

---

# Author

Vaidehi Purohit

B.Tech Student | AI & Machine Learning Enthusiast | Backend Developer
