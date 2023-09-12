import os
percorso = 'testo.txt'
try:
    os.remove(percorso)
# questo elimina solo files
    print("il file è stato eliminato")
except Exception:
    print("qualcosa è andato storto")