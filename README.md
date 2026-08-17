# Mariam Wassem Diabetes Prediction Project

## Project Title

**Diabetes Prediction Using Machine Learning**

## Student Information

**Name:** Mariam Wassem
**ID:** 231001582
**Course:** CBIO313: Data Mining and Machine Learning

---

## Project Description

This project aims to predict diabetes risk using demographic and clinical patient information. The project follows a complete machine learning workflow, including data loading, data cleaning, exploratory data analysis, feature engineering, preprocessing, model training, model comparison, hyperparameter tuning, model evaluation, and deployment using Streamlit.

The final trained model was deployed in an interactive web application titled:

**Mariam Wassem Diabetes Prediction App**

The app allows users to enter patient information and receive an instant diabetes risk prediction with a probability score.

---

## Dataset Source

The dataset was obtained from Kaggle:

https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

Dataset file used:

```text
diabetes_prediction_dataset.csv
```

---

## Dataset Overview

The dataset includes demographic and clinical patient features such as:

* Gender
* Age
* Hypertension
* Heart disease
* Smoking history
* BMI
* HbA1c level
* Blood glucose level
* Diabetes status

The target variable is:

```text
diabetes
```

Where:

```text
0 = Non-diabetic
1 = Diabetic
```

---

## Data Cleaning

The dataset was inspected before model training. The cleaning phase included:

* Checking the dataset shape and data types
* Checking missing values
* Checking duplicated rows
* Removing duplicated records
* Standardizing column names
* Replacing unclear smoking history values such as `No Info` with `unknown`
* Saving the cleaned dataset as `Cleaned_Diabetes_Data.csv`

Although the dataset did not contain missing values, it contained duplicated rows and unclear category labels, so preprocessing was required before training the models.

---

## Feature Engineering

New clinically meaningful features were created to improve interpretability and model learning:

* `age_group`: Categorizes patients by age range
* `bmi_category`: Categorizes BMI values into weight groups
* `hba1c_category`: Categorizes HbA1c values into normal, prediabetes, and diabetes range
* `glucose_category`: Categorizes blood glucose values into normal, prediabetes, and diabetes range

These features help represent medical risk levels more clearly.

---

## Exploratory Data Analysis

Several visualizations were created to understand the dataset and the relationship between features and diabetes status.

The plots include:

* Target distribution
* Age distribution
* BMI distribution
* HbA1c level distribution
* Blood glucose level distribution
* Age vs diabetes
* BMI vs diabetes
* Hypertension vs diabetes
* Heart disease vs diabetes
* Smoking history vs diabetes
* Correlation heatmap

These plots helped identify important variables such as HbA1c level, blood glucose level, BMI, age, hypertension, and heart disease.

---

## Machine Learning Models

Six machine learning algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine
5. K-Nearest Neighbors
6. Gradient Boosting

The models were compared using multiple evaluation metrics instead of accuracy alone.

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC AUC
* Classification report
* Confusion matrix
* ROC curve

Since diabetes prediction is a healthcare-related task, recall is important because missing diabetic patients may delay diagnosis and treatment. Precision is also important because it shows how reliable high-risk predictions are.

---

## Final Model

After comparing different models, the final selected model was tuned using GridSearchCV and saved as:

```text
best_diabetes_model.pkl
```

The final model showed strong overall performance, especially in accuracy, precision, F1-score, and ROC AUC. The model can distinguish diabetic and non-diabetic patients effectively, but it should be used only as a screening support tool and not as a replacement for medical diagnosis.

---

## Model Deployment

The final model was deployed using Streamlit.

The deployment file is:

```text
streamlit_app.py
```

The app allows the user to enter:

* Gender
* Age
* Hypertension status
* Heart disease status
* Smoking history
* BMI
* HbA1c level
* Blood glucose level

Then the app predicts whether the patient has:

```text
High diabetes risk
```

or

```text
Low diabetes risk
```

It also displays the predicted probability.

---

## Project Files

The project repository includes:

```text
Mariam Wassem_231001582_Project.ipynb
diabetes_prediction_dataset.csv
Cleaned_Diabetes_Data.csv
X_features.csv
y_target.csv
model_comparison_results.csv
best_diabetes_model.pkl
streamlit_app.py
requirements.txt
README.md
diabetes_project_plots/
```

---

## How to Run the Project

### 1. Clone or download the repository

Download the project folder or clone it from GitHub.

### 2. Install required packages

Run this command in the terminal:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

Run:

```bash
streamlit run streamlit_app.py
```

### 4. Open the app

The app will open in the browser at:

```text
http://localhost:8501
```

---

## Requirements

The required Python packages are:

```text
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## Example Test Cases

### High Diabetes Risk Example

```text
Gender: Male
Age: 68
Hypertension: Yes
Heart Disease: Yes
Smoking History: former
BMI: 36.5
HbA1c Level: 8.2
Blood Glucose Level: 240
```

This patient is expected to be predicted as high diabetes risk because the input includes older age, hypertension, heart disease, high BMI, high HbA1c, and high blood glucose level.

### Low Diabetes Risk Example

```text
Gender: Female
Age: 24
Hypertension: No
Heart Disease: No
Smoking History: never
BMI: 22.0
HbA1c Level: 5.2
Blood Glucose Level: 90
```

This patient is expected to be predicted as low diabetes risk because the input values show younger age, normal BMI, normal HbA1c, normal glucose level, and no major clinical risk factors.

---

## Important Note

This machine learning model is intended for educational purposes and should be interpreted as a screening support tool only. It does not replace professional medical diagnosis, laboratory testing, or consultation with healthcare professionals.

---

## Conclusion

This project demonstrates a complete machine learning workflow for diabetes prediction. Starting from the raw dataset, the data was cleaned, explored, engineered, modeled, evaluated, and finally deployed using Streamlit. The final web application provides an interactive way to test diabetes risk prediction using patient information.
