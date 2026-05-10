import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# Page Config
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Load Model and Scaler
model = joblib.load("attrition_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title(" Employee Attrition Analysis Dashboard")

st.markdown("""
This dashboard predicts employee attrition using Machine Learning and provides HR analytics insights.
""")

# KPI SECTION
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

attrition_count = len(df[df['Attrition'] == 'Yes'])

attrition_rate = round(
    (attrition_count / len(df)) * 100,
    2
)

col1.metric("Total Employees", len(df))
col2.metric("Employees Left", attrition_count)
col3.metric("Attrition Rate", f"{attrition_rate}%")

st.divider()

# ATTRITION DISTRIBUTION
st.subheader("Attrition Distribution")

fig1 = px.histogram(
    df,
    x="Attrition",
    color="Attrition",
    text_auto=True
)

st.plotly_chart(fig1, use_container_width=True)

# DEPARTMENT ATTRITION
st.subheader("Department-wise Attrition")

fig2 = px.histogram(
    df,
    x="Department",
    color="Attrition",
    barmode="group"
)

st.plotly_chart(fig2, use_container_width=True)

# MONTHLY INCOME
st.subheader("Monthly Income vs Attrition")

fig3 = px.box(
    df,
    x="Attrition",
    y="MonthlyIncome",
    color="Attrition"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# PREDICTION SECTION
st.header("Predict Employee Attrition")

st.markdown("Enter employee details below:")

# USER INPUTS

age = st.slider("Age", 18, 60, 30)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=50000,
    value=10000
)

years_at_company = st.slider(
    "Years at Company",
    0,
    40,
    5
)

job_level = st.slider(
    "Job Level",
    1,
    5,
    2
)

job_satisfaction = st.slider(
    "Job Satisfaction",
    1,
    4,
    3
)

overtime = st.selectbox(
    "OverTime",
    ["Yes", "No"]
)

# Encode Overtime
overtime_value = 1 if overtime == "Yes" else 0

# Create Input DataFrame
input_data = pd.DataFrame({
    'Age': [age],
    'MonthlyIncome': [monthly_income],
    'YearsAtCompany': [years_at_company],
    'JobLevel': [job_level],
    'JobSatisfaction': [job_satisfaction],
    'OverTime': [overtime_value]
})

# SCALE INPUT
input_scaled = scaler.transform(input_data)

# PREDICT BUTTON
if st.button("Predict Attrition"):

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(
            f"⚠️ High Risk of Attrition\n\nProbability: {probability:.2f}"
        )
    else:
        st.success(
            f"✅ Low Risk of Attrition\n\nProbability: {probability:.2f}"
        )