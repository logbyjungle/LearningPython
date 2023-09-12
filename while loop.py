parola = ""
while len(parola) == 0:
    parola = input("inserisci una parola : ")
print("ciao la parola che hai scelto è " + parola)
# inanzitutto si da alla parola valore di lunghezza 0
# dopodiche si fa che quando la parola ha lunghezza 0
# viene eseguito un codiche che in questo caso chiede di riformulare la parola
# e alla fine quanto l'utente inserisce una parola lunga piu di 0 viene eseguito il codice finale
# un altro modo in coi si può scrivere è
parola2 = None
while not parola2:
    parola2 = input("inserisci un altra parola : ")
print("la seconda parola che hai scelto è " + parola2)
# funziona diversamente, si utilizza il None ovvero non si da valore alla parola2
# e while not parola2 fa si che quando non si ha la parola 2 il codice viene eseguito