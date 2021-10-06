class Robot:
    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.health = ""

    def __str__(self) -> str:
        return self.name    