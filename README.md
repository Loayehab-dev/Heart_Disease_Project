# ❤️ Heart Disease Prediction App

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## **Overview**

This project is an interactive **Heart Disease Prediction App** built with **Streamlit** and **Random Forest**.  
It predicts the risk of heart disease using **8 selected patient features** and provides a **risk probability score**.

The model has been optimized using **RandomizedSearchCV** for best accuracy.

---

## **Selected Features**

| Feature     | Description |
|------------|-------------|
| oldpeak    | ST depression induced by exercise relative to rest (numeric) |
| cp_4.0     | Chest pain type 4 (1 = typical angina, 0 = otherwise) |
| exang_1.0  | Exercise induced angina (1 = yes, 0 = no) |
| slope_2.0  | Slope of ST segment during peak exercise (2 = flat, 1 = upsloping, 0 = downsloping) |
| thal_7.0   | Thalassemia type 7 (1 = fixed defect, 0 = otherwise) |
| ca_1.0     | Number of major vessels colored by fluoroscopy = 1 (1 = yes, 0 = no) |
| ca_2.0     | Number of major vessels colored by fluoroscopy = 2 (1 = yes, 0 = no) |
| ca_3.0     | Number of major vessels colored by fluoroscopy = 3 (1 = yes, 0 = no) |

---

## **Model Performance**

| Model               | Accuracy |
|--------------------|----------|
| Baseline Random Forest | 0.82     |
| GridSearchCV          | 0.85     |
| RandomizedSearchCV    | 0.87 ✅ |

**Best Model Hyperparameters (RandomizedSearchCV):**

```json
{
    "n_estimators": 300,
    "min_samples_split": 5,
    "min_samples_leaf": 4,
    "max_depth": 5,
    "bootstrap": true
}
Installation

Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>


Install dependencies:

pip install -r requirements.txt


requirements.txt should include:

pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
streamlit

Usage

Run the Streamlit app:

streamlit run app.py


Open the URL displayed in the terminal to access the app.

Enter patient data for the 8 features and click Predict.

The app will display:

✅ Low Risk

⚠️ High Risk

with risk probability.

Sample Test Data
oldpeak	cp_4.0	exang_1.0	slope_2.0	thal_7.0	ca_1.0	ca_2.0	ca_3.0	Expected Risk
0.0	0	0	0	0	0	0	0	Low Risk ✅
0.5	1	0	1	0	0	0	0	Low Risk ✅
1.2	0	1	0	1	0	0	0	High Risk ⚠️
2.3	0	1	0	0	0	1	0	High Risk ⚠️
1.0	1	0	0	0	1	0	0	High Risk ⚠️
Folder Structure
HeartDiseaseApp/
├─ Models/
│  ├─ best_model.pkl       # Optimized Random Forest model
│  └─ app.py               # Streamlit application
├─ test_data.csv           # Sample test data
├─ README.md
├─ requirements.txt

Notes

Ensure that user inputs match the 8 selected features exactly.

oldpeak is numeric; all other features are binary (0/1).

The app is ready for deployment and testing in the browser using Streamlit.

