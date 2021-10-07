from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()
        self.robot0_battle = self.fleet.robots[0]
        self.robot1_battle = self.fleet.robots[1]
        self.robot2_battle = self.fleet.robots[2]
        self.dino0_battle = self.herd.dinosaurs[0]
        self.dino1_battle = self.herd.dinosaurs[1]
        self.dino2_battle = self.herd.dinosaurs[2]

    def display_welcome(self):
        print("This is END GAME")

    def battle(self,turn): 
        if(turn == 1 or turn == 3):
            self.battle = True
        elif(turn == 2 or turn == 4):
            self.battle = False
        else:
            print("Illegal turn")