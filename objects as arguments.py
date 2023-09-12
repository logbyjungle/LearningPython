class tizio:
    intelligenza = None
# crea la classe tizio che imposta l'intelligenza di default a None
def cambia_intelligenza(persona,intelligenza):
    persona.intelligenza = intelligenza
# crea la funzione cambia_intelligenza che permette di cambiare l'intelligenza
persona1 = tizio()
# crea l'oggetto persona1 legato alla classe tizio()
cambia_intelligenza(persona1,"poca")
# viene utilizzata la funzione
print(persona1.intelligenza)
# viene mostrato il risultato