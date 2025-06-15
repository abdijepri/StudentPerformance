# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikan atau mengalami dropout.

Masalah ini berdampak buruk tidak hanya pada citra institusi, tetapi juga pada efektivitas proses belajar-mengajar dan keberlanjutan operasional. Untuk itu, pihak institusi ingin mengidentifikasi lebih awal siswa-siswa yang berpotensi dropout agar dapat diberikan intervensi dan bimbingan yang tepat.

Dengan menyediakan data yang mencakup informasi demografis, akademik, dan administratif siswa, Jaya Jaya Institut berharap dapat memanfaatkan analisis data untuk memahami pola dan faktor-faktor yang memengaruhi keberhasilan akademik siswa. Hasil dari analisis ini akan menjadi dasar pengambilan keputusan yang berbasis data, seperti strategi pencegahan dropout, peningkatan tingkat kelulusan, dan pengembangan program dukungan bagi siswa yang berisiko untuk dropout.

### Permasalahan Bisnis
1. Distribusi dan Tren Status Mahasiswa
   * Bagaimana distribusi status akhir mahasiswa (Dropout, Graduate, Enrolled) di Jaya Jaya Institut?
2. Faktor Demografis
   * Apakah status mahasiswa internasional (International) atau pengungsi (Displaced) memiliki dampak terhadap keberhasilan studi?
3. Latar Belakang Keluarga
   * Apakah tingkat pendidikan dan pekerjaan orang tua (Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation) berkorelasi dengan status akhir mahasiswa?
4. Faktor Akademik
   * Bagaimana dampak beasiswa (Scholarship_holder) terhadap kelulusan?
5. Faktor Keuangan dan Administratif
   * Apakah mahasiswa yang memiliki tunggakan (Debtor) atau tidak membayar biaya kuliah tepat waktu (Tuition_fees_up_to_date) lebih berisiko dropout?

### Cakupan Proyek
1. Analisis Distribusi dan Tren Status Mahasiswa
    * Membuat visualisasi distribusi status akhir mahasiswa (Dropout, Graduate, Enrolled) untuk memahami proporsi dari masing-masing kategori.
    * Menganalisis pola waktu dan semester dalam kaitannya dengan mahasiswa yang dropout lebih awal selama masa studi.

2. Analisis Faktor Demografis
    * Menguji hubungan antara jenis kelamin (Gender), usia saat mendaftar (Age_at_enrollment), dan status pernikahan (Marital_status) dengan status akhir mahasiswa.
    * Menganalisis pengaruh status mahasiswa internasional (International) dan status sebagai pengungsi (Displaced) terhadap kemungkinan dropout atau kelulusan.

3. Analisis Latar Belakang Keluarga
    * Menganalisis korelasi antara pendidikan orang tua (Mothers_qualification, Fathers_qualification) serta pekerjaan orang tua (Mothers_occupation, Fathers_occupation) dengan hasil akhir studi mahasiswa.
    * Menilai apakah latar belakang keluarga dapat menjadi indikator risiko dropout.

4. Analisis Faktor Akademik
    * Mengevaluasi pengaruh kepemilikan beasiswa (Scholarship_holder) terhadap tingkat kelulusan mahasiswa.
    * Menganalisis peran nilai rata-rata akademik dari semester 1 dan 2 (Curricular_units_1st_sem_grade, Curricular_units_2nd_sem_grade) terhadap status akhir.
    * Mempelajari hubungan jumlah mata kuliah yang diambil, dinilai, dan disetujui dengan keberhasilan studi.

5. Analisis Faktor Keuangan dan Administratif
    * Mengkaji apakah mahasiswa yang memiliki tunggakan pembayaran (Debtor) dan yang tidak membayar tepat waktu (Tuition_fees_up_to_date) memiliki risiko dropout yang lebih tinggi.
    * Menilai pengaruh kondisi ekonomi makro seperti tingkat pengangguran (Unemployment_rate), inflasi (Inflation_rate), dan PDB (GDP) terhadap kelulusan atau dropout mahasiswa.

### Persiapan

Data source: <a href="https://doi.org/10.24432/C5MC89">link data</a>

Setup environment:
```bash
conda create -n myenv
conda activate myenv
pip install -r requirements.txt
```

