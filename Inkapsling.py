class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.__ålder = ålder

    def get_ålder(self):
        return self.__ålder
    def set_ålder(self, nyÅlder):
        self.__ålder = nyÅlder
        
person = Person("Anna", 25)

print(person.namn)
print(person.get_ålder())

person.namn = "Erik"
person.ålder = 40

print(person.namn)
print(person.ålder)

class Bil:
    def __init__(bil, ägare = '', reg = '', hastighet = 0):
        bil.ägare = ägare
        bil.__reg = reg
        bil.hastighet = hastighet

    def get_reg(self):
            return self.__reg

    def set_ålder(self, nyreg):
            self.__reg = nyreg

Bil = Bil("Anna", "crazy", 1000)

print(Bil.ägare)
print(Bil.get_reg())
print(Bil.hastighet)

Bil.ägare = "Erik"
Bil.reg = 69420
Bil.hastighet = 10000

print(Bil.ägare)
print(Bil.reg)

class bankkonto:
    def __init__(self, namn, saldo):
        self.namn = namn
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, nySaldo):
        self.__saldo = nySaldo
    