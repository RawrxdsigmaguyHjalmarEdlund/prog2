import copy

class Bil:
    def __init__(bil):
        bil.ägare = ''
        bil.reg = ''
        bil.fabrikat = ''
        bil.årsmodell = ''
        bil.tjänstevikt = ''
        bil.motoreffekt = ''

class person:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = '' 
        self.födelseår = ''
        self.singel = True


bil1 = Bil()
bil1.ägare = person()
bil1.ägare.förnamn = 'Robin'
bil1.reg = 'CMZ45X'
bil1.fabrikat = 'BMW'
bil1.årsmodell ='2022'
bil1.tjänstevikt = '1 925 kg'
bil1.motoreffekt = '183 Hk'

bil2 = Bil()
bil2.ägare = person()
bil2.ägare.förnamn = 'Bobin'
bil2.reg = 'TUL37L'
bil2.fabrikat = 'Audi'
bil2.årsmodell ='2020'
bil2.tjänstevikt = '1 930 kg.'
bil2.motoreffekt = '204 Hk'



print ('Bil 1')
print (bil1.ägare.förnamn , bil1.reg, bil1.fabrikat, bil1.årsmodell, bil1.tjänstevikt, bil1.motoreffekt)
print ('-------------------------------')
print ('Bil 2')
print (bil2.ägare.förnamn , bil2.reg, bil2.fabrikat, bil2.årsmodell, bil2.tjänstevikt, bil2.motoreffekt)