from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = Weapon(weapon, 50)
        self.health = 200

    def attack(self,dinosaur):
        dinosaur.health -= self.weapon.attack_pwr