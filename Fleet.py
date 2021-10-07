from weapon import Weapon
from robot import Robot 

class Fleet:
    def __init__(self):
        self.robots = []
        self.armory = []
        self.weapon_create()
        self.make_fleet()

    def weapon_create(self):
        weapon0 = Weapon("The Laser Sword", 50)
        weapon1 = Weapon("The Sword That Shoots Lasers", 50)
        weapon2 = Weapon("The Sword Laser", 50)
        self.armory.append(weapon0)
        self.armory.append(weapon1)
        self.armory.append(weapon2)
    
    
    def make_fleet(self):
        robot0 = Robot('Killer Term', "The Laser Sword")
        robot1 = Robot('Murderest Kim', "The Sword That Shoots Lasers")
        robot2 = Robot('Pyscho Bob', "The Sword Laser")
        self.robots.append(robot0)
        self.robots.append(robot1)
        self.robots.append(robot2)     