persona = "giggino"
oggetto = "un microonde"
print("{} ha ucciso {}".format(persona,oggetto))
print("{1} ha ucciso {0}".format(persona,oggetto))
# cambia l'ordine, parte da 0 il conteggio
print("{persona} ha ucciso {oggetto}".format(persona="giggino",oggetto="un microonde"))
# questo invece definisce quale bisogna inserire
testo = "{} ha ucciso {}"
print(testo.format(oggetto,persona))
print("salve {:20} ,come ti chiami?".format(persona))
# {:10} imposta 10 caratteri di spazio dopo la parola
# ma si può fare anche diversamente come cosi
print("salve {:^20} ,come ti chiami?".format(persona))
# questo centra il termine che lascia lo spazio
print("salve {:>20} ,come ti chiami?".format(persona))
# questo lascia lo spazio prima del termine
# queste cose possono essere comode pure per i numeri
numero = 100000
print("{:.3f}".format(numero))
# questo ad esempio mostra 3 numeri dopo il punto
print("{:,}".format(numero))
# questo aggiunge una virgola per ogni migliaia
print("{:b}".format(numero))
# questo mostra il numero in binario
print("{:x}".format(numero))
# questo invece è esadecimale