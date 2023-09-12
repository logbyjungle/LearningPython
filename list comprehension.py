lista = [1,45,12]
lista_modificata = list(filter(lambda x: x == 1, lista))
# viene definita la lista modificata, ovvero gli elementi della lista equivalenti a 1
# il modo lento invece è

# lista_modificata = []
#for obj in lista:
#    if obj == 1:
#        lista_modificata.append(obj)
#    else:
#        pass
print(lista_modificata)