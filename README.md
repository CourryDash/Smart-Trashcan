# Smart-Trashcan
Project Agile [Kelompok O7] - due 31 Maret 2026

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
