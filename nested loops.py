file = int(input(" quante file? : "))
colonne = int(input(" quante colonne? : "))
simbolo = input(" che simbolo vuoi usare? : ")

for fil3 in range(file):
    for colonn3 in range(colonne):
        print(simbolo, end="")
    print()
# ciò crea un rettangolo utilizzando 2 loops
# il primo loop determina quante volte viene eseguito il codice delle colonne per fila
# il print ha ,end="" per evitare di andare a capo ad ogni simbolo
# per andare a capo quando lo si desidera invece si usa print() che in quanto privo dell' end="" fa andare a capo
