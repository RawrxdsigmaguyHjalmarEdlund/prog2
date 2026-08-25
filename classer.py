class person:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = '' 
        self.födelseår = ''
        self.singel = True

class Bankkonto:
    def __init__(self):
        self.kontohavare = ''
        self.saldo = '' 

k = Bankkonto()
k.kontohavare = person() 
k.kontohavare.förnamn = 'Bertil'
