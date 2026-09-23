# Sistem Manajemen Toko Diecast

class TokoDiecast:
    nama_toko = "Le Mans Diecast Indonesia"
    lokasi_pusat = "Samarinda" 
    tahun_berdiri = 2026

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.koleksi_diecast = {} 
        self.koleksi_user = {}    
        self.user_login = None

    def tambah_diecast(self, diecast_baru):
        self.koleksi_diecast[diecast_baru.id_produk] = diecast_baru

    def tampilkan_katalog(self):
        print(f"\n=== Katalog {self.nama_toko} ===")
        for id_produk, produk in self.koleksi_diecast.items():
            produk.tampilkan_info()
        print("==================================\n")

    @classmethod
    def info_jaringan_toko(cls):
        print(f"[{cls.nama_toko}] Berdiri tahun {cls.tahun_berdiri}, berpusat di {cls.lokasi_pusat}.")

    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah


class Diecast:
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk      
        self.nama = nama                
        self.harga = harga              
        self.__stok = stok              

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if not isinstance(nilai, int):
            print("[ERROR] Stok harus berupa angka.")
        elif nilai < 0:
            print(f"[ERROR] Gagal! Stok untuk '{self.nama}' tidak boleh negatif.")
        else:
            self.__stok = nilai

    def tampilkan_info(self):
        status = "Ready" if self.__stok > 0 else "Not Ready"
        print(f"ID {self.id_produk}: {self.nama:<25} | Rp{self.harga:,} | Stok: {self.__stok} ({status})")

    @classmethod
    def dari_dictionary(cls, id_produk, data_dict):
        return cls(id_produk, data_dict['Diecast'], data_dict['Harga'], data_dict['stok'])


class User:
    def __init__(self, username, role, password):
        self.username = username        
        self.role = role                
        self.__password = password      

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if not password_baru or len(password_baru) < 5:
            print("[ERROR] Password minimal 5 karakter!")
        else:
            self.__password = password_baru

    # 3. Static Method
    @staticmethod
    def sapa_user(username, role):
        print(f"\nSelamat datang, {username}! Anda login sebagai {role.upper()}.")


toko = TokoDiecast("Pusat")

data_produk_default = {
    1: {'Diecast': 'Ferrari 499p', 'stok': 2, 'Harga': 330000},
    2: {'Diecast': 'Porsche 963 LMDh', 'stok': 0, 'Harga': 400000},
    3: {'Diecast': 'Ferrari SF-24', 'stok': 0, 'Harga': 140000},
    4: {'Diecast': 'Porsche 911 GT3', 'stok': 5, 'Harga': 100000},
    5: {'Diecast': 'BMW M4 GT3', 'stok': 0, 'Harga': 150000},
    6: {'Diecast': 'BMW M V8 Hybrid', 'stok': 1, 'Harga': 300000},
    7: {'Diecast': 'Mercedes AMG Petronas F1', 'stok': 0, 'Harga': 140000},
    8: {'Diecast': 'McLaren F1', 'stok': 3, 'Harga': 140000},
    9: {'Diecast': 'Lotus 67', 'stok': 0, 'Harga': 40000},
    10: {'Diecast': 'Peugeot 9x8', 'stok': 6, 'Harga': 190000},
    11: {'Diecast': 'Cadillac V-Series R V8', 'stok': 0, 'Harga': 50000}
}
for id_prod, data in data_produk_default.items():
    mobil = Diecast.dari_dictionary(id_prod, data)
    toko.tambah_diecast(mobil)

admin_default = User("Attol", "admin", "adminGanteng67")
toko.koleksi_user["Attol"] = admin_default


def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Stok\n2. Update Stok\n3. Uji Validasi Setter (Demo Tugas)\n4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            toko.tampilkan_katalog()
        elif pilihan == "2":
            toko.tampilkan_katalog()
            id_produk = int(input("ID produk: "))
            if id_produk in toko.koleksi_diecast:
                mobil = toko.koleksi_diecast[id_produk]
                jumlah = int(input("Ubah stok menjadi berapa? "))
                mobil.stok = jumlah 
                print(f"Stok sekarang: {mobil.stok} unit")
            else:
                print("ID tidak valid.")
        elif pilihan == "3":
            print("\n--- [DEMO TUGAS PBO] ---")
            TokoDiecast.info_jaringan_toko() # Panggil Class Method
            print("Mencoba ubah stok Ferrari 499P (ID 1) jadi -5...")
            toko.koleksi_diecast[1].stok = -5 # Pemicu penolakan setter
        elif pilihan == "4":
            break

def menu_pembeli():
    while True:
        print("\n=== Menu Pembeli ===")
        print("1. Lihat Produk\n2. Beli Produk\n3. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            toko.tampilkan_katalog()
        elif pilihan == "2":
            toko.tampilkan_katalog()
            pilih = int(input("Pilih ID produk yang ingin dibeli: "))
            if pilih in toko.koleksi_diecast:
                mobil = toko.koleksi_diecast[pilih]
                if mobil.stok == 0:
                    print("Produk tidak tersedia.")
                    continue
                
                jumlah = int(input("Masukkan jumlah: "))
                if jumlah > mobil.stok:
                    print("Stok tidak mencukupi.")
                else:
                    total = TokoDiecast.hitung_total_harga(mobil.harga, jumlah) # Panggil static method
                    print(f"Total harga: Rp{total:,}")
                    if input("Lanjutkan (ya/tidak)? ").lower() == 'ya':
                        mobil.stok = mobil.stok - jumlah # Pemicu Setter
                        print("Berhasil dibeli!")
            else:
                print("ID tidak valid")
        elif pilihan == "3":
            break

if __name__ == "__main__":
    while True:
        print("\n=== Le Mans Diecast Indonesia ===")
        print("1. Registrasi\n2. Login\n3. Keluar")
        opsi = input("Pilih Menu: ")
        
        if opsi == "1":
            uname = input("Username: ")
            if uname not in toko.koleksi_user:
                pw = input("Password: ")
                role = input("Role (admin/pembeli): ").lower()
                user_baru = User(uname, role, pw)
                
                # Uji validasi setter password
                if user_baru.password == pw: # Jika password lolos validasi (gak kosong/kependekan)
                    toko.koleksi_user[uname] = user_baru
                    print("Registrasi Berhasil!")
            else:
                print("Username sudah ada.")
                
        elif opsi == "2":
            uname = input("Username: ")
            pw = input("Password: ")
            
            if uname in toko.koleksi_user and toko.koleksi_user[uname].password == pw:
                user_aktif = toko.koleksi_user[uname]
                User.sapa_user(user_aktif.username, user_aktif.role) # Panggil static method
                
                if user_aktif.role == 'admin':
                    menu_admin()
                else:
                    menu_pembeli()
            else:
                print("Login Gagal! Username/Password salah.")
                
        elif opsi == "3":
            print("Terima kasih!")
            break