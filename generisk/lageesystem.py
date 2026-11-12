from typing import TypeVar, Generic #Klassvariabel
T = TypeVar('T') #Klassvariabel

class Lager(Generic[T]): #Klassvariabel
    total_objects: int = 0 #Lokal

    def __init__(self, value: T): #Instansvariabler
        self.value: T = value #Lokal
        Lager.total_objects += 1 #Lokal

    def get_value(self) -> T: #Instansvariabler
        return self.value #Lokal

    def yttrefunktion(self) -> T: #Instansvariabler
        yttre_value = self.value #Lokal

        def inrefunction() -> T: #Lokal
            return yttre_value #Lokal

        return inrefunction() #Lokal



#1. Vad är skillnaden i livslängd mellan en klassvariabel och en lokal variabel i en metod? När dör de respektive?
# En klassvariabel lever från start av program och lever så länge programet körs medans en lokalvariabel börjar leva när den anropas och där när den returnas.
#2 Varför kan inte den inre (nästlade) funktionen nå variabler som skapats inuti en helt annan metod i samma klass? (Koppla till LEGB).
#En lokal variabel i en metod är isolerad den kan bara se saker i sin egna variabel. För att den är lokal så efter den har körts så radderas det från minnet vilket gör det omöjligt att komma åt andra metoder.