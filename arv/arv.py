class Fordon:
    def __init__(self, reg = '', fordonstyp = ''):
        self.reg = reg
        self.fordonstyp = fordonstyp

class Lastbil(Fordon):
    def __init__(self, reg='', fordonstyp='', maxvikt = 0):
        maxvikt = maxvikt 
        super().__init__(reg, fordonstyp)

    def honk(self):
        print("Hooooooooonk!")

class Motorcykel(Fordon):
    def __init__(self, reg='', fordonstyp ='', senastBesiktigad = 0):
        senastBesiktigad = senastBesiktigad
        super().__init__(reg, fordonstyp)

    def whelie(self):
        print("whellie brum brum")

f1 = Motorcykel("Motorcykel", "Abc123", 2022)
f2 = Lastbil ("Lastbil", "dsa456", 1000)

print(vars(f1))