from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def herd_up(self):
        dino0 = Dinosaur("Timmy Two Rex")
        dino1 = Dinosaur("One Eyed Bill")
        dino2 = Dinosaur("Veli The Raptor")
        self.dinosaurs.append(dino0)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)


