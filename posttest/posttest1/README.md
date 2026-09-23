# Laporan Praktikum PBO: Sistem Manajemen Le Mans Diecast

Ketentuan Tugas:
Buat program Python dengan pendekatan OOP sesuai tema yang sudah di-ACC aslab. Program ini harus memakai materi dari tiga modul yang sudah dipelajari: Class & Object (Modul 1), Atribut & Method (Modul 2), serta Encapsulation & Property (Modul 3).
1. Tema dan Class
Tema harus sama dengan yang sudah disetujui. Jika ingin mengganti judul/tema, konfirmasi dan minta persetujuan ke aslab kelas masing-masing terlebih dahulu.
Program minimal memiliki 3 class utama. Class-class ini tidak diwajibkan menggunakan pewarisan (inheritance), cukup class yang berdiri sendiri atau saling berinteraksi (menggunakan objek satu sama lain).
2. Atribut
Atribut kelas: Minimal 3 atribut kelas, berisi data yang dipakai bersama oleh seluruh objek (contoh: nama instansi, total data terdaftar, atau konfigurasi umum).
Atribut instance: Diinisialisasi melalui __init__() menggunakan self, dengan nilai yang unik untuk tiap objek.
Hak akses:
Wajib memiliki atribut Public (dapat diakses langsung).
Wajib memiliki minimal satu atribut Private (__nama) untuk data penting atau sensitif (misal: saldo, pin/password, atau stok inti).
3. Method
Program wajib mengimplementasikan ketiga jenis method:
Instance method 
Minimal satu, menerima self, untuk mengolah, menampilkan, atau mengubah data objek.
Class method (@classmethod) 
Minimal satu, menerima cls. Digunakan untuk mengubah atribut kelas atau sebagai alternatif membuat objek (misal: factory method dari data dictionary).
Static method (@staticmethod) Minimal satu, berupa fungsi bantuan (utility) tanpa parameter self maupun cls (misal: validasi format teks, pengecekan syarat, atau helper perhitungan).
4. Getter, Setter, dan Validasi Data
Akses ke atribut private wajib menggunakan decorator idiomatis Python.
@property sebagai getter.
@<nama_properti>.setter sebagai setter.
Catatan penting sintaks: Nama fungsi setter harus sama persis dengan nama fungsi getter-nya (bukan dinamai get_nama atau set_nama) dan berfungsi memperbarui nilai atribut private yang bersangkutan.
Method setter wajib memiliki validasi data (misal: angka tidak boleh negatif, input tidak boleh kosong). Jika input melanggar validasi, tolak perubahan data (bisa mencetak pesan peringatan atau memunculkan raise ValueError).
5. Pengujian Program (Main Code) 
Pada bagian bawah kode program, lakukan demonstrasi:
Buat minimal 2 objek untuk tiap class.
Panggil dan peragakan seluruh jenis method yang telah dibuat (instance, class, dan static method).
Uji pengisian setter dengan data yang valid dan data yang tidak valid untuk membuktikan validasi berjalan.
Pengumpulan:
Pengumpulan dilakukan melalui GitHub. Kirimkan link repositori GitHub saja.
Buat laporan/dokumentasi mengenai penjelasan program, struktur class, serta panduan pengujian di dalam file README.md.

---

## 🏗️ Struktur Class dan Atribut

Program ini mengimplementasikan 3 *class* utama yang saling berinteraksi:

### 1. Class `TokoDiecast` (Manajemen Utama)
Bertindak sebagai wadah yang mengelola katalog barang dan mencatat riwayat transaksi.
* **Atribut Kelas:** `nama_toko`, `lokasi_pusat`, `tahun_berdiri` (berlaku universal untuk semua objek toko).
* **Atribut Instance:** `nama_cabang`, `koleksi_diecast` (Dictionary), `riwayat_transaksi` (List).
* **Instance Method:** `tambah_diecast()`, `tampilkan_katalog()`.
* **Class Method (`@classmethod`):** `info_jaringan_toko()` untuk memanggil dan mencetak atribut kelas.
* **Static Method (`@staticmethod`):** `hitung_total_harga()` sebagai fungsi *utility* kalkulasi matematika murni.

### 2. Class `Diecast` (Entitas Produk)
Merepresentasikan cetak biru (*blueprint*) dari produk mobil miniatur yang dijual.
* **Atribut Public:** `id_produk`, `nama`, `harga`.
* **Atribut Private:** `__stok` (Disembunyikan agar tidak bisa dimanipulasi dari luar *class*).
* **Getter & Setter:** Menggunakan `@property stok` dan `@stok.setter`. Terdapat **validasi** yang menolak input nilai non-integer dan angka negatif.
* **Class Method (`@classmethod`):** `dari_dictionary()` berfungsi sebagai *factory method* untuk mengonversi data mentah menjadi objek.

### 3. Class `Transaksi` (Entitas Struk)
Merepresentasikan riwayat/bukti pembelian saat pelanggan melakukan *checkout*.
* **Atribut Public:** `id_transaksi`, `nama_pembeli`, `diecast` (Objek produk), `jumlah`.
* **Atribut Private:** `__total_harga`.
* **Getter & Setter:** Dilengkapi validasi untuk menolak total bayar bernilai negatif guna mencegah anomali data transaksi.
* **Instance Method:** `cetak_struk()` untuk menampilkan detail format pembayaran.

---

## 🚀 Panduan Pengujian (Testing Guide)

Untuk membuktikan bahwa seluruh syarat PBO (termasuk validasi dan *method*) berjalan dengan baik, lakukan skenario pengujian berikut saat program dijalankan:

### Pengujian 1: Simulasi Pembelian (Interaksi antar Class)
1. Jalankan program dan pilih menu **2 (Beli Produk)**.
2. Masukkan ID produk yang tersedia (misal: `1` untuk Ferrari 499P).
3. Masukkan jumlah beli dan ketik nama.
4. **Hasil:** Program akan memanggil *Static Method* untuk menghitung total harga, mengurangi atribut `__stok` menggunakan *Setter*, membuat objek `Transaksi` baru, dan mencetak struk pembelian secara otomatis.

### Pengujian 2: Uji Validasi Setter (Demonstrasi Syarat PBO)
1. Pada Menu Utama, pilih menu **4 (Uji Validasi Setter)**.
2. **Hasil:** Program akan mendemonstrasikan dua hal secara otomatis:
   * Memanggil *Class Method* untuk mencetak "Berdiri tahun 2026, berpusat di Samarinda".
   * Menguji *Setter* dengan mencoba memasukkan nilai stok `-10` ke produk ID 1. Sistem akan secara otomatis memblokirnya dan memunculkan notifikasi `[ERROR] Validasi Gagal! Stok tidak boleh negatif`.
3. Anda juga bisa mengujinya secara manual melalui menu **3 (Update Stok Produk)** dan mencoba memasukkan huruf atau angka minus.
