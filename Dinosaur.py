from robot import Robot


import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_pwr = random.randint(25, 75)
        self.health = random.randint(200, 300)

    def attack(self, robot):
        robot.health -= self.attack_pwr