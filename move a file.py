import os
partenza = "testo.txt"
arrivo = "C:\\Users\\lucam\\PycharmProjects\\learningpython\\cartella per robe\\testo mosso.txt"
try:
    os.replace(partenza,arrivo)
    print("file mosso")
except Exception:
    print("qualcosa è andato storto")
# ricordo che oltre ad essere un file può anche essere una cartella e altre cose