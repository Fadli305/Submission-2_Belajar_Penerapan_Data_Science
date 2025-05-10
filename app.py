import streamlit as st
import joblib
import json
import numpy as np


# Load model & scaler
model = joblib.load('./model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')
with open("model/features.json") as f:
    feature_order = json.load(f)
  
st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="centered")

st.title("\U0001F393 Prediksi Dropout Mahasiswa")
st.write("Isi data mahasiswa di bawah ini untuk memprediksi apakah mereka berpotensi Dropout atau Graduate.")

# --- FORM INPUT MANUSIAWI ---
with st.form("form_prediksi"):
    st.subheader("Data Akademik dan Sosial Mahasiswa")

    # Beberapa input dipilih sebagai representatif, sisanya default 0
    marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            1: "1 – Single", 2: "2 – Married", 3: "3 – Widower",
            4: "4 – Divorced", 5: "5 – Facto Union", 6: "6 – Legally Separated"
        }[x])

    application_mode = st.selectbox("Jalur Masuk", [1, 2, 5, 7, 10, 15, 39, 42, 51, 57],
        format_func=lambda x: {
            1: "1 – 1st Phase (General)", 2: "2 – Ordinance 612/93",
            5: "5 – Special (Azores)", 7: "7 – Lulusan PT Lain", 10: "10 – Ordinance 854-B/99",
            15: "15 – International Student", 39: "39 – Usia >23 tahun",
            42: "42 – Transfer", 51: "51 – Change of Institution", 57: "57 – Int'l Transfer"
        }.get(x, f"Mode {x}"))

    admission_grade = st.slider("Nilai Ujian Masuk (0-200)", 0, 200, 130)
    previous_qualification_grade = st.slider("Nilai Pendidikan Terakhir (0-200)", 0, 200, 120)
    age = st.slider("Umur Saat Mendaftar", 17, 60, 20)

    tuition_status = st.radio("Status Pembayaran Kuliah", ["Lancar", "Tertunggak"])
    tuition_val = 1 if tuition_status == "Lancar" else 0

    curr_1st_grade = st.slider("Nilai Rata-rata Semester 1 (0-20)", 0.0, 20.0, 12.0)
    curr_2nd_grade = st.slider("Nilai Rata-rata Semester 2 (0-20)", 0.0, 20.0, 12.0)

    approved_1st = st.number_input("Jumlah Matkul Lulus Semester 1", min_value=0, step=1)
    approved_2nd = st.number_input("Jumlah Matkul Lulus Semester 2", min_value=0, step=1)

    submitted = st.form_submit_button("🔍 Prediksi")

# --- PREDIKSI ---
if submitted:
    # Buat template input default
    input_dict = {feat: 0 for feat in feature_order}

    # Masukkan nilai dari input pengguna
    input_dict.update({
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Admission_grade': admission_grade,
        'Previous_qualification_grade': previous_qualification_grade,
        'Age_at_enrollment': age,
        'Tuition_fees_up_to_date': tuition_val,
        'Curricular_units_1st_sem_grade': curr_1st_grade,
        'Curricular_units_2nd_sem_grade': curr_2nd_grade,
        'Curricular_units_1st_sem_approved': approved_1st,
        'Curricular_units_2nd_sem_approved': approved_2nd,
    })

    # Susun array input sesuai urutan
    input_array = np.array([[input_dict[feat] for feat in feature_order]])
    input_scaled = scaler.transform(input_array)

    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][pred]
    label = "Dropout" if pred == 1 else "Graduate"

    st.success(f"📢 Prediksi: **{label}**  \n🎯 Probabilitas: **{prob:.2%}**")
