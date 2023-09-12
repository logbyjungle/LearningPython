from tkinter import *
finestra = Tk()
# la dimensione della finestra non è necessaria ma diventa quella dell'etichetta
finestra.title("finestra")
icona = PhotoImage(file='icona uwu.png')
finestra.iconphoto(True,icona)
immagine = PhotoImage(file='icona uwu.png')
etichetta = Label(finestra,text="dio brando",
                  font=('Arial',30,'bold'),
# font, dimensione font, tipo font
                  fg='orange',
# colore testo
                  bg='black',
# colore background
                  bd=10,
# dimensione bordo
                  relief=RAISED,
# tipo bordo
                  padx=10,
# distanza bordo testo x
                  pady=10,
# distanza bordo testo y
                  image=immagine,
# mette un immagine
                  compound='bottom')
# fa si che l'immagine non ricopra il testo riposizionandola
etichetta.pack()
# .pack() la posizione al centro in alto mentre .place(x=numero,y=numero)

finestra.mainloop()