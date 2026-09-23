# ==========================================
# Posttest PBO: Sistem Manajemen Toko Diecast
# ==========================================

class TokoDiecast:
    nama_toko = "Le Mans Diecast Indonesia"
    lokasi_pusat = "Samarinda" 
    tahun_berdiri = 2026

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.koleksi_diecast = {} 
        self.riwayat_transaksi = []

    # Instance Method
    def tambah_diecast(self, diecast_baru):
        self.koleksi_diecast[diecast_baru.id_produk] = diecast_baru

    # Instance Method
    def tampilkan_katalog(self):
        print(f"\n=== Katalog {self.nama_toko} ===")
        if not self.koleksi_diecast:
            print("Katalog kosong.")
        else:
            for produk in self.koleksi_diecast.values():
                produk.tampilkan_info()
        print("==================================\n")

    # Class Method
    @classmethod
    def info_jaringan_toko(cls):
        print(f"[{cls.nama_toko}] Berdiri tahun {cls.tahun_berdiri}, berpusat di {cls.lokasi_pusat}.")

    # Static Method
    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah


class Diecast:
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk      # Public Atribut
        self.nama = nama                # Public Atribut
        self.harga = harga              # Public Atribut
        self.__stok = stok              # Private Atribut

    # Getter
    @property
    def stok(self):
        return self.__stok

    # Setter dengan Validasi
    @stok.setter
    def stok(self, nilai):
        if not isinstance(nilai, int):
            print("[ERROR] Stok harus berupa angka bulat.")
        elif nilai < 0:
            print(f"[ERROR] Validasi Gagal! Stok untuk '{self.nama}' tidak boleh negatif.")
        else:
            self.__stok = nilai

    # Instance Method
    def tampilkan_info(self):
        status = "Ready" if self.__stok > 0 else "Not Ready"
        print(f"ID {self.id_produk}: {self.nama:<25} | Rp{self.harga:,} | Stok: {self.__stok} ({status})")

    # Class Method 
    @classmethod
    def dari_dictionary(cls, id_produk, data_dict):
        return cls(id_produk, data_dict['Diecast'], data_dict['Harga'], data_dict['stok'])


class Transaksi:
    def __init__(self, id_transaksi, nama_pembeli, diecast, jumlah, total_harga):
        self.id_transaksi = id_transaksi
        self.nama_pembeli = nama_pembeli
        self.diecast = diecast
        self.jumlah = jumlah
        self.__total_harga = total_harga 
        
    @property
    def total_harga(self):
        return self.__total_harga

    @total_harga.setter
    def total_harga(self, nilai):
        if nilai < 0:
            print("[ERROR] Total harga tidak valid.")
        else:
            self.__total_harga = nilai

    def cetak_struk(self):
        print("\n--- STRUK PEMBELIAN ---")
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Pembeli      : {self.nama_pembeli}")
        print(f"Item         : {self.diecast.nama} (x{self.jumlah})")
        print(f"Total Bayar  : Rp{self.__total_harga:,}")
        print("-----------------------\n")


if __name__ == "__main__":
    toko = TokoDiecast("Pusat Samarinda")

    # Load Data Default
    data_produk_default = {
        1: {'Diecast': 'Ferrari 499p', 'stok': 2, 'Harga': 330000},
        2: {'Diecast': 'Porsche 963 LMDh', 'stok': 0, 'Harga': 400000},
        3: {'Diecast': 'Ferrari SF-24', 'stok': 0, 'Harga': 140000},
        4: {'Diecast': 'Porsche 911 GT3', 'stok': 5, 'Harga': 100000},
        5: {'Diecast': 'BMW M4 GT3', 'stok': 0, 'Harga': 150000},
        6: {'Diecast': 'BMW M V8 Hybrid', 'stok': 1, 'Harga': 300000}
    }
    for id_prod, data in data_produk_default.items():
        mobil = Diecast.dari_dictionary(id_prod, data)
        toko.tambah_diecast(mobil)

    id_transaksi_counter = 100

    while True:
        print("\n=== MENU UTAMA LE MANS DIECAST ===")
        print("1. Lihat Katalog Produk")
        print("2. Beli Produk")
        print("3. Update Stok Produk")
        print("4. Uji Validasi Setter (Demo Tugas PBO)")
        print("5. Keluar")
        opsi = input("Pilih Menu (1-5): ")

        if opsi == "1":
            toko.tampilkan_katalog()

        elif opsi == "2":
            toko.tampilkan_katalog()
            try:
                pilih = int(input("Masukkan ID produk yang ingin dibeli: "))
                if pilih in toko.koleksi_diecast:
                    mobil = toko.koleksi_diecast[pilih]
                    if mobil.stok == 0:
                        print("Maaf, produk sedang kosong (Not Ready).")
                        continue
                    
                    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                    if jumlah > mobil.stok:
                        print("Stok tidak mencukupi.")
                    elif jumlah <= 0:
                        print("Jumlah pembelian harus lebih dari 0.")
                    else:
                        nama_pembeli = input("Masukkan nama Anda: ")
                        total = TokoDiecast.hitung_total_harga(mobil.harga, jumlah) 
                        
                        konfirmasi = input(f"Total harga Rp{total:,}. Lanjutkan? (y/n): ").lower()
                        if konfirmasi == 'y':
                            mobil.stok = mobil.stok - jumlah 
                            
                            transaksi_baru = Transaksi(id_transaksi_counter, nama_pembeli, mobil, jumlah, total)
                            toko.riwayat_transaksi.append(transaksi_baru)
                            transaksi_baru.cetak_struk()
                            id_transaksi_counter += 1
                else:
                    print("ID Produk tidak ditemukan.")
            except ValueError:
                print("Input harus berupa angka.")

        elif opsi == "3":
            toko.tampilkan_katalog()
            try:
                id_produk = int(input("Masukkan ID produk untuk diupdate: "))
                if id_produk in toko.koleksi_diecast:
                    mobil = toko.koleksi_diecast[id_produk]
                    stok_baru = int(input(f"Masukkan stok baru untuk {mobil.nama}: "))
                    mobil.stok = stok_baru # Pemicu Setter
                    print(f"Stok {mobil.nama} berhasil diupdate.")
                else:
                    print("ID Produk tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

        elif opsi == "4":
            print("\n--- [DEMO VALIDASI PBO] ---")
            TokoDiecast.info_jaringan_toko() 
            print("Mencoba mengubah stok Ferrari 499P (ID 1) menjadi negatif (-10)...")
            toko.koleksi_diecast[1].stok = -10 
            print(f"Stok Ferrari 499P saat ini tetap: {toko.koleksi_diecast[1].stok}")

        elif opsi == "5":
            print("Terima kasih telah berkunjung!")
            break
        
        else:
            print("Pilihan tidak valid.")