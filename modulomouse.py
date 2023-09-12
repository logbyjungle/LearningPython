class Mouse:
    bottoni = 5
    def __init__(self,cps,bellezza,ergonominità):
        self.cps = cps
        self.bellezza = bellezza
        self.ergonominità = ergonominità
    def clicca(self):
        print("hai cliccato il mouse")
    def lancia(self):
        print("hai lanciato il mouse da " + self.cps + " cps")