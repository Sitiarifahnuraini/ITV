import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="ITV Recap", layout="wide")

st.title("🚢 ITV Recap System")

uploaded_files = st.file_uploader(
    "Upload Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

all_data = []

if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            for i in range(len(df)):
                for j in range(len(df.columns)-2):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val = str(df.iloc[i, j+1]).strip()
                    nama = str(df.iloc[i, j+2]).strip()

                    if re.match(r"^\d{3}$", trailer) and \
                       re.match(r"^\d{4}$", id_val) and \
                       nama not in ["nan", ""]:

                        all_data.append({
                            "Shift": sheet_name,
                            "Nama": nama,
                            "ID": id_val,
                            "No Trailer": trailer
                        })

if all_data:
    df_final = pd.DataFrame(all_data)
    st.dataframe(df_final)
