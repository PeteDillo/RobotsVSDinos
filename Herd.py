from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.herd_up()

    def herd_up(self):
        dino0 = Dinosaur("Timmy Two Rex", 35)
        dino1 = Dinosaur("One Eyed Bill", 35)
        dino2 = Dinosaur("Veli The Raptor", 35)
        self.dinosaurs.append(dino0)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)


