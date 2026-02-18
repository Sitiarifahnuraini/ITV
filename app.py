import streamlit as st
import pandas as pd

st.set_page_config(page_title="ITV Recap Akurat", layout="wide")

st.title("🚢 Rekap ITV (Akurat Semua Operator)")
st.write("Rekap otomatis sesuai struktur asli file.")

uploaded_files = st.file_uploader(
    "Upload file Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            # Scan dengan pola 3 baris vertikal
            for i in range(len(df) - 2):
                for j in range(len(df.columns)):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val  = str(df.iloc[i+1, j]).strip()
                    nama    = str(df.iloc[i+2, j]).strip()

                    if trailer.isdigit() and len(trailer) == 3 and \
                       id_val.isdigit() and len(id_val) == 4 and \
                       nama not
