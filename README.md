# Analisis Statistik Populasi Penduduk Sulawesi Tengah Menggunakan Python

Repositori ini berisi implementasi proyek analisis statistik deskriptif terhadap data populasi penduduk Provinsi Sulawesi Tengah menggunakan bahasa pemrograman Python. Proyek ini dikembangkan untuk mengeksplorasi karakteristik demografi wilayah berdasarkan jumlah penduduk, kepadatan penduduk, laju pertumbuhan penduduk, dan distribusi populasi antar kabupaten/kota.

Proyek ini disusun sebagai bagian dari pemenuhan tugas mata kuliah **Statistik dan Probabilitas**.

---

## 📌 Latar Belakang Studi

Data kependudukan merupakan salah satu indikator penting dalam perencanaan pembangunan daerah. Informasi mengenai jumlah penduduk, kepadatan penduduk, serta laju pertumbuhan penduduk dapat digunakan sebagai dasar dalam pengambilan kebijakan di bidang ekonomi, pendidikan, kesehatan, dan infrastruktur.

Provinsi Sulawesi Tengah memiliki karakteristik demografi yang beragam pada setiap kabupaten dan kota. Oleh karena itu, diperlukan analisis statistik untuk memahami pola distribusi penduduk dan mengidentifikasi wilayah dengan tingkat populasi maupun kepadatan tertinggi dan terendah.

---

## 📊 Sumber Data

Dataset yang digunakan dalam proyek ini berisi data statistik kependudukan Kabupaten/Kota di Provinsi Sulawesi Tengah.

Variabel yang dianalisis meliputi:

* **Tahun**
* **Kabupaten/Kota**
* **Populasi (Ribu Jiwa)**
* **Laju Pertumbuhan Penduduk (%)**
* **Persentase terhadap Total Populasi (%)**
* **Kepadatan Penduduk (Jiwa/Km²)**
* **Rasio Jenis Kelamin**

---

## ⚙️ Alur Analisis Data

Sistem analisis dalam repositori ini dibangun melalui beberapa tahapan pengolahan data sebagai berikut:

### 1. Import dan Pembacaan Dataset

Dataset dibaca menggunakan library Pandas untuk memperoleh struktur data yang siap dianalisis.

### 2. Eksplorasi Data

Melakukan pemeriksaan informasi dataset meliputi:

* Jumlah data
* Tipe data
* Kelengkapan data
* Statistik deskriptif awal

### 3. Analisis Statistik Deskriptif

Menghitung berbagai ukuran statistik seperti:

* Rata-rata (Mean)
* Nilai Minimum
* Nilai Maksimum
* Standar Deviasi
* Kuartil Data

### 4. Identifikasi Karakteristik Populasi

Melakukan pencarian:

* Kabupaten/Kota dengan populasi terbesar
* Kabupaten/Kota dengan populasi terkecil
* Tingkat kepadatan penduduk tertinggi
* Tingkat kepadatan penduduk terendah

### 5. Visualisasi Data

Data divisualisasikan menggunakan Matplotlib dan Seaborn dalam bentuk:

* Grafik Populasi Penduduk
* Grafik Kepadatan Penduduk
* Grafik Laju Pertumbuhan Penduduk

### 6. Interpretasi Hasil

Hasil analisis digunakan untuk memberikan gambaran umum mengenai kondisi demografi Provinsi Sulawesi Tengah berdasarkan data yang tersedia.

---

## 🛠️ Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn

---

## 📈 Output Program

Program menghasilkan beberapa visualisasi dan informasi statistik :

* Statistik Deskriptif Dataset
* Grafik Populasi Penduduk Kabupaten/Kota
* Grafik Kepadatan Penduduk
* Grafik Laju Pertumbuhan Penduduk
* Ringkasan Hasil Analisis

File output yang dihasilkan:

* `grafik_populasi.png`
* `grafik_kepadatan.png`
* `grafik_pertumbuhan.png`
Proyek ini dibuat sebagai implementasi analisis statistik deskriptif menggunakan Python pada data populasi penduduk Provinsi Sulawesi Tengah untuk mendukung pembelajaran mata kuliah Statistik dan Probabilitas.
