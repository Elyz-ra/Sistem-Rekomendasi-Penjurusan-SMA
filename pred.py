# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("🎓 Sistem Rekomendasi Penjurusan SMA")

# Load model dan scaler
model = joblib.load("random_forest_model.pkl")  # simpan dari notebook
scaler = joblib.load("scaler.pkl")              # simpan dari notebook
label_encoder = joblib.load("label_encoder.pkl")  # simpan dari notebook

# Input manual atau upload
option = st.radio("Pilih metode input data:", ["Input Manual", "Upload File Excel"])

if option == "Input Manual":
    st.subheader("Masukkan Nilai Semester (1-6) untuk Setiap Mata Pelajaran")
    pelajaran = ['Agama', 'PKN', 'Indo', 'Mate', 'IPA', 'IPS', 'Inggris', 'Senbud', 'PJOK', 'Prakarya', 'B_Daerah']
    input_data = {}

    for pel in pelajaran:
        for sem in range(1, 7):
            key = f"{pel}{sem}"
            input_data[key] = st.number_input(f"{pel} Semester {sem}", min_value=0, max_value=100)

    # Convert ke DataFrame dan scaling
    if st.button("Prediksi Jurusan"):
        df = pd.DataFrame([input_data])
        df_scaled = scaler.transform(df)
        pred = model.predict(df_scaled)
        pred_label = label_encoder.inverse_transform(pred)[0]
        st.success(f"✅ Jurusan yang Direkomendasikan: **{pred_label}**")

elif option == "Upload File Excel":
    st.subheader("Unggah File Excel dengan Format Kolom yang Sesuai")
    uploaded_file = st.file_uploader("Pilih file Excel...", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        df_scaled = scaler.transform(df)
        predictions = model.predict(df_scaled)
        pred_labels = label_encoder.inverse_transform(predictions)

        df["Rekomendasi Jurusan"] = pred_labels
        st.dataframe(df)

        st.download_button("📥 Unduh Hasil Prediksi", data=df.to_csv(index=False), file_name="hasil_prediksi.csv")

