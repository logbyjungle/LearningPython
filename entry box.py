from tkinter import *
finestra = Tk()
def invia():
    coso = la_entry_box.get()
    print(coso)
la_entry_box = Entry(finestra,
                     font=("Arial",20))
la_entry_box.insert(0,"scrivi qua")
la_entry_box.pack()
invio = Button(finestra,
               command=invia,
               text="inviaaa",
               font=("Arial",20))
invio.pack()






finestra.mainloop()