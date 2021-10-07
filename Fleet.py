from weapon import Weapon
from robot import Robot 

class Fleet:
    def __init__(self):
        self.robots = []
        self.armory = []
        self.weapon_create()
        self.make_fleet()

    def weapon_create(self):
        weapon0 = Weapon("",50)
        weapon1 = Weapon("",50)
        weapon2 = Weapon("",50)
        self.armory.append(weapon0)
        self.armory.append(weapon1)
        self.armory.append(weapon2)
    
    
    def make_fleet(self):
        robot0 = Robot('')
        robot1 = Robot('')
        robot2 = Robot('')
        self.robots.append(robot0)
        self.robots.append(robot1)
        self.robots.append(robot2)     