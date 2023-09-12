import random
x = random.randint(1,69)
# ciò da un numero casuale intero
print(x)
# sia 1 che 69 sono inclusi
y = random.random()
# qua il numero può essere anche decimale
print(y)

lista = ['ceco' , 'sordo']
scelta = random.choice(lista)
# prende un elemento casuale
print(scelta)
random.shuffle(lista)
# mischia la lista
print(lista)