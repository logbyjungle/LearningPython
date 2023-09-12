# break termina il loop
# continue passa al loop successivo
# pass non fa nulla
while 1==1:
    parola = input("inserisci la parola : ")
    if len(parola) > 0:
        break
# questo codice fa si che viene eseguito fino a quando la parola non viene inserita

parola_e_numeri = "a1a1a1a1"
for pen in parola_e_numeri:
    if pen == "1":
        continue
    print(pen ,end="")
# quando il carattere pen era uguale ad 1 ha continuato senza eseguire il comando del loop
# ,end="" è stato utilizzato per non scrivere tutto quanto andando a capo ogni volta
# si può realizzare uguale usando pass
print()
for pen in parola_e_numeri:
    if pen =="1":
        pass
    else:
        print(pen ,end="")
# qua il print() l'ho utilizzato solo per andare a capo