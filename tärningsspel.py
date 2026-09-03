import random

class Spelare:
        def __init__(self, namn = '', poäng = 0):
            self.namn = namn
            self.poäng = poäng

        def kasta(self):
            return (random.randint(1,6))

def vinn_runda():
    global resultat1, resultat2, spelare1, spelare2

    if resultat1 > resultat2:
        print(spelare1.namn, 'rullade:', resultat1)
        print(spelare2.namn, 'rullade:', resultat2)
        print (spelare1.namn, 'vann!!!')
        spelare1.poäng += 1
        print(spelare1.namn,':', spelare1.poäng,' poäng')
        print(spelare2.namn,':',spelare2.poäng,' poäng')
    elif resultat2 > resultat1:
        print (spelare2.namn, 'vann!!!')
        spelare2.poäng += 1
        print(spelare1.namn,':', spelare1.poäng,' poäng')
        print(spelare2.namn,':',spelare2.poäng,' poäng')
    else:
        print ('Det blev lika')
        print(spelare1.namn,':', spelare1.poäng,' poäng')
        print(spelare2.namn,':',spelare2.poäng,' poäng')

spelare1 = Spelare("Anna")
spelare2 = Spelare("Erik")

while True:
    resultat1 = spelare1.kasta()
    resultat2 = spelare2.kasta()
    if spelare1.poäng == 5:
        print(spelare1.namn, 'vann hela spelet!!!!!!!!!')
        break
    if spelare2.poäng == 5:
        print(spelare2.namn, 'vann hela spelet!!!!!!!!!')
        break
    vinn_runda()
