# Sistem-Rekomendasi-Penjurusan-SMA

## Business Understanding
Proses penjurusan siswa SMA (IPA, IPS, Bahasa) seringkali tidak mempertimbangkan data akademik maupun karakteristik pribadi siswa secara menyeluruh. Hal ini menyebabkan ketidaksesuaian jurusan, rendahnya motivasi belajar, hingga pengambilan keputusan karier yang kurang tepat. Diperlukan sistem yang dapat membantu sekolah dan siswa mengambil keputusan penjurusan secara objektif dan berbasis data.

## Permasalahan Bisnis

1. Penjurusan masih dilakukan secara manual dan subjektif.

2. Banyak siswa memilih jurusan karena tekanan eksternal (orang tua/tren), bukan berdasarkan potensi dan minat.

3. Sekolah tidak memiliki sistem berbasis data untuk membantu proses bimbingan penjurusan.

4. Belum tersedia alat yang mampu memberikan prediksi jurusan secara otomatis dan transparan.

## Cakupan Proyek

1. Merancang dan melatih model machine learning (Random Forest) untuk prediksi jurusan siswa.

2. Menggunakan data nilai, kehadiran, dan aktivitas siswa SMP sebagai input model.

3. Membangun prototipe dashboard sederhana untuk menampilkan hasil rekomendasi.

4. Mengintegrasikan sistem dengan data sekolah agar dapat digunakan guru BK secara berkelanjutan.

## Persiapan

### Sumber data
Data diperoleh dari SMPN 2 Wungu, meliputi nilai akademik, kehadiran, dan aktivitas non-akademik siswa kelas 7–9 pada tahun ajaran 2021–2023. Data dapat diakses pada link berikut:
	https://docs.google.com/spreadsheets/d/1WHtDZErQARYJ7pytXsQg26UwzZKcV1pD7EbGMX5s7YE/edit?usp=sharing


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

**Cara Menjalankan Dashboard**

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
