import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("❤️ Heart Disease Prediction App")

# Input fields
age = st.number_input("Age", 1, 120)
gender = st.selectbox("Gender", ['Male', 'Female'])
bp = st.number_input("Resting Blood Pressure", 80, 200)
cholesterol = st.number_input("Cholesterol", 100, 600)
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'ASY', 'TA'])
rest_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Max Heart Rate", 60, 220)
exercise_angina = st.selectbox("Exercise-Induced Angina", ['Yes', 'No'])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0, step=0.1)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])


# Encode categorical data
le = LabelEncoder()
gender = le.fit(['Male', 'Female']).transform([gender])[0]
chest_pain = le.fit(['ATA', 'NAP', 'ASY', 'TA']).transform([chest_pain])[0]
rest_ecg = le.fit(['Normal', 'ST', 'LVH']).transform([rest_ecg])[0]
exercise_angina = le.fit(['Yes', 'No']).transform([exercise_angina])[0]
st_slope = le.fit(['Up', 'Flat', 'Down']).transform([st_slope])[0]

input_data = np.array([[age, gender, bp, cholesterol, chest_pain,
                        rest_ecg, max_hr, exercise_angina, oldpeak,
                        st_slope, fasting_bs]])

# Predict
input_data = np.array([[age, gender, bp, cholesterol, chest_pain,
                        rest_ecg, max_hr, exercise_angina, oldpeak, st_slope]])

if st.button("Predict"):
    result = model.predict(input_data)
    output = "Positive for Heart Disease" if result[0] == 1 else "No Heart Disease"
    st.subheader(f"Prediction: {output}")
