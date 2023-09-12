# slicing = [start:stop:step]
nome = "Giovanni Giorgio"
primo_carattere = nome[0]
print(primo_carattere)
prima_parola = nome[0:8] # si può scrivere anche nome[:3]
print(prima_parola)
# è giovanni anziche giovann perchè il carattere di stop esclude quel carattere mentre quello d'inizio lo include
ultima_parola = nome[9:]
print(ultima_parola)
# step fa contare i caratteri ogni numero impostato di step, default è 1
nome_strano = nome[::2]
print(nome_strano)
nome_al_contrario = nome[::-1]
print(nome_al_contrario)

sito = "www.google.com"
nome_sito = slice(4,-4)
print(sito[nome_sito])
# questo modo di tagliare è utile in quanto si possono usare i numeri negativi dei caratteri per partire dalla fine
# ma bisogna tenere conto che parte dall'1 e non dallo 0 coi caratteri


