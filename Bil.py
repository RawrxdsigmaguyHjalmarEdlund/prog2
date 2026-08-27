import copy

class Bil:
    def __init__(bil, ägare = '', reg = '', fabrikat = '', årsmodell = '', tjänstevikt = '', motoreffekt = ''):
        bil.ägare = ägare
        bil.reg = reg
        bil.fabrikat = fabrikat
        bil.årsmodell = årsmodell
        bil.tjänstevikt = tjänstevikt
        bil.motoreffekt = motoreffekt

class person:
    def __init__(self, förnamn = '', eftarnamn = '', födelseår = '', singel = True):
        self.förnamn = förnamn
        self.efternamn = eftarnamn
        self.födelseår = födelseår
        self.singel = singel


bil1 = Bil(person(), 'CMZ45X', 'BMW', '2022', '1925 kg', '183 Hk')

bil1.ägare.förnamn = 'Robin'

bil2 = Bil(person(), 'TUL37L', 'Audi', '2020', '1930 kg', '204 Hk')

bil2.ägare.förnamn = 'Bobin'

print ('Bil 1')
print (bil1.ägare.förnamn , bil1.reg, bil1.fabrikat, bil1.årsmodell, bil1.tjänstevikt, bil1.motoreffekt)
print ('-------------------------------')
print ('Bil 2')
print (bil2.ägare.förnamn , bil2.reg, bil2.fabrikat, bil2.årsmodell, bil2.tjänstevikt, bil2.motoreffekt)