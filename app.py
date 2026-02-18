import streamlit as st
import pandas as pd

# ===================================
# CONFIG
# ===================================
st.set_page_config(page_title="ITV Recap Super Final", layout="wide")

st.title("🚢 Rekap ITV - SUPER FINAL")
st.write("Rekap otomatis (hanya Area Plotting, tanpa mengubah isi data).")

# ===================================
# UPLOAD FILE
# ===================================
uploaded_files = st.file_uploader(
    "Upload file Excel harian",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

# ===================================
# PROCESS FILE
# ===================================
if uploaded_files:

    for file in uploaded_files:

        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            stop_scan = False

            for i in range(len(df) - 1):

                # ===== STOP jika sudah masuk kegiatan lapangan =====
                row_text = " ".join(df.iloc[i].astype(str).tolist()).upper()

                if "KEGIATAN LAPANGAN" in row_text:
                    stop_scan = True
                    break

                for j in range(len(df.columns) - 1):

                    # FORMAT TPS:
                    # ITV di atas
                    # ID + Nama di bawah
                    trailer = str(df.iloc[i, j]).strip()
                    id_val = str(df.iloc[i + 1, j]).strip()
                    nama = str(df.iloc[i + 1, j + 1]).strip()

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

            if stop_scan:
                pass

# ===================================
# OUTPUT
# ===================================
if rekap_data:

    hasil = pd.DataFrame(rekap_data)

    # hapus duplikat
    hasil = hasil.drop_duplicates()

    st.success("✅ Rekap selesai (hanya Area Plotting)")

    st.dataframe(hasil, use_container_width=True)

    csv = hasil.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap CSV",
        csv,
        "rekap_itv_super_final.csv",
        "text/csv"
    )

else:
    st.info("Upload file untuk mulai rekap.")
