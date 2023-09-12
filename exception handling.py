try:
    numeratore = int(input("inserisci numeratore : "))
    denominatore = int(input("inserisci denominatore : "))
    risultato = numeratore / denominatore
    print(risultato)
# problema: se l'utente mette 0 come denominatore il risultato è impossibile e ciò crea un errore, quindi
# si può fare cosi
except Exception:
    print("hai sbagliato qualcosa scemo")