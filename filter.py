# filter(funzione,cosicomeliste)
# filtra elementi di cosicomeliste
coppie = [("nani",2),("alti",30),("medi",29)]
numero = lambda cosi:cosi[1] == 30
quelli_che_hanno_30 = filter(numero, coppie)
for trentini in quelli_che_hanno_30:
    print(trentini)