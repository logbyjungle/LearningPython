età = int(input("inserisci la tua età : "))
if età == 69:
    print("sei un dio")
# prima possibilità, i controlli avvengono in ordine, il simbolo dell' uguale è un doppio uguale
elif età >= 8:
    print("hai piu di, o 8 anni, hai "+ str(età))
elif età < 0:
    print("non sei ancora nato")
# elif vuol dire else if , quindi è un altra opzione
else:
    print("hai meno di 8 anni, ne hai " + str(età))
# ultima risorsa nel caso tutto quanto è negativo
