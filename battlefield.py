from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()
        self.robot0_battle_ready = self.fleet.robots[0]
        self.robot1_battle_ready = self.fleet.robots[1]
        self.robot2_battle_ready = self.fleet.robots[2]
        self.dino0_battle_ready = self.herd.dinosaurs[0]
        self.dino1_battle_ready = self.herd.dinosaurs[1]
        self.dino2_battle_ready = self.herd.dinosaurs[2]

    def display_welcome(self):
        pass
    
