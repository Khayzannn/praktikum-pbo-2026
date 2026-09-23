class Hero:
    jumlah_hero = 0
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        print('objek dibuat')
        Hero.jumlah_hero += 1

def serang(self, lawan):
    print (f"{self.name} menyerang {lawan.name}")
    lawan.diserang(self)

def diserang(self, lawan):
    print (f"{self.name} diserang {lawan.name}")

balmond = Hero("Balmond", 100, 40, 10)
roger = Hero("Roger", 100, 50, 5)

print(Hero.__dict__)

@classmethod
def jumlah_hero(cls):
    print(f"Jumlah hero: {cls.jumlah_hero}")

@staticmethod
def IsCriticalHit(critical):
    return "critical" if critical >= 75 else "normal"

#instance method
def level_up(self):
    self.health += 20
    self.attack += 10
    self.armor += 5
    print(f"{self.name} naik level! Health: {self.health}, Attack: {self.attack}, Armor: {self.armor}")

def healing(self):
    self.health += 10

balmond.health()
balmond.healing()
print(f"Health Balmond: {balmond.health}")