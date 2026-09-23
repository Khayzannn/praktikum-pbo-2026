class Hero:
    MAKS_SLOT = 6  # Perbaikan 2: Deklarasi batas maksimal slot inventory

    def __init__(self, name, health, mana, armor, attack, gold, daftar_skill, skills):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self.__inventory = []
        self.__skills = [skill(name, dmg, mana) for name, dmg, mana in daftar_skill]

    def beli_item(self, item, toko):
        if len(self.__inventory) >= Hero.MAKS_SLOT:
            print(f"Slot inventory penuh, tidak bisa membeli {item.name}")
            return  

        if toko.proses_pembelian(self, item):
            self.__inventory.append(item)
            print(f"> {self.name} berhasil memasukkan {item.name} ke dalam inventory.\n")

    def cast_skill(self, nomor, lawan):
        skill = self.__skills [nomor-1]  # Mengakses skill berdasarkan nomor (1-3)
        if self.mana >= skill.mana_cost:
            self.mana -= skill.mana_cost
            print(f"{self.name} menggunakan skill {skill.name} ke {lawan.name}. (Sisa mana: {self.mana})")
            lawan.receive_damage(skill.damage)
            return
        self.mana -= skill.mana_cost
        lawan.receive_damage(skill.damage)
        print(f"{self.name} menggunakan skill {skill.name} ke {lawan.name}. (Sisa mana: {self.mana})")


class Shop: 
    def __init__(self, name):
        self.name = name
        self.__daftar_item = []

    
    def proses_pembelian(self, hero, item):
        if hero.gold >= item.harga:
            hero.gold -= item.harga  # Proses transaksi berhasil
            print(f"[{self.name}] {hero.name} membeli {item.name} seharga {item.harga} gold. (Sisa gold: {hero.gold})")
            return True
        else:
            print(f"[{self.name}] Transaksi gagal! Gold {hero.name} tidak mencukupi.")
            return False


class Item:
    def __init__(self, name, harga, bonus_attack, bonus_armor):
        self.name = name
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor
        
    def __str__(self):
        return f"{self.name} (harga: {self.harga}, bonus attack: {self.bonus_attack}, bonus armor: {self.bonus_armor})"


lylia = Hero("Lylia", 100, 30, 4, 15, 5000, [['tembak', 25, 40]])
layla = Hero("Layla", 100, 30, 4, 15, 5000, [['laser', 25, 40]])
print 
BOD = Item("Blade of Despair", 3000, 350, 0)
toko_ml = Shop("Toko Item Rahasia")
print (lylia.__dict__)
print(lylia.name)

lylia.beli_item(BOD, toko_ml)

# Uji coba jika gold kurang (opsional untuk melihat validasi toko)
# item_mahal = Item("Holy Crystal", 3000, 100, 0)
# lylia.beli_item(item_mahal, toko_ml)