import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekap ITV", layout="wide")

st.title("🚢 Rekap ITV (Area Plotting)")
st.write("Rekap otomatis tanpa mengubah isi data.")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:

    # Baca file
    df = pd.read_excel(uploaded_file)

    # Normalisasi nama kolom (hapus spasi)
    df.columns = df.columns.str.strip()

    # Pastikan kolom yang dibutuhkan ada
    required_columns = ["Tanggal", "Shift", "Area", "Nama", "ID", "No Trailer"]
    
    for col in required_columns:
        if col not in df.columns:
            st.error(f"Kolom '{col}' tidak ditemukan di file.")
            st.stop()

    # 🔎 FILTER SESUAI KEBUTUHAN
    df_filter_
