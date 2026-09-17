class Djur:
    def __init__(self, namn, ålder):
        namn = namn
        ålder = ålder

class Apa(Djur):
    def låta(self):
        print("Oa oa")

class Björn(Djur):
    def låta(self):
        print("rawr")

class Skunk(Djur):
    def låta(self):
        print("Skunk skunk")

DjurLista = [
    Skunk(),
    Apa(),
    Björn()
]

for djur in DjurLista:
    djur.låta()