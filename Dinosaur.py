class Dinosaur:
    def __init__(self):
        self.name = ""
        self.attack_pwr = ""
        self.health = ""

    def __str__(self) -> str:
        return self.name