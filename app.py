import streamlit as st
import pandas as pd
import re

# ===============================
# CONFIG PAGE
# ===============================
st.set_page_config(page_title="ITV Master Recap", layout="wide")

st.title("🚢 ITV Daily Recap System")
st.write("Upload file Excel harian (berisi 3 shift).")

# ===============================
# UPLOAD FILE
# ===============================
uploaded_files = st.file_uploader(
    "Upload file Excel (bisa banyak sekaligus)",
    type=["xlsx"],
    accept_multiple_files=True
)

all_data = []

# ===============================
# PROCESS FILE
# ===============================
if uploaded_files:

    for file in uploaded_files:

        # baca semua sheet (tiap shift biasanya beda sheet)
        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            # scan seluruh cell
            for i in range(len(df)):
                for j in range(len(df.columns)-2):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val  = str(df.iloc[i, j+1]).strip()
                    nama    = str(df.iloc[i, j+2]).strip()

                    # pola data:
                    # Trailer = 3 digit
                    # ID = 4 digit
                      if re.ma :
                                ^
IndentationError: expected an indented block after 'if' statement on line 47
