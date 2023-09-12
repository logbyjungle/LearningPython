from tkinter import *
# ciò importa tutto da tkinter senza dovere fare tkinter.nomecoso ogni volta ma solo nomecoso
window = Tk()
# crea la finestra
window.geometry("500x500")
# le cambia la dimensione
window.title("finestra")
# da il titolo alla finestra
icona = PhotoImage(file='icona uwu.png')
# imposta l'icona della finestra
window.iconphoto(True,icona)
# abilita l'icona della finestra
window.config(background="red")
# il colore si può mettere anche esadecimale (con #)
# imposta il colore del background della finestra
window.mainloop()
# assolutamente necessario per inizializzare la finestra