import math
class Författare:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = ''

class Bok:
    def __init__(self):
        self.Titel = ''
        self.författare = None

bok =Bok()
bok.titel = 'One piece'
bok.författre = Författare()



class Cirkel:
    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r

    def set_r(self, r):
        assert r >=0
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def omkr(self):
        return 2 * math.pi * self.r

cirkel = Cirkel()
input = float(input("Vad är cirkelns radie "))

cirkel.set_r(input)

print("Area: ", cirkel.area())

