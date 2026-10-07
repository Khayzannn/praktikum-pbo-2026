class Pembeli:
    def __init__(self, nama):
        self.nama = nama

class Struk:
    def __init__(self, id_transaksi, teks_detail):
        self.id_transaksi = id_transaksi
        self.teks_detail = teks_detail

    def cetak(self):
        print("\n" + "="*30)
        print(f" STRUK TRANSAKSI #{self.id_transaksi}")
        print("="*30)
        print(self.teks_detail)
        print("="*30 + "\n")


class Diecast:
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk
        self._nama = nama
        self._harga = harga
        self.__stok = stok

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if not isinstance(nilai, int) or nilai < 0:
            print(f"[ERROR] Stok untuk '{self._nama}' tidak valid (tidak boleh negatif).")
        else:
            self.__stok = nilai

    def tampilkan_info(self):
        status = "Ready" if self.__stok > 0 else "Not Ready"
        print(f"ID {self.id_produk}: {self._nama:<25} | Rp{self._harga:,} | Stok: {self.__stok} ({status})")

class DiecastF1(Diecast):
    def __init__(self, id_produk, nama, harga, stok, tim_f1):
        super().__init__(id_produk, nama, harga, stok)
        self.tim_f1 = tim_f1

    def tampilkan_info(self):
        status = "Ready" if self.stok > 0 else "Not Ready"
        print(f"ID {self.id_produk}: [Formula 1] {self._nama:<19} | Tim: {self.tim_f1:<10} | Rp{self._harga:,} | Stok: {self.stok} ({status})")

class DiecastEndurance(Diecast):
    def __init__(self, id_produk, nama, harga, stok, kategori_balap):
        super().__init__(id_produk, nama, harga, stok)
        self.kategori_balap = kategori_balap

    def tampilkan_info(self):
        status = "Ready" if self.stok > 0 else "Not Ready"
        print(f"ID {self.id_produk}: [Endurance] {self._nama:<19} | Kategori: {self.kategori_balap:<5} | Rp{self._harga:,} | Stok: {self.stok} ({status})")



class Transaksi:
    def __init__(self, id_transaksi, pembeli, diecast, jumlah):
        self.id_transaksi = id_transaksi
        self.pembeli = pembeli       
        self.diecast = diecast       
        self.jumlah = jumlah
        self.__total_harga = diecast._harga * jumlah 
        detail = f"Pembeli    : {self.pembeli.nama}\n Item: {self.diecast._nama} (x{self.jumlah})\nTotal Bayar: Rp{self.__total_harga:,}"
        self.struk = Struk(self.id_transaksi, detail)

class TokoDiecast:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.koleksi_diecast = {} 
        self.riwayat_transaksi = []

    def tambah_diecast(self, diecast_baru):
        self.koleksi_diecast[diecast_baru.id_produk] = diecast_baru

    def tampilkan_katalog(self):
        print(f"\n=== Katalog {self.nama_toko} ===")
        for produk in self.koleksi_diecast.values():
            produk.tampilkan_info()
        print("============================================\n")

    def layani_pembelian(self, pembeli, id_produk, jumlah):
        mobil = self.koleksi_diecast.get(id_produk)
        if not mobil:
            print("ID Produk tidak ditemukan.")
            return

        if jumlah > mobil.stok:
            print("Gagal: Stok tidak mencukupi!")
            return

        mobil.stok -= jumlah
        
        trx_baru = Transaksi(len(self.riwayat_transaksi) + 101, pembeli, mobil, jumlah)
        self.riwayat_transaksi.append(trx_baru)
        
        trx_baru.struk.cetak()


if __name__ == "__main__":
    toko = TokoDiecast("Le Mans Diecast Samarinda")

    f1_1 = DiecastF1(1, "Ferrari SF-26", 140000, 5, "Ferrari")
    f1_2 = DiecastF1(2, "McLaren F1", 140000, 3, "McLaren")
    f1_3 = DiecastF1(5, "Mercedes W17", 150000, 0, "Mercedes")
    f1_4 = DiecastF1(6, "Red Bull RB22", 150000, 2, "Red Bull")
    
    endurance_1 = DiecastEndurance(3, "Ferrari 499p", 330000, 2, "LMH")
    endurance_2 = DiecastEndurance(4, "Porsche 963 LMDh", 400000, 0, "LMDh")
    endurance_3 = DiecastEndurance(7, "Toyota GR010", 350000, 1, "LMH")
    endurance_4 = DiecastEndurance(8, "Cadillac V-LMDh", 360000, 0, "LMDh")

    toko.tambah_diecast(f1_1)
    toko.tambah_diecast(f1_2)
    toko.tambah_diecast(f1_3)
    toko.tambah_diecast(f1_4)
    toko.tambah_diecast(endurance_1)
    toko.tambah_diecast(endurance_2)
    toko.tambah_diecast(endurance_3)
    toko.tambah_diecast(endurance_4)
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Lihat Katalog Produk")
        print("2. Beli Produk")
        print("3. Uji Validasi PBO (Stok Negatif)")
        print("4. Keluar")
        opsi = input("Pilih Menu: ")

        if opsi == "1":
            toko.tampilkan_katalog()

        elif opsi == "2":
            toko.tampilkan_katalog()
            nama = input("Masukkan Nama Pembeli: ")
            
            pembeli = Pembeli(nama) 
            
            try:
                id_produk = int(input("Masukkan ID produk yang ingin dibeli: "))
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                
                toko.layani_pembelian(pembeli, id_produk, jumlah)
            except ValueError:
                print("Input harus berupa angka!")

        elif opsi == "3":
            print("\n--- [DEMO VALIDASI INHERITANCE] ---")
            print("Mencoba memaksa stok Ferrari 499p (ID 3) menjadi -5...")
            toko.koleksi_diecast[3].stok = -5 

        elif opsi == "4":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid.")