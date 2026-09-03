class player:
    def __init__(self, level, Hp):
         self.level = level
         self.Hp = Hp

    def levelUp(self, amount):
         self.level += amount
    
    def attack(self):
        print("Player attacks")

    def heal(self):
            print("Player heals")

    def walk(self):
         print ("Player walks")

    def takedamage(self, amount):
         self.Hp -= amount

player1 = player(10,10)
player1.levelUp(5)
player1.takedamage(7)
print("Level" ,player1.level)
print(player1.Hp, "Hp")