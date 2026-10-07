from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    @abstractmethod
    def hitung_damage(self, target):
        pass

    def serang(self, target):
        damage = self.hitung_damage(target)
        target.health -= damage
        print(f"{self.name} menyerang {target.name} dengan damage {damage}. (Sisa HP {target.name}: {target.health})")


class Fighter(Hero):
    def hitung_damage(self, target):
        return max(0, self.attack - target.armor)


class Mage(Hero):
    def hitung_damage(self, target):
        return self.attack

    def ulti(self):
        print(f"{self.name} menggunakan ulti!")

    def __str__(self):
        print(f"namaku adalah {self.name}")

class Warrior(Hero):
    def ulti(self):
        pass

class Minion(Hero):
    def __init__(self, name, health, attack, armor=2):
        super().__init__(name, health, attack, armor)

    def hitung_damage(self, target):
        return max(0, self.attack - target.armor)



balmond = Fighter("Balmond", 100, 20, 4)
eudora = Mage("Eudora", 80, 15, 2)

minion_kecil = Minion("Minion", 50, 10, 1)

balmond.serang(eudora)
eudora.serang(balmond)
minion_kecil.serang(balmond)
