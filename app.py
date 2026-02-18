import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekap ITV", layout="wide")

st.title("🚢 Rekap ITV (Format Manning)")
st.write("Rekap otomatis tanpa mengubah isi data.")

uploaded_files = st.file_uploader(
    "Upload file Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

rekap_data = []

if uploaded_files:

    for file in uploaded_files:

        # baca semua sheet tanpa header
        sheets = pd.read_excel(file, sheet_name=None, header=None)

        for sheet_name, df in sheets.items():

            # scan pola vertikal:
            # baris atas = ITV
            # bawahnya = ID
            # bawah lagi = Nama
            for i in range(len(df)-2):
                for j in range(len(df.columns)):

                    trailer = str(df.iloc[i, j]).strip()
                    id_val  = str(df.iloc[i+1, j]).strip()
                    nama    = str(df.iloc[i+2, j]).strip()

                    if trailer.isdigit() and len(trailer) == 3 and \
                       id_val.isdigit() and len(id_val) == 4 and \
                       nama not in ["nan", ""] and \
                       not nama.isdigit():

                        rekap_data.append({
                            "Tanggal": file.name[:10],   # ambil dari nama file
                            "Shift": sheet_name,
                            "Nama": nama,
                            "ID": id_val,
                            "No Trailer": trailer
                        })

if rekap_data:

    df_rekap = pd.DataFrame(rekap_data).drop_duplicates()

    st.success(f"✅ Rekap selesai - {len(df_rekap)} operator")

    st.dataframe(df_rekap, use_container_width=True)

    csv = df_rekap.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Rekap CSV",
        csv,
        "rekap_itv.csv",
        "text/csv"
    )

else:
    st.info("Upload file untuk mulai rekap.")
