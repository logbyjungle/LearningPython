# zip(lista/tuple/dizionario/...) unisce gli elementi dai diversi gruppi creando un oggetto zip
tipo = ["bravo","cattivo","normale"]
# crea questo gruppo
abilità = ["plot armor", "flashback" , "muore"]
# crea quest'altro gruppo
insieme = dict(zip(tipo, abilità))
# crea un dizionario composto dallo zip dei 2 gruppi
for key,value in insieme.items():
    print(key + ": " + value)
# fa il print() del dizionario