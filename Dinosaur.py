from robot import Robot


import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_pwr = 200
        self.health = 300

    def attack(self, robot):
        robot.health -= self.attack_pwr
        