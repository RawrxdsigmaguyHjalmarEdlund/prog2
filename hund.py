class Hund:
    def __init__(self):
        self.ras = ''
    def existera(self):
        print("Jag existerar voff!")

hund1 = Hund()
hund2 = Hund()

hund1.ras = 'pudel'
hund2.ras = 'chiwawa'

hund1.existera()

print(hund1)