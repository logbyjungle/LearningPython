# per impedire all'utente di creare oggetti di classi non intese per creare oggetti si può
# fare cosi in modo da creare un errore

from abc import ABC, abstractmethod

class classe_in_cui_non_si_deve_creare_oggetti(ABC):
    @abstractmethod
    def gigi(self):
        pass
# tutte le classi che sono derivate da una classe astratta devono fare l'override in questo caso della funzione
class classe1(classe_in_cui_non_si_deve_creare_oggetti):
    def gigi(self):
        print("gigi1")
class classe2(classe_in_cui_non_si_deve_creare_oggetti):
    def gigi(self):
        print("gigi2")
oggettochedaerrore = classe_in_cui_non_si_deve_creare_oggetti()
print(oggettochedaerrore.gigi())