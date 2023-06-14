class User:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

    def attack(self, enemy, dmg):
        print(f'Вы атаковали {enemy} на {dmg} очков')

class Magician(User):
    def __init__(self, hp, dmg):
        super().__init__(self, hp, dmg)

class Archer(User):
    def __init__(self, hp, dmg):
        super().__init__(self, hp, dmg)

class Warrior(User):
    def __init__(self, hp, dmg):
        super().__init__(self, hp, dmg)