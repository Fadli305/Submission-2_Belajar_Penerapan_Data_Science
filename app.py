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

st.title("🎓 Prediksi Dropout Mahasiswa")
st.write("Isi data mahasiswa di bawah ini untuk memprediksi apakah mereka berpotensi Dropout atau Graduate.")

# Buat form input dari semua fitur
input_dict = {}
with st.form("form_prediksi"):
    for feat in feature_order:
        if "grade" in feat or "rate" in feat or "GDP" in feat:
            val = st.number_input(feat, format="%.2f", step=0.1)
        else:
            val = st.number_input(feat, step=1)
        input_dict[feat] = val

    submitted = st.form_submit_button("🔍 Prediksi")

# Proses prediksi jika tombol ditekan
if submitted:
    # Urutkan input sesuai fitur training
    input_array = np.array([[input_dict[feat] for feat in feature_order]])
    input_scaled = scaler.transform(input_array)

    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][pred]
    label = "Dropout" if pred == 1 else "Graduate"

    st.success(f"📢 **Prediksi:** {label}  \n🎯 **Probabilitas:** {prob:.2%}")
