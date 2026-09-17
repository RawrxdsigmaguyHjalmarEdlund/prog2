class Player:
    def låta(self):
        print("Player låter")

class Warrior(Player):
    def låta(self):
        print("Warrior låter")

class Mage(Player):
    def låta(self):
        print("Mage låter")

Players = [
    Player(),
    Warrior(),
    Mage()
]

for Player in Players:
    Player.låta()