parola = "ciao tonNo"
parola_senza_spazio = "ciaotonNo"
print(len(parola))
# len sta per lenght ovvero lunghezza
print(parola.find("c"))
# .find ha trovato in quale carattere della parola si trova la prima lettera c
print(parola.capitalize())
# .capitalize mette in maiuscolo sola la prima lettera
print(parola.upper())
# invece .upper mette tutte le parole in maiuscolo
print(parola.lower())
# .lower mette tutte le parole in lettere minuscole
print(parola.isdigit())
# .isdigit può avere valore vero o falso se la parola è numero o no
print(parola.isalpha())
# .isalpha fa come isdigit ma per le lettere (carattere alfabetico)
# in questo caso è falso poichè lo spazio non è un carattere alfabetico
print(parola_senza_spazio.isalpha())
print(parola.count("o"))
# .count conta quanti caratteri specifici sono presenti nella stringa
print(parola.replace("o","1"))
# .replace rimpiazza un carattere con un altro
print(parola*2)
# mostra la stringa parola 2 volte tutto attaccato
