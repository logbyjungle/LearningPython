x = 2.0 #float
print(int(x))
# ciò mostra x come numero intero anziche decimale
#però per cambiare x da decimale a intero si deve fare
x = int(x)
# e di conseguenza
print(x)
# x è intero, si può però ricambiare
x = float(x)
print(x)
y = "3" #string
print(y*3)
# y*3 ha fatto 333 anziche 9 perchè bisogna convertirlo come numero
y = int(y)
print(y*3)