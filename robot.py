class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 200

    def attack(self,dinosaur):
        dinosaur.health -= self.weapon