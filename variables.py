print("text printed")
# text printed è una stringa (str)

name = "zoro"
print(name)
print(name + "ciao")

metà1 = "melone"
metà2 = "prosciutto"
intero =metà1 + " " + metà2
print(intero)

numero = 1
numero = numero + 1
print(numero)
print(type(numero))
# numero è un numero intero (int)
# quindi non puoi fare print("ciao"+numero) in quanto sono uno stringa e l'altro numero intero
# si può però convertire il numero intero facendo print("ciao"+str(numero))
# per capire di che tipo è un qualcosa basta fare print(type(numero)) numero in questo caso è ciò che non si sa
# di che tipo è
print("ciao"+ " " +str(numero))

numero_decimale= 0.5
# 0.5 è un numero decimale (float)

vivo = True
print(vivo)
# vivo è booleano (bool)

