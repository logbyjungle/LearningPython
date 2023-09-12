def rumoroso(testo):
    return testo.upper()
def silezioso(testo):
    return testo.lower()
def ciao(funz):
    testo = funz("abdullino")
    print(testo)

ciao(rumoroso)
# ciao(funz) in questo caso funz + rumoroso quindi testo = rumoroso("abdullino")

def divisore(divisor3):
    def dividendo(dividend0):
        return dividend0 / divisor3
    return dividendo

divisione = divisore(2)
print(divisione(4))

# in questo caso avviene print(divisore(2)(4))