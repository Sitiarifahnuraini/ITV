import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Rekap ITV", layout="wide")

st.title("🚢 Rekap ITV (Tanpa Mengubah Isi)")

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

            # scan seluruh isi sheet
            for i in range(len(df)):
                for j in range(len(df.columns)-2):

                    val1 = df.iloc[i, j]
                    val2 = df.iloc[i, j+1]
                    val3 = df.iloc[i, j+2]

                    # hanya ambil yang punya trailer + id
                    if str(val1).isdigit() and len(str(val1)) == 3 and \
                       str(val2).isdigit() and len(str(val2)) == 4 and \
                       pd.notna(val3):

                        rekap_data.append({
                            "Tanggal": file.name[:10],
                            "Shift": sheet_name,
                            "No Trailer": val1,
                            "ID": val2,
                            "Nama": val3
                        })

if rekap_data:

    hasil = pd.DataFrame(rekap_data)

    st.success("✅ Rekap selesai (isi data tidak diubah)")

    st.dataframe(hasil, use_container_width=True)

    csv = hasil.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap",
        csv,
        "rekap_itv.csv",
        "text/csv"
    )
else:
    st.info("Upload file untuk mulai rekap.")
