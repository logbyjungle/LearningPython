set1 = {"val1","val2","val3","val3"}
set2 = {"Val1","Val2","Val3"}
set3 = set1.union(set2)
# unione crea un set con elementi di entrambi
for sets in set1:
    print(sets + " ", end="")
# come si può vedere i sets non ammettono duplicati
print()
set1.add("val4")
for sets in set1:
    print(sets + " ", end="")
print()
set1.remove("val1")
for sets in set1:
    print(sets + " ", end="")
set1.update(set2)
# update aggiiunge tutti gli elementi di un set ad un altro
print()
for sets in set1:
    print(sets + " ", end="")
print()
for sets in set3:
    print(sets + " ", end="")
# non è cambiato nulla tra set3 e set1 poichè set3 è set1 + set2 ma set1 è set1 + set2 e i set non ammettono duplicati
print()
print(set3.difference(set2))
# ciò mostra ciò che il set3 ha che il set2 non ha
print()
print(set3.intersection(set2))
# ciò mostra gli elementi che entrambi i set anno in comune