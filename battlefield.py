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
        while len(self.herd.dinosaurs) != 0 or len(self.fleet.robots) != 0:
            self.herd.dinosaurs.dino_turn()
            self.fleet.robots.robo_turn()
        display_winners()



    def dino_turn(self):
        print("Choose your dinosaur to attack:")
        self.show_dino_opponent_options()
        dino_champion = int(input())
        print("Choose the robot that'll defend:")
        self.show_robo_opponent_options()
        robot_champion = int(input())
        self.herd.dinosaurs[dino_champion].attack(self.fleet.robots[robot_champion])
        if self.fleet.robots[robot_champion].health <= 0:
            print(f"{self.fleet.robots[robot_champion].name} has fainted")
            self.fleet.robots.remove(self.fleet.robots[robot_champion])
      

    def robo_turn(self): 
        print("Choose the robot who will attack:")
        self.show_robo_opponent_options()
        robot_champion = int(input())
        print("Choose the dinosaur who will defend:")
        self.show_dino_opponent_options()
        dino_champion = int(input())
        self.fleet.robots[robot_champion].attack(self.herd.dinosaurs[dino_champion])
        if self.herd.dinosaurs[dino_champion].health <= 0:
            print(f"{self.herd.dinosaurs[dino_champion].name} has fainted")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_champion])
          

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
        if self.dino1_battle_ready == 0 and self.dino2_battle_ready.health == 0 and self.dino3_battle_ready.health == 0:
            print("The Dinosaurs went EXTINCT! Robots WIN!")
        if self.robot1_battle_ready.health == 0 and self.robot2_battle_ready.health == 0 and self.robot3_battle_ready.health == 0:
            print("The Robots are DEAD! Dinosaurs WIN!")   

    def run_game(self);
        self.display_welcome()
        self.game_start()
        self.robot0_battle = self.fleet.robots[0]
        self.robot1_battle = self.fleet.robots[1]
        self.robot2_battle = self.fleet.robots[2]
        self.dino0_battle = self.herd.dinosaurs[0]
        self.dino1_battle = self.herd.dinosaurs[1]
        self.dino2_battle = self.herd.dinosaurs[2]
        self.battle()
