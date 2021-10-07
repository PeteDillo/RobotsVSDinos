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


    def dino_turn(self):
        print("Choose your dinosaur to attack:")
        self.show_dino_opponent_options()
        dino_champion = int(input())
        print("Choose the robot that'll defend:")
        self.show_robo_opponent_options()
        robot_champion = int(input())
        self.herd.dinosaurs[dino_champion].attack(self.fleet.robots[robot_champion])
        if self.fleet.robots[robot_champion].health <= 0:
            print(f"{self.fleet.robots[robot_champion]} has fainted")
            self.fleet.robots.remove(self.fleet.robots[robot_champion])
        else:
            robo_turn()        