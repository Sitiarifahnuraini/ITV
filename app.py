import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="ITV Recap System", layout="wide")

st.title("🚢 Rekap ITV - Area Plotting Lapangan")

uploaded_files = st.file_uploader(
    "Upload file Excel (harian / 3 shift)",
    type=["xlsx"],
    accept_multiple_files=True
)

all_data = []

# ===================================
# PROCESS FILE
# ===================================
if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            for i in range(len(df)):
                for j in range(len(df.columns)-2):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val  = str(df.iloc[i, j+1]).strip()
                    nama    = str(df.iloc[i, j+2]).strip()

                    # ===============================
                    # FILTER KHUSUS AREA PLOTTING LAPANGAN
                    # ===============================
                    if re.match(r"^\d{3}$", trailer) and \
                       re.match(r"^\d{4}$", id_val) and \
                       nama not in ["nan", ""]:

                        all_data.append({
                            "Tanggal": file.name[:10],
                            "Shift": sheet_name,
                            "Nama": nama,
                            "ID": id_val,
                            "No Trailer": trailer
                        })

# ===================================
# OUTPUT
# ===================================
if all_data:

    master_df = pd.DataFrame(all_data)

    # hapus duplikat
    master_df = master_df.drop_duplicates()

    st.success("✅ Rekap hanya operator yang mendapat ITV")

    st.dataframe(master_df, use_container_width=True)

    csv = master_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap",
        csv,
        "rekap_itv.csv",
        "text/csv"
    )

else:
    st.info("Upload file untuk mulai rekap.")
