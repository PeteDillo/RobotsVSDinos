import random
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon()
        self.health = random.randint(150, 250)

def attack(self,dinosaur): 
        dinosaur.health -= self.weapon