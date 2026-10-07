import random
class hero():
    def __init__(self, name, health, armor, attack, mana = 50) :
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.__inventory = []

    def _str_(self):
        return f"{self.name}"

class marksman(hero):
    def __init__(self, name, health, armor, attack, mana = 50, missChange = 50):
        super().__init__(name, health, armor, attack, mana = 50)
        self.missChange = missChange

    def serang(self, target):
        damage = max(self.attack - target.armor, 0)
        target.diserang(damage)
        print(f"{self.name} menyerang {target.name} dengan damage {damage}. Sisa health {target.name}: {target.health}")

    def diserang(self, jumlah):
        self.health -= max(self.health, jumlah - self.armor)

class fighter(hero):
    def __init__(self, name, health, armor, attack, mana = 50):
        super().__init__(name, health, armor, attack, mana)

    def serang(self, target):
        damage = max(self.attack - target.armor, 0)
        target.diserang(damage)
        print(f"{self.name} menyerang {target.name} dengan damage {damage}. Sisa health {target.name}: {target.health}")

def diserang(self, jumlah):
    self._health -= max(self._health, jumlah - self._armor)

def serang(self, target):
    if random.randint(1, 100) <= self.missChange:
        print(f'{self.name} melesatkan tembakan ke {target.name}!')
    else:
       super ().serang(target)
    

layla = marksman("Layla", 100, 10, 20, 50, 50)
balmond = hero("Balmond", 150, 20, 30, 50)

for i in range(5):
    layla.serang(balmond)
