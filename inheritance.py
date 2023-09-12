class corpi_celesti:
    grandi = True
    def abdul(self):
        print("abdul è stato qua")
class stelle(corpi_celesti):
    luminose = True
print(corpi_celesti.grandi)
print(stelle.luminose)
stelle = stelle() # questo è necessario per fare funzionare stelle.abdul()
stelle.abdul()

class pollo:
    pass
class cellula(pollo):
    pass
class atomo(cellula):
    pass

class scemo:
    pass
class intelligente:
    pass
class tizio(scemo,intelligente):
    pass
