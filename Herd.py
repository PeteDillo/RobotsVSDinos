from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.herd_up()

    def herd_up(self):
        dino0 = Dinosaur("Timmy Two Rex", 200)
        dino1 = Dinosaur("One Eyed Bill", 200)
        dino2 = Dinosaur("Veli The Raptor", 200)
        self.dinosaurs.append(dino0)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)


