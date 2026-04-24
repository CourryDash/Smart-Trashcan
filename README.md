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

- Sprint 1: "The Brain & The Shell" (Fondasi Dasar)
Fokus pada fungsi inti: Bisa membedakan sampah dan punya tempat menyimpannya.

Target (Goal): Alat bisa mengenali satu jenis sampah dan datanya tersimpan di database.

Fitur yang diambil: 
Fitur 2: Database Sampah (versi awal/MVP).
Fitur 1: Penyortiran Otomatis (mekanik dasar).
Fitur 20: Database Penjaga (agar ada yang bisa akses sistem).

Kenapa? Karena tanpa database sampah, sensor tidak tahu apa yang harus dilakukan.

- Sprint 2: "Connected Trashcan" (IoT & Konektivitas)
Fokus pada komunikasi alat dengan aplikasi.

Target (Goal): Petugas bisa tahu lewat aplikasi kalau tong sampah mulai penuh.

Fitur yang diambil:
- Fitur 3: Monitoring Kapasitas Spesifik.
- Fitur 15: Notifikasi Tong Sampah Penuh (ke aplikasi).
- Fitur 12: Sistem Login Terdaftar (agar petugas bisa masuk ke aplikasi).
- Fitur 16: Dashboard Progress (tampilan visual di HP).

Ini adalah nilai jual utama Smart Trashcan. Memberi tahu status tanpa harus mendatangi lokasi.

- Sprint 3: "Security & Guard" (Keamanan & Akses)
Fokus pada perlindungan alat karena alat ini mahal (banyak sensor).

Target (Goal): Hanya orang tertentu yang bisa buka alat, dan alat aman dari pencurian.

Fitur yang diambil:
- Fitur 7: Verifikasi Akses RFID (untuk buka fisik tong).
- Fitur 10: Pelacakan Lokasi/GPS.
- Fitur 9: Sirine Peringatan.
- Fitur 14: Peringatan Akses Ditolak.

Kenapa? Sebelum alat disebar ke tempat umum, fitur keamanan harus siap agar investasi hardware tidak hilang dicuri.

- Sprint 4: "Health & Maintenance" (Ketahanan Sistem)
Fokus pada pemeliharaan agar alat tidak cepat rusak.

Target (Goal): Admin tahu kalau alat macet atau baterai mau habis sebelum terjadi kerusakan.

Fitur yang diambil:
- Fitur 4: Status Kesehatan Sensor.
- Fitur 5: Peringatan Kemacetan Mekanik.
- Fitur 6: Monitoring Daya/Baterai.
- Fitur 19: Fitur Reset (setelah sampah diambil).

- Sprint 5: "Advanced Control & Security"
Fokus pada hak akses yang lebih detail dan fitur keamanan tingkat tinggi.

Target (Goal): Mengatur siapa yang bisa melihat apa dan mengaktifkan proteksi fisik otomatis.

Fitur yang diambil:
- Fitur 13: Role-Based Access (Membedakan tampilan admin vs user umum).
- Fitur 8: Kejut Listrik Preventif (Ini fitur paling berisiko, dikerjakan paling akhir).
- Fitur 11: Notifikasi Darurat Polisi (Integrasi eksternal).

Kenapa? Fitur ini butuh sistem dasar yang sudah sangat stabil di Sprint 1-4.

- Sprint 6: "Analytics & Monitoring Center"
Fokus pada pengolahan data untuk kebutuhan manajemen jangka panjang.

Target (Goal): Memberikan gambaran besar kepada pimpinan melalui data dan peta.

Fitur yang diambil:
- Fitur 17: Peta Lokasi Tong Sampah (Visualisasi map untuk banyak titik).
- Fitur 18: Log Aktivitas Operasional (Rekaman riwayat kerja).
- Fitur 21: Laporan dan Analitik Data (Grafik volume sampah mingguan).
