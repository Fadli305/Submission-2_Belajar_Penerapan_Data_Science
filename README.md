# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan fiktif yang menghadapi masalah serius terkait jumlah mahasiswa yang tidak menyelesaikan studi alias dropout. Tingginya angka dropout berdampak buruk pada reputasi institusi, efisiensi operasional, dan efektivitas pendidikan.

### Permasalahan Bisnis
- Tingginya tingkat mahasiswa yang dropout sebelum menyelesaikan studi
- Apa saja Faktor-faktor yang dapat memperngaruhi keputusan siswa untuk melakukan dropout dari kampus?

### Cakupan Proyek
- Melakukan eksplorasi dan analisis terhadap data akademik dan administratif mahasiswa
- Membangun model machine learning untuk prediksi dropout
- Membuat business dashboard untuk monitoring performa


### Persiapan

Sumber data: Dataset performa mahasiswa yang mencakup data akademik, sosial, dan administratif dari Jaya Jaya Institut. [link dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```bash
# Ekstrak file ZIP hasil submission
# Masuk ke dalam folder proyek
cd submission


# Instal seluruh dependency yang dibutuhkan
pip install -r requirements.txt

```

## Business Dashboard
Dashboard dibuat menggunakan Looker Studio untuk memvisualisasikan performa akademik dan tren dropout mahasiswa. Visualisasi disusun ke dalam beberapa bagian utama:

- **Ringkasan**: Menampilkan metrik utama berupa total mahasiswa, jumlah mahasiswa lulus, dan jumlah dropout dalam bentuk scorecard.
- **Distribusi Status Mahasiswa**: Pie chart untuk melihat proporsi Graduate, Dropout, dan Enrolled.
- **Performa Akademik**: Menampilkan rata-rata nilai semester 1 dan 2 serta jumlah matkul yang diselesaikan sebagai indikator kinerja belajar mahasiswa.
- **Faktor Administratif**: Menyediakan visualisasi hubungan antara status pembayaran kuliah, beasiswa, dan gender terhadap peluang terjadinya dropout.
- **Filter Interaktif**: Terdapat panel filter untuk Course_name, Status, Tuition_fees_up_to_date yang memberikan pengguna untuk menyaring data sesuai kebutuhan.

📎 Link dashboard: [klik disini](https://lookerstudio.google.com/reporting/544b7c09-2dad-4c93-811a-5f0892aa0254)


## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dropout dibangun menggunakan Streamlit dan dapat dijalankan secara lokal maupun online.

### Cara Menjalankan Lokal:
Pastikan Anda telah mengikuti tahapan pada bagian *Setup Environment*. Jika sudah, jalankan perintah berikut di terminal atau command prompt:
```bash
streamlit run app.py
```

📎 Akses online: [klik disini](https://submission-2belajarpenerapandatascience-eveciat9whaspwdb8vda5s.streamlit.app/)


## Conclusion
Tingkat dropout yang tinggi di Jaya Jaya Institut bukan hanya mencerminkan tantangan akademik, tetapi juga tantangan administratif dan sosial yang perlu segera diatasi. Berdasarkan hasil analisis dan pemodelan machine learning yang dilakukan, terdapat pola-pola yang jelas mengenai mahasiswa berisiko tinggi untuk tidak menyelesaikan studinya. Mahasiswa dengan nilai rendah, matkul yang tidak diselesaikan, serta masalah administratif seperti keterlambatan pembayaran terbukti lebih rentan terhadap dropoutnya para mahasiswa.

Model Random Forest yang dibangun dalam proyek ini dapat menjadi pilihan yang optimal dengan hasil evaluasi mencapai akurasi 93% dan f1-score sebesar 91% pada kelas dropout. Evaluasi dilakukan menggunakan validasi silang dan optimasi hyperparameter melalui GridSearchCV. Model ini dapat mengidentifikasi sejumlah fitur penting seperti nilai semester, jumlah matkul lulus, serta status pembayaran dan beasiswa sebagai indikator terjadinya dropout.

Dengan implementasi sistem prediksi berbasis Streamlit serta dashboard visual di Looker Studio, pihak kampus kini memiliki alat yang praktis dan efisien untuk mendeteksi mahasiswa yang memiliki resiko dropout sejak dini. Harapannya dengan diterapkan solusi ini, pihak institusi dapat mengidentifikasi mahasiswa berisiko sejak dini dan mengambil langkah intervensi yang tepat.


### Rekomendasi Action Items
- **Intervensi Dini**: Terapkan program mentoring untuk mahasiswa dengan nilai semester 1 & 2 yang rendah atau jumlah matkul lulus minim
- **Pemantauan Administratif**: Prioritaskan pemantauan pada mahasiswa dengan status pembayaran tertunggak dan bukan penerima beasiswa
- **Dukungan Psikologis dan Akademik**: Arahkan hasil model ke tim konseling untuk dilakukan tindakan lebih lanjut
- **Integrasi Sistem**: Kembangkan sistem ini untuk terhubung langsung dengan data real-time akademik kampus
- **Pembaruan Model Secara Berkala**: Jadwalkan retraining model setiap semester untuk menjaga akurasi terhadap dinamika mahasiswa.
