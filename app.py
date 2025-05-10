import streamlit as st
import joblib
import numpy as np

# Load model & scaler
model = joblib.load('./model/best_model.pkl')
scaler = joblib.load('.model/scaler.pkl')

st.title("🎓 Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

# Form input data
st.header("Masukkan Data Mahasiswa")

# Contoh input
age = st.slider("Umur saat mendaftar", 17, 60, 20)
admission_grade = st.slider("Nilai Ujian Masuk", 0, 200, 130)
curr_1st_grade = st.slider("Nilai Semester 1", 0.0, 20.0, 12.0)
curr_2nd_grade = st.slider("Nilai Semester 2", 0.0, 20.0, 12.0)
approved_1st = st.number_input("Matkul Lulus Semester 1", min_value=0)
approved_2nd = st.number_input("Matkul Lulus Semester 2", min_value=0)
tuition_ok = st.selectbox("Status Pembayaran Kuliah", ['Lancar', 'Tertunggak'])

# Konversi input ke bentuk numerik
tuition_val = 1 if tuition_ok == 'Lancar' else 0

# Gabungkan jadi array
input_data = np.array([[approved_2nd, approved_1st, curr_2nd_grade, curr_1st_grade,
                        tuition_val, age, admission_grade]])

# Scaling
input_scaled = scaler.transform(input_data)

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][prediction]

    status = "Dropout" if prediction == 1 else "Graduate"
    st.success(f"🚩 Prediksi: **{status}** (Probabilitas: {proba:.2f})")
