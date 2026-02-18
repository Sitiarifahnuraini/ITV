import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekap ITV", layout="wide")

st.title("🚢 Rekap ITV")
st.write("Rekap otomatis dari file manning.")

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

            for i in range(len(df)-1):
                for j in range(len(df.columns)-1):

                    # convert ke string & hilangkan .0
                    trailer = str(df.iloc[i, j]).replace(".0","").strip()
                    id_val  = str(df.iloc[i+1, j]).replace(".0","").strip()
                    nama    = str(df.iloc[i+1, j+1]).strip()

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

# OUTPUT
if len(rekap_data) > 0:

    df_rekap = pd.DataFrame(rekap_data).drop_duplicates()

    st.success(f"✅ Total ditemukan: {len(df_rekap)} operator")

    st.dataframe(df_rekap, use_container_width=True)

    csv = df_rekap.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap CSV",
        csv,
        "rekap_itv.csv",
        "text/csv"
    )

else:
    st.warning("⚠️ Tidak ada data yang cocok terdeteksi.")
