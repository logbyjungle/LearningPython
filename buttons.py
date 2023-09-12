from tkinter import *
finestra = Tk()
def abdullino():
    print("abdullino ti osserva")
bottone = Button(finestra,
                 text="abdul",
                 command=abdullino,
# definisce il comando del bottone
                 activeforeground='green',
                 activebackground='blue')
# cambia come diventa il bottone da cliccato, si può cambiare il testo come è fatto allo stesso modo delle etichette
# si possono anche mettere immagini come alle etichette
bottone.pack()
# ancora una volta pack è necessario per attivare il bottone
finestra.mainloop()