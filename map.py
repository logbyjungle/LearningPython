# map() applica una funziona a una lista/tuple/altro
# map(funzione, lista)
coppie = [("nani",2),("alti",30),("medi",29)]
# crea un dizionario
moltiplica_per_20 = lambda cosi: (cosi[0],cosi[1]*20)
# crea la funzione moltiplica_per_20 utilizzando lambda
coppie_moltiplicate_per_20 = map(moltiplica_per_20, coppie)
for cosi in coppie_moltiplicate_per_20:
    print(cosi)