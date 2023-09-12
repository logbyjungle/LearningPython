contenuto = "abdul\nessere\nabdul"
contenuto2= "\nquesto essere stato inserito successivamente nel file"
# \n fa andare a capo
try:
    with open('testo.txt', 'w') as file:
        file.write(contenuto)
    with open('testo.txt', 'a') as file:
        file.write(contenuto2)
    with open('testo.txt', 'r') as file:
        print(file.read())
except Exception:
    print("qualcosa è andato storto")