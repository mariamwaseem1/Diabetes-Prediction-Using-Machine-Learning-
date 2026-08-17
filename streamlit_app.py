import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_diabetes_model.pkl")

st.set_page_config(
    page_title="Mariam Wassem Diabetes Prediction App",
    page_icon="🩸",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #2f3136;
        color: #f9fafb;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    h1, h2, h3, h4, h5, h6, p, label,
    .stMarkdown, .stText, .stCaption {
        color: #f9fafb !important;
    }

    .title-card {
        background: linear-gradient(135deg, #111827, #374151);
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.45);
        margin-bottom: 25px;
        text-align: center;
    }

    .title-card h1 {
        color: #ffffff !important;
        font-size: 42px;
        margin-bottom: 10px;
    }

    .title-card p {
        color: #e5e7eb !important;
        font-size: 18px;
    }

    .section-card {
        background-color: #3b3f46;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.30);
        margin-bottom: 20px;
    }

    .section-card h3, .section-card p {
        color: #ffffff !important;
    }

    .high-risk-card {
        background: linear-gradient(135deg, #7f1d1d, #dc2626);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.35);
    }

    .low-risk-card {
        background: linear-gradient(135deg, #064e3b, #059669);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.35);
    }

    .high-risk-card *, .low-risk-card * {
        color: #ffffff !important;
    }

    div.stButton > button {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.5rem !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 18px !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background-color: #dc2626 !important;
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #1f2937 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #f9fafb !important;
    }

    div[data-baseweb="select"] > div,
    input,
    textarea {
        color: #111827 !important;
        background-color: #f3f4f6 !important;
    }

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] input,
    div[data-baseweb="select"] svg {
        color: #111827 !important;
        fill: #111827 !important;
    }

    ul[role="listbox"] {
        background-color: #f3f4f6 !important;
        color: #111827 !important;
    }

    li[role="option"],
    li[role="option"] div,
    li[role="option"] span {
        color: #111827 !important;
        background-color: #f3f4f6 !important;
    }

    li[role="option"]:hover {
        background-color: #d1d5db !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("## 🩸 About the App")
    st.write("This app predicts diabetes risk using demographic and clinical patient data.")

    st.markdown("## 👩‍💻 Developed by")
    st.write("**Mariam Wassem**")
    st.write("**ID: 231001582**")

    st.markdown("## 📌 Model Note")
    st.write("This model is a screening support tool and does not replace medical diagnosis.")

st.markdown(
    """
    <div class="title-card">
        <h1>🩸 Mariam Wassem Diabetes Prediction App</h1>
        <p>Enter patient information to estimate diabetes risk using a trained machine learning model.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-card">
        <h3>👤 Patient Information</h3>
        <p>Please fill in the following demographic and clinical features.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    age = st.slider("Age", 1, 100, 45)
    hypertension = st.radio("Hypertension", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)
    heart_disease = st.radio("Heart Disease", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)

with col2:
    smoking_history = st.selectbox(
        "Smoking History",
        ["never", "former", "current", "not current", "ever", "unknown"]
    )
    bmi = st.number_input("BMI", min_value=10.0, max_value=80.0, value=25.0)
    hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, value=5.5)
    glucose = st.number_input("Blood Glucose Level", min_value=50, max_value=400, value=100)

age_group = pd.cut(
    [age],
    bins=[0, 18, 35, 50, 65, 100],
    labels=["Child", "Young Adult", "Adult", "Senior", "Elderly"]
)[0]

bmi_category = pd.cut(
    [bmi],
    bins=[0, 18.5, 24.9, 29.9, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"]
)[0]

hba1c_category = pd.cut(
    [hba1c],
    bins=[0, 5.7, 6.4, 20],
    labels=["Normal", "Prediabetes", "Diabetes Range"]
)[0]

glucose_category = pd.cut(
    [glucose],
    bins=[0, 140, 199, 500],
    labels=["Normal", "Prediabetes", "Diabetes Range"]
)[0]

input_data = pd.DataFrame({
    "gender": [gender],
    "age": [age],
    "hypertension": [hypertension],
    "heart_disease": [heart_disease],
    "smoking_history": [smoking_history],
    "bmi": [bmi],
    "HbA1c_level": [hba1c],
    "blood_glucose_level": [glucose],
    "age_group": [age_group],
    "bmi_category": [bmi_category],
    "hba1c_category": [hba1c_category],
    "glucose_category": [glucose_category]
})

with st.expander("View automatically generated health categories"):
    st.write("Age Group:", age_group)
    st.write("BMI Category:", bmi_category)
    st.write("HbA1c Category:", hba1c_category)
    st.write("Glucose Category:", glucose_category)

st.markdown("### 🔍 Prediction")

if st.button("Predict Diabetes Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    risk_percent = probability * 100

    st.metric("Diabetes Probability", f"{risk_percent:.1f}%")
    st.progress(min(int(risk_percent), 100))

    if prediction == 1:
        st.markdown(
            f"""
            <div class="high-risk-card">
                <h2>⚠️ High Diabetes Risk Detected</h2>
                <p>The model predicts that this patient may be at high risk of diabetes.</p>
                <p><b>Predicted probability:</b> {risk_percent:.2f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="low-risk-card">
                <h2>✅ Low Diabetes Risk Predicted</h2>
                <p>The model predicts that this patient is less likely to have diabetes based on the provided data.</p>
                <p><b>Predicted probability:</b> {risk_percent:.2f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Patient Input Summary")
    st.dataframe(input_data)