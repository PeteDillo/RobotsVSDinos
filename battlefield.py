from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print("This is END GAME")

    def game_start(self):    
        user = input("Ready to fight for survival? Enter y or n.")
        if(user == "y"):
            print("**Game Starts**")

    def battle(self): 
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            if len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
                self.dino_turn()
            elif len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
                self.robo_turn()
        print(self.herd.dinosaurs)          
        self.herd.dinosaurs.display_winnners()



    def dino_turn(self):
        print("Choose your dinosaur to attack:")
        self.show_dino_opponent_options()
        dino_champion = int(input())
        if len(self.fleet.robots) > 0:
            print("Choose the robot that'll defend:")
            self.show_robo_opponent_options()
            robot_champion = int(input())
            self.herd.dinosaurs[dino_champion].attack(self.fleet.robots[robot_champion])
            if self.fleet.robots[robot_champion].health <= 0:
                print(f"{self.fleet.robots[robot_champion].name} has fainted")
                self.fleet.robots.remove(self.fleet.robots[robot_champion])
        else: 
            self.display_winnners()
        
    def robo_turn(self): 
        print("Choose the robot who will attack:")
        self.show_robo_opponent_options()
        robot_champion = int(input())
        if len(self.herd.dinosaurs) > 0:
            print("Choose the dinosaur who will defend:")
            self.show_dino_opponent_options()
            dino_champion = int(input())
            self.fleet.robots[robot_champion].attack(self.herd.dinosaurs[dino_champion])
            if self.herd.dinosaurs[dino_champion].health <= 0:
                print(f"{self.herd.dinosaurs[dino_champion].name} has fainted")
                self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_champion])
        else: 
            self.display_winnners()  

    def show_dino_opponent_options(self): 
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"Press {dino_index} for {dino.name}")
            dino_index += 1        


    def show_robo_opponent_options(self): 
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"Press {robot_index} for {robot.name}")
            robot_index += 1        

    def display_winners(self): 
        if len(self.herd.dinosaurs == 0 ):
            print("The Dinosaurs went EXTINCT! Robots WIN!")
        if len(self.fleet.robots ==  0 ):
            print("The Robots are DEAD! Dinosaurs WIN!")   

    def run_game(self):
        self.display_welcome()
        self.game_start()
        self.robot0_battle = self.fleet.robots[0]
        self.robot1_battle = self.fleet.robots[1]
        self.robot2_battle = self.fleet.robots[2]
        self.dino0_battle = self.herd.dinosaurs[0]
        self.dino1_battle = self.herd.dinosaurs[1]
        self.dino2_battle = self.herd.dinosaurs[2]
        self.battle()   
       
