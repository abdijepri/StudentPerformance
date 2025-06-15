import streamlit as st
import joblib
import pandas as pd
import json

# Load model dan scaler
rf_model = joblib.load('models/rf_model.pkl')
scaler = joblib.load('scaler.pkl')
model_features = joblib.load('model_features.pkl')  # Gunakan yang hanya memuat 20 fitur terpilih

# Load mapping dari data.json
with open('data.json') as f:
    data_json = json.load(f)

st.title("Student Status Prediction")

# Fungsi input pengguna berdasarkan fitur terpilih
def user_input_form(data_json):
    inputs = {}

    inputs['Student_Name'] = st.text_input("Student Name")
    
    col1, col2 = st.columns(2)

    with col1:
        inputs['Application_mode'] = st.selectbox("Application Mode", list(data_json['data_application_mode'].values()))
        inputs['Course'] = st.selectbox("Course", list(data_json['data_course'].values()))
        inputs['Mothers_qualification'] = st.selectbox("Mother's Qualification", list(data_json['data_parents_qualification'].values()))
        inputs['Mothers_occupation'] = st.selectbox("Mother's Occupation", list(data_json['data_parents_occupation'].values()))
        inputs['Previous_qualification_grade'] = st.number_input("Previous Qualification Grade", 0.0, 200.0)
        inputs['Admission_grade'] = st.number_input("Admission Grade", 0.0, 200.0)
        inputs['Curricular_units_1st_sem_enrolled'] = st.number_input("1st Sem: Enrolled Units", 0)
        inputs['Curricular_units_1st_sem_evaluations'] = st.number_input("1st Sem: Evaluations", 0)
        inputs['Curricular_units_1st_sem_approved'] = st.number_input("1st Sem: Approved Units", 0)
        inputs['Curricular_units_1st_sem_grade'] = st.number_input("1st Sem: Grade", 0.0, 20.0)

    with col2:
        inputs['Tuition_fees_up_to_date'] = st.selectbox("Tuition Fees Up-to-Date", list(data_json['data_yes_no'].values()))
        inputs['Age_at_enrollment'] = st.number_input("Age at Enrollment", 17, 100)
        inputs['Fathers_qualification'] = st.selectbox("Father's Qualification", list(data_json['data_parents_qualification'].values()))
        inputs['Fathers_occupation'] = st.selectbox("Father's Occupation", list(data_json['data_parents_occupation'].values()))
        inputs['Unemployment_rate'] = st.number_input("Unemployment Rate (%)", 0.0, 100.0)
        inputs['GDP'] = st.number_input("GDP per Capita", 0.0)
        inputs['Curricular_units_2nd_sem_enrolled'] = st.number_input("2nd Sem: Enrolled Units", 0)
        inputs['Curricular_units_2nd_sem_evaluations'] = st.number_input("2nd Sem: Evaluations", 0)
        inputs['Curricular_units_2nd_sem_approved'] = st.number_input("2nd Sem: Approved Units", 0)
        inputs['Curricular_units_2nd_sem_grade'] = st.number_input("2nd Sem: Grade", 0.0, 20.0)
        

    return inputs

# Enkode kategori berdasarkan mapping data.json
def encode_inputs(inputs, data_json):
    encoded = inputs.copy()

    # Mapping kategori ke angka
    mappings = {
        'Application_mode': data_json['data_application_mode'],
        'Course': data_json['data_course'],
        'Mothers_qualification': data_json['data_parents_qualification'],
        'Fathers_qualification': data_json['data_parents_qualification'],
        'Mothers_occupation': data_json['data_parents_occupation'],
        'Fathers_occupation': data_json['data_parents_occupation'],
        'Tuition_fees_up_to_date': data_json['data_yes_no']
    }

    for col, mapping in mappings.items():
        reverse_map = {v: int(k) for k, v in mapping.items()}
        encoded[col] = reverse_map[inputs[col]]

    return encoded

# Main proses
inputs = user_input_form(data_json)

if st.button("Submit"):
    student_name = inputs.pop('Student_Name')  # Remove name before encoding and prediction
    encoded_inputs = encode_inputs(inputs, data_json)
    input_df = pd.DataFrame([encoded_inputs], columns=model_features)

    # Scaling
    input_scaled = scaler.transform(input_df)

    # Prediksi
    prediction = rf_model.predict(input_scaled)
    status_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}

    st.subheader("Prediction Result")
    st.success(f"**{student_name}** is predicted to: **{status_map[prediction[0]]}**")