iq = int(input("il tuo iq è : "))
if iq >= 80 and iq <= 120:
    print("il tuo iq è nella media")
elif iq < 80 or iq > 120:
    print("il tuo iq non è nella media")
# oltre a and e or c'è anche not che funziona un po' diversamente, infatti se la risposta è vera diventa falsa

iq2 = int(input("il tuo iq è : "))
if not(iq2 >= 80 and iq <= 120):
    print("il tuo iq è nella media")
elif not(iq < 80 or iq > 120):
    print("il tuo iq non è nella media")
# come si può notare ha invertito la risposta da falsa a vera