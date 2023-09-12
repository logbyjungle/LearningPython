lista = ["gionni","meloni","cpu"]
lista.sort()
# fa in ordine alfabetico
for oggetti in lista:
    print(oggetti)
# oppure

lista2 = ["gionni","meloni","cpu"]
lista_in_ordine = sorted(lista2,reverse=False)
# qua non serviva mettere reverse=False ma è per fare capire che si può invertire l'ordine della lista
# dopo averla organizzata
for altri_oggetti in lista_in_ordine:
    print(altri_oggetti)

lista3 = [("beppe","3"),("andonio","6"),("edoardo","9")]
# si ha fatto una lista accoppiando diversi elementi ovvero nome e voto
voto = lambda voti:voti[1]
# si da al voto valore secondo elemento nelle coppie
lista3.sort(key=voto,reverse=True)
# la lista viene organizzata seguendo il voto, è servito il reverse che se no andava in ordine crescente
for efn in lista3:
    print(efn)
# la lista viene mostrata