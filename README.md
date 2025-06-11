# Sistem-Rekomendasi-Penjurusan-SMA

## Menjalankan Sistem Machine Learning

Dashboard rekomendasi penjurusan calon siswa SMA telah dibuat dengan deployment melalui Streamlit. Berikut adalah cara mengakses dashboard tersebut:

### Menjalankan dashboard melalui tautan Streamlit Cloud
Buka tautan berikut dengan browser Anda:

https://predsiswa.streamlit.app/

### Menjalankan dashboard secara lokal

**Struktur Folder**

Pastikan file berikut berada dalam satu folder:

```
├── pred.py
├── random_forest_model.pkl
├── scaler.pkl
├── README.md
├── requirements.txt
├── (venv/)
```

**Cara Menjalankan Aplikasi**

1. Aktifkan virtual environment:

```bash
source venv/bin/activate   # Untuk Mac/Linux
venv\Scripts\activate      # Untuk Windows
```

2. Jalankan Streamlit melalui terminal

```bash
streamlit run pred.py
```

Jika berhasil, Streamlit akan membuka browser secara otomatis atau menampilkan URL lokal seperti:

```
  Local URL: http://localhost:8501
  Network URL: http://192.168.68.111:8501
```
