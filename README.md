# ITV Daily Recap System

Aplikasi Streamlit untuk merekap data ITV harian (3 shift).

## Fitur
- Upload multiple Excel files
- Otomatis scan data horizontal
- Deteksi:
  - No Trailer (3 digit)
  - ID (4 digit)
  - Nama
- Rekap master otomatis
- Download CSV

## Jalankan
```bash
pip install -r requirements.txt
streamlit run app.py
