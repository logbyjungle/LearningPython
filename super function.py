class due_o_piu_dimensioni:
    def __init__(self,larghezza,lunghezza):
        self.larghezza = larghezza
        self.lunghezza = lunghezza
class dueD(due_o_piu_dimensioni):
    def __init__(self,larghezza,lunghezza):
        super().__init__(larghezza,lunghezza)
class treD(due_o_piu_dimensioni):
    def __init__(self,larghezza,lunghezza,altezza):
        super().__init__(larghezza,lunghezza)
        self.altezza = altezza
    def volume(self):
        return(self.larghezza*self.lunghezza*self.altezza)

cubo = treD(6,6,6)
print(cubo.volume())