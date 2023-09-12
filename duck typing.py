class anguria:
# ricorda che nelle classi scrivere anguria oppure anguria() è uguale se il contenuto delle parentesi è vuoto
    def rompersi(self):
        print("l'anguria si è rotta")
    def evolversi(self):
        print("l'anguria si è evoluta")
class pikachu:
    def rompersi(self):
        print("il pikachu si è rotto")
    def evolversi(self):
        print("il pikachu si è evoluto")
class umano:
    def picchiare(self, anguria):
        anguria.rompersi()
        anguria.evolversi()
        print("hai picchiato fino alla morte l'obiettivo")
Anguria = anguria()
Pikachu = pikachu()
Umano = umano()

Umano.picchiare(Pikachu)
Umano.picchiare(Anguria)

# se hanno gli stessi metodi o attributi, in questo caso rompersi ed evolversi quindi si, anguria e pikachu possono
# venire scambiati