import streamlit as st
import pandas as pd
import joblib

# 1️⃣ Load the trained model
model_path = "best_model.pkl"  # path to your saved RandomizedSearchCV
model = joblib.load(model_path)

# 2️⃣ Page title
st.set_page_config(page_title="Heart Disease Prediction App", layout="centered")
st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to predict the risk of heart disease.")

# 3️⃣ Feature descriptions
feature_info = {
    "oldpeak": "ST depression induced by exercise relative to rest (numeric, e.g., 1.2).",
    "cp_4.0": "Chest pain type 4 (1 = typical angina, 0 = otherwise).",
    "exang_1.0": "Exercise induced angina (1 = yes, 0 = no).",
    "slope_2.0": "Slope of the ST segment during peak exercise (2 = flat, 1 = upsloping, 0 = downsloping).",
    "thal_7.0": "Thalassemia type 7 (1 = fixed defect, 0 = otherwise).",
    "ca_1.0": "Number of major vessels colored by fluoroscopy = 1 (1 = yes, 0 = no).",
    "ca_2.0": "Number of major vessels colored by fluoroscopy = 2 (1 = yes, 0 = no).",
    "ca_3.0": "Number of major vessels colored by fluoroscopy = 3 (1 = yes, 0 = no)."
}

# 4️⃣ Collect user input with descriptions
user_input = {}
for feature, description in feature_info.items():
    if feature == "oldpeak":
        user_input[feature] = st.number_input(f"{feature} - {description}", value=0.0, step=0.1)
    else:
        user_input[feature] = st.selectbox(f"{feature} - {description}", [0, 1], index=0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input])


if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low/No Heart Disease Risk (Probability: {probability:.2f})")
