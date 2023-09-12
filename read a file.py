try:
    with open('C:\\Users\\lucam\\Desktop\\ook\\standardoptions.txt') as file:
# questo di default è "with open('percorso\\abdul.txt','r') r sta per read
#
        print(file.read())
except Exception:
    print("il file non è stato aperto")
# l'eccezzione è stata inserita per non bloccare il programma nel caso il file non viene trovato
