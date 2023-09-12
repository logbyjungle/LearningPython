robe = ["orsi","cavalli","cartone"]
print(robe)
# robe ora ha diversi oggetti contenuti in se stesso in quanto è una lista ora
print(robe[0])
# ciò prende l'elemento 0 della lista, in questo caso "orsi"
robe[0] = "aereo"
print(robe[0])
# si può rimpiazzare un elemento come appena dimostrato
# per elecncare tutti gli elementi si può fare cosi
for rob3 in robe:
    print(rob3 + " ", end="")
# in questo caso rob3 non è piu per i caratteri ma per elementi della lista
robe.append("marte")
# aggiunge un elemento alla lista
robe.remove("aereo")
# rimuove un elemento alla lista
print()
for rob3 in robe:
    print(rob3 + " ", end="")
robe.pop()
# pop rimuove l'ultimo elemento della lista
print()
for rob3 in robe:
    print(rob3 + " ", end="")
robe.insert(0,"lampadario")
# ciò aggiunge alla posizione 0 un oggetto anziche a quello finale
print()
for rob3 in robe:
    print(rob3 + " ", end="")
robe.sort()
# organizza la lista alfabeticamente
print()
for rob3 in robe:
    print(rob3 + " ", end="")
robe.clear()
# elemina ogni elemento dalla lista
print()
for rob3 in robe:
    print(rob3 + " ", end="")