import streamlit as st
import pandas as pd

# ===================================
# CONFIG
# ===================================
st.set_page_config(page_title="ITV Recap Final", layout="wide")

st.title("🚢 Rekap ITV Final")
st.write("Rekap otomatis data ITV (tanpa mengubah isi data).")

# ===================================
# UPLOAD FILE
# ===================================
uploaded_files = st.file_uploader(
    "Upload file Excel harian (bisa banyak)",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

# ===================================
# PROCESS FILE
# ===================================
if uploaded_files:

    for file in uploaded_files:

        # baca semua sheet (shift)
        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            # ===== BAGIAN SCAN (FORMAT TPS) =====
            # ITV ada di baris atas
            # ID + Nama di baris bawah

            for i in range(len(df) - 1):
                for j in range(len(df.columns) - 1):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val = str(df.iloc[i + 1, j]).strip()
                    nama = str(df.iloc[i + 1, j + 1]).strip()

                    # hanya ambil data valid
                    if trailer.isdigit() and len(trailer) == 3 and \
                       id_val.isdigit() and len(id_val) == 4 and \
                       nama not in ["nan", ""]:

                        rekap_data.append({
                            "Tanggal": file.name[:10],
                            "Shift": sheet_name,
                            "No Trailer": trailer,
                            "ID": id_val,
                            "Nama": nama
                        })

# ===================================
# OUTPUT
# ===================================
if rekap_data:

    hasil = pd.DataFrame(rekap_data)

    # hapus data duplikat
    hasil = hasil.drop_duplicates()

    st.success("✅ Rekap selesai (isi data tidak diubah)")

    st.dataframe(hasil, use_container_width=True)

    # DOWNLOAD
    csv = hasil.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap CSV",
        csv,
        "rekap_itv_final.csv",
        "text/csv"
    )

else:
    st.info("Upload file untuk mulai rekap.")
