def salve(**kwargs):
# usare la parola kwargs non è veramente obbligatorio ma è molto comune come utilizzo
    print("ciao" + kwargs['primo_nome'] + kwargs['secondo_nome'] + kwargs['cognome'])
salve(primo_nome="giuseppino",secondo_nome="antonino",cognome="gianpeppino")
# questo funziona solo se li si dà tutti e tre
def buonsalve(**abdullino):
# crea la funzione buonsalve che funziona attraverso kwargs
    print("ciao", end="")
# scrive ciao
    for key,value in abdullino.items():
        print(value, end="")
# scrive ogni valore inserito
buonsalve(primo_nome="giuseppino",cognome="gianpeppino")