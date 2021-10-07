class Dinosaur:
    def __init__(self, name, attack_pwr):
        self.name = name
        self.attack_pwr = attack_pwr
        self.health = 250

    def attack(self, robot):
        robot.health -= self.attack_pwr
