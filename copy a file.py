import shutil
# copyfile() copia il contenuto del file
# copy() fa copyfile() e modalità permesso e la destinazione può essere una directory
# copy2() fa copy() e copia la data di creazione del file e l'ora di modifica
try:
    shutil.copyfile('testo.txt', 'copia di testo.txt')
except Exception:
    print("qualcosa è andato storto")