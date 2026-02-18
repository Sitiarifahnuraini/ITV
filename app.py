import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekap ITV", layout="wide")

st.title("🚢 Rekap ITV (Smart Detector)")

uploaded_files = st.file_uploader(
    "Upload file Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

def clean(v):
    return str(v).replace(".0", "").strip()

if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            rows, cols = df.shape

            for i in range(rows):
                for j in range(cols):

                    trailer = clean(df.iloc[i, j])

                    # cari ITV (3 digit)
                    if trailer.isdigit() and len(trailer) == 3:

                        # cek kemungkinan posisi ID + Nama di bawah
                        if i+1 < rows and j+1 < cols:

                            id_val = clean(df.iloc[i+1, j])
                            nama = clean(df.iloc[i+1, j+1])

                            if id_val.isdigit() and len(id_val) == 4 and \
