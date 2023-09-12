risposte_giuste = 0
def giusto():
    global risposte_giuste
    risposte_giuste = risposte_giuste + 1
risposta1 = input(str("sei scemo? rispondi con si oppure no : "))
if risposta1 == "no":
    giusto()
risposta2 = input(str("minecraft o fortnite? rispondi con 1 oppure 2 : "))
if risposta2 == "1":
    giusto()
risposta3 = input(str("sei vivo? rispondi con si oppure no : "))
if risposta3 == "si":
    giusto()
risposta4 = input(str("hai meno di 2 anni? rispondi con si oppure no : "))
if risposta4 == "no":
    giusto()
print("hai fatto " + str(risposte_giuste) + " risposte giuste")
percentuale_risposte_giuste = risposte_giuste / 4 * 100
print("la percentuale di risposte giuste è del " + str("{:.0f}".format(percentuale_risposte_giuste)) + "%")