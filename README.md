# Smart-Trashcan
Project Agile [Kelompok O7]

Penjelasan Project :
Project ini adalah pengembangan tempat sampah pintar (Smart Trashcan) berbasis Internet of Things (IoT) untuk mengatasi masalah penumpukan sampah dan pengelolaan yang kurang baik. Alat ini mampu menyortir sampah secara otomatis ke dalam tiga kategori (Organik, Anorganik, dan B3) guna menurunkan persentase sampah yang tidak terkelola. 

Selain berfokus pada efisiensi daur ulang, project ini juga menonjolkan sistem keamanan tingkat tinggi mengingat maraknya fasilitas umum yang hilang. Tempat sampah ini dilengkapi sistem verifikasi akses untuk petugas , pelacakan lokasi, hingga tindakan preventif berupa kejut listrik dan sirine jika tempat sampah dipindahkan dari koordinatnya, yang terintegrasi langsung dengan laporan ke kepolisian terdekat.

===

Fitur-fitur : 
A) Fitur Utama Penyortiran & Sensor (Perangkat Keras & IoT)
1. Penyortiran Otomatis: Sistem yang menyortir sampah secara otomatis berdasarkan jenisnya, yaitu organik, anorganik, dan B3.
2. Database Sampah: Basis data cerdas yang menyimpan referensi klasifikasi sampah untuk membantu sensor (kamera dan inframerah) dalam mendeteksi jenis sampah.
3. Monitoring Kapasitas Spesifik: Melacak persentase kepenuhan tong sampah secara real-time, dipisah berdasarkan masing-masing kompartemen (organik, anorganik, B3).
4. Status Kesehatan Sensor: Indikator untuk memastikan kamera dan sensor pembaca berfungsi dengan baik dan tidak tertutup kotoran.
5. Peringatan Kemacetan Mekanik: Notifikasi sistem jika motor/servo penyortir sampah macet atau terganjal.
6. Monitoring Daya/Baterai: Indikator untuk memantau sisa daya atau baterai dari modul IoT agar perangkat tidak mati secara tiba-tiba.

B) Fitur Keamanan & Penanganan Insiden

7. Verifikasi Akses Petugas (RFID): Sistem penguncian yang memastikan hanya petugas berwenang yang dapat membuka dan mengosongkan tong sampah menggunakan verifikasi kartu RFID.
8. Kejut Listrik Preventif: Fitur keamanan yang menembakkan kejut listrik non-mematikan untuk melumpuhkan oknum jika tong sampah dipaksa buka atau berpindah koordinat.
9. Sirine Peringatan: Alarm yang secara otomatis berbunyi untuk memancing perhatian orang di sekitar apabila terjadi pelanggaran keamanan.
10. Pelacakan Lokasi (GPS): Sensor lokasi untuk mendeteksi jika tempat sampah berpindah koordinat dari tempat asalnya.
11. Notifikasi Darurat Polisi: Fitur auto-dispatch yang langsung mengirimkan informasi ke kantor polisi terdekat saat terjadi upaya pencurian tong sampah.

C) Fitur Aplikasi & Antarmuka Pengguna (UI)

12. Sistem Login Terdaftar: Portal masuk ke aplikasi yang hanya bisa diakses oleh penjaga/petugas kebersihan dengan ID yang sudah terdaftar di database.
13. Pembatasan Hak Akses (Role-Based Access): Pemisahan antarmuka dan fitur antara pengguna umum (hanya bisa melihat edukasi atau status tong sampah) dan penjaga (memiliki akses operasional).
14. Peringatan Akses Ditolak: Menampilkan pesan error pada layar UI perangkat maupun aplikasi jika identitas/kartu yang di-tap tidak sesuai.
15. Notifikasi Tong Sampah Penuh: Peringatan yang dikirimkan ke server pusat atau smartphone petugas saat tong sampah sudah mencapai kapasitas maksimal.
16. Dashboard Progress (Track Kepenuhan): Tampilan visual yang menunjukkan persentase kepenuhan Smart Trashcan saat ini.
17. Peta Lokasi Tong Sampah: Fitur visual (map) di UI admin untuk melihat letak seluruh tong sampah beserta statusnya (penuh, kosong, atau error).

D) Fitur Manajemen & Pelaporan Sistem

18. Log Aktivitas Operasional: Pencatatan otomatis yang menyimpan riwayat data mengenai penjaga siapa yang login, serta kapan tong sampah tersebut dikosongkan.
19. Fitur Reset/Pengosongan: Tombol perintah di aplikasi bagi petugas untuk mereset indikator persentase sampah kembali ke 0% setelah fisik tong sampah dikosongkan.
20. Database Penjaga: Basis data untuk mengelola, menambah, atau menghapus daftar petugas kebersihan yang diberikan wewenang.
21. Laporan dan Analitik Data: Fitur yang mengolah data dari server pusat untuk menampilkan grafik volume sampah harian atau mingguan guna memantau tingkat efisiensi daur ulang.

===

Timeline Pengerjaan Fitur (Agile/Scrum Approach)
Pengembangan dilakukan menggunakan metode Agile dengan pembagian Sprint (berdurasi 2 minggu per sprint):

- Sprint 1: Core IoT & Database (Minggu 1 - 2)
Target Selesai: Fitur 1 (Penyortiran), Fitur 9 (Database Sampah), Fitur 11 (Track Progress), Fitur 16 (Kapasitas Spesifik).

- Sprint 2: Security & Emergency Protocol (Minggu 3 - 4)
Target Selesai: Fitur 2 (Keamanan Aktif), Fitur 14 (GPS Tracking), Fitur 15 (Laporan Polisi).

- Sprint 3: Authentication & User Management (Minggu 5 - 6)
Target Selesai: Fitur 4 (Login Penjaga), Fitur 8 (Hak Akses), Fitur 10 (Validasi ID), Fitur 12 (Database Penjaga), Fitur 13 (Error Identitas).

- Sprint 4: Application Dashboard & Operations (Minggu 7 - 8)
Target Selesai: Fitur 3 (Notifikasi Penuh), Fitur 5 (Log Aktivitas), Fitur 6 (Reset Kapasitas), Fitur 7 (UI Dashboard).

- Sprint 5: System Polish & Advanced Monitoring (Minggu 9 - 10)
Target Selesai: Fitur 17 (Kesehatan Sensor), Fitur 18 (Peringatan Mekanik), Fitur 19 (Monitoring Daya), Fitur 20 (Peta Tong Sampah), Fitur 21 (Analitik Data).
