import random
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon()
        self.health = 200

def attack(self,dinosaur): 
        dinosaur.health -= self.weapon