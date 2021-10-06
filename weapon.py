class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_pwr = ""
        
    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.attack_pwr
        