## Business Dashboard

![Image](https://github.com/user-attachments/assets/758cbcca-a181-4d5f-8cc4-f6dc81618a3e)

Akses menuju Dashboard : [Link Dashboard](https://lookerstudio.google.com/reporting/9c498901-2731-42c3-971d-728486e95c2c)

**Tujuan Dashboard**

Dashboard ini dirancang untuk membantu manajemen Jaya Jaya Institut dalam memahami status akhir mahasiswa yang terdiri dari kategori graduate, dropout, dan enrolled. Melalui visualisasi data, manajemen dapat mengidentifikasi pola dan tren tertentu, terutama yang berkaitan dengan mahasiswa yang berisiko tinggi mengalami dropout. Selain itu, dashboard ini juga berfungsi untuk mengevaluasi berbagai faktor akademik, demografis, dan administratif yang dapat memengaruhi performa mahasiswa. Dengan informasi yang tersedia, pengambilan keputusan berbasis data dapat dilakukan secara lebih cepat dan akurat guna meningkatkan tingkat kelulusan serta menurunkan angka putus studi di institusi.

**Status Mahasiswa**

Tiga diagram lingkaran memberikan gambaran umum tentang status akhir mahasiswa, status beasiswa, dan status tunggakan. Sebanyak 49.9% mahasiswa berhasil lulus, 32.1% mengalami dropout, dan 17.9% masih aktif terdaftar. Dari sisi beasiswa, hanya 18.2% mahasiswa yang menerima beasiswa, sementara 81.9% lainnya tidak. Terkait keuangan, 9.6% mahasiswa tercatat memiliki tunggakan, sedangkan 90.4% sisanya tidak memiliki masalah pembayaran.

**Status Akademik Mahasiswa**

Dalam hal status beasiswa, terlihat bahwa mahasiswa penerima beasiswa memiliki tingkat kelulusan yang lebih tinggi dibandingkan mereka yang tidak menerima beasiswa. Ini menunjukkan bahwa dukungan finansial berkontribusi positif terhadap keberhasilan akademik. Selain itu, nilai admission mahasiswa juga menunjukkan pengaruh signifikan: mahasiswa dengan nilai masuk rendah (kategori Low dan Very Low) lebih rentan mengalami dropout. Sebaliknya, mahasiswa dengan nilai admission yang lebih tinggi cenderung memiliki tingkat kelulusan yang lebih baik, menandakan bahwa kesiapan awal akademik berpengaruh terhadap keberhasilan akhir.

**Status Demografi Mahasiswa**

Pada kategori mahasiswa internasional, data menunjukkan bahwa mahasiswa non-internasional mendominasi jumlah lulusan dan mahasiswa aktif, sedangkan mahasiswa internasional jumlahnya lebih sedikit dan memiliki tren dropout yang tetap perlu diperhatikan. Untuk mahasiswa dengan status displaced (imigran), ditemukan bahwa tingkat kelulusan mereka relatif tinggi, meskipun tetap terdapat proporsi dropout yang signifikan. Hal ini mengindikasikan bahwa latar belakang imigrasi tidak selalu menjadi penghalang kesuksesan akademik, namun tetap memerlukan perhatian khusus.

**SFaktor Keuangan dan Administratif**

Faktor keuangan memainkan peran penting dalam kelulusan mahasiswa. Data menunjukkan bahwa mahasiswa dengan tunggakan (debtor) memiliki risiko dropout yang jauh lebih tinggi dibandingkan mereka yang tidak memiliki tunggakan. Selain itu, mahasiswa yang membayar biaya kuliah tepat waktu memiliki tingkat kelulusan yang jauh lebih tinggi dibandingkan mereka yang menunggak atau tidak membayar tepat waktu. Hal ini menegaskan bahwa keteraturan dalam pembayaran menjadi indikator penting bagi keberhasilan studi mahasiswa.

## Menjalankan Sistem Machine Learning
![Image](https://github.com/user-attachments/assets/1db28260-2761-4294-962e-3aa05fefe018)

```
streamlit run app.py
```

[Link Akses Streamlit](https://studentperformance-abdijepri.streamlit.app/)

Catatan: sebelum menjalankan perintah di atas, Anda harus menyelesaikan terlebih dahulu pengaturan lingkungan (environment setup).
## Conclusion
Proyek ini berhasil menghasilkan dashboard analitik interaktif yang dapat digunakan oleh manajemen Jaya Jaya Institut untuk memahami performa akademik mahasiswa secara menyeluruh dan berbasis data. Dengan memanfaatkan data historis dari berbagai aspek — akademik, demografis, hingga administratif — dashboard ini memberikan wawasan penting yang dapat digunakan untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap risiko dropout mahasiswa.

Beberapa kesimpulan utama yang dapat diambil dari analisis:

* Dropout menjadi isu signifikan, dengan lebih dari 30% mahasiswa tidak menyelesaikan pendidikan mereka. Ini menunjukkan perlunya strategi intervensi dini yang lebih efektif.
* Faktor akademik seperti nilai admission dan beasiswa memiliki pengaruh kuat terhadap kelulusan. Mahasiswa dengan nilai masuk tinggi dan penerima beasiswa cenderung memiliki tingkat kelulusan yang lebih tinggi.
* Aspek demografis dan sosial, seperti status sebagai mahasiswa internasional, imigran (displaced), serta usia saat mendaftar, memiliki pola-pola tertentu yang perlu diperhatikan dalam perencanaan dukungan mahasiswa.
* Faktor keuangan dan administrasi, termasuk status pembayaran biaya kuliah dan keberadaan tunggakan, terbukti sangat memengaruhi tingkat keberhasilan mahasiswa. Mahasiswa yang tertib membayar menunjukkan tingkat kelulusan yang lebih tinggi.

Secara keseluruhan, dashboard ini tidak hanya menyajikan data, tetapi juga memberikan insight strategis untuk pengambilan keputusan. Dengan pendekatan berbasis data ini, Jaya Jaya Institut dapat menyusun program pencegahan dropout yang lebih efektif, mendukung mahasiswa yang berisiko, serta meningkatkan kualitas dan reputasi institusi dalam jangka panjang.

### Rekomendasi Action Items
Berdasarkan hasil analisis dan visualisasi pada dashboard Students Performance Analysis, berikut adalah beberapa rekomendasi langkah konkret (action items) yang dapat dilakukan oleh Jaya Jaya Institut untuk mengatasi isu dropout dan meningkatkan performa akademik mahasiswa:

1. Program Dukungan Akademik untuk Mahasiswa Berisiko Tinggi
  * Target: Mahasiswa dengan nilai admission rendah (kategori Low dan Very Low) serta mahasiswa tanpa beasiswa.
  * Tindakan
    * Buat program bimbingan belajar khusus.
    * Adakan sesi konseling akademik rutin.
    * Terapkan sistem early warning untuk absensi dan nilai rendah.
2. Intervensi Keuangan untuk Mahasiswa dengan Masalah Pembayaran
  * Target: Mahasiswa yang memiliki tunggakan (Debtor) atau tidak membayar kuliah tepat waktu.
  * Tindakan:
    * Tawarkan skema pembayaran cicilan atau keringanan biaya.
    * Prioritaskan pemberian beasiswa atau bantuan keuangan bagi mahasiswa berprestasi yang kesulitan membayar.
    * Lakukan edukasi literasi keuangan saat orientasi mahasiswa baru.
3. Pendekatan Khusus untuk Mahasiswa Internasional dan Imigran (Displaced)
  * Target: Mahasiswa internasional dan mahasiswa imigran yang memiliki dropout rate cukup signifikan.
  * Tindakan:
    * Buat program adaptasi budaya dan bahasa.
    * Sediakan mentor akademik dan sosial dari kalangan mahasiswa senior.
    * Bentuk komunitas pendukung (support group)
4. Pemanfaatan Dashboard secara Aktif oleh Pimpinan Akademik
  * Target: Dekan, ketua program studi, dan bagian akademik.
  * Tindakan:
    * Lakukan pelatihan pemanfaatan dashboard sebagai alat monitoring berkala.
    * Gunakan hasil analitik untuk membuat kebijakan berbasis data (data-driven decision making).
    * Integrasikan hasil analisis ke dalam rapat evaluasi triwulanan atau semesteran.
