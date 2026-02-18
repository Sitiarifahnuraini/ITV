import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekap ITV Akurat", layout="wide")

st.title("🚢 Rekap ITV (Grid Detector)")
st.write("Rekap otomatis sesuai layout manning & deployment.")

uploaded_files = st.file_uploader(
    "Upload file Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

# ==============================
# FUNCTION CEK ANGKA
# ==============================
def clean_num(val):
    val = str(val).replace(".0", "").strip()
    return val


# ==============================
# PROCESS FILE
# ==============================
if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            rows, cols = df.shape

            # SCAN SEMUA GRID
            for i in range(rows - 1):
                for j in range(cols - 1):

                    trailer = clean_num(df.iloc[i, j])
                    id_val  = clean_num(df.iloc[i+1, j])
                    nama    = str(df.iloc[i+1, j+1]).strip()

                    # RULE VALIDASI
                    if trailer.isdigit() and len(trailer) == 3 and \
                       id_val.isdigit() and len(id_val) == 4 and \
                       nama not in ["nan", ""] and \
                       not nama.isdigit():

                        rekap_data.append({
                            "Tanggal": file.name[:10],
                            "Shift": sheet_name,
                            "No Trailer": trailer,
                            "ID": id_val,
                            "Nama": nama
                        })

# ==============================
# OUTPUT
# ==============================
if len(rekap_data) > 0:

    df_rekap = pd.DataFrame(rekap_data)

    # buang duplikat
    df_rekap = df_rekap.drop_duplicates()

    st.success(f"✅ Total operator terdeteksi: {len(df_rekap)}")

    st.dataframe(df_rekap, use_container_width=True)

    # DOWNLOAD
    csv = df_rekap.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap CSV",
        csv,
        "rekap_itv_final.csv",
        "text/csv"
    )

else:
    st.warning("⚠️ Tidak ada data ITV terdeteksi.")
