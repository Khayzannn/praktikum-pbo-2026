class hero:
    jumlah_hero = 0
    def __init__(self, name, health, attack, armor):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        self.__name = "None"

miya = hero("miya", 100, 10, 5)

# miya.name = "miya baru"
# print(miya.name)

del miya.name