# i daemon threads sono dei threads che il programma non aspetta prima di uscire
import time
import threadin

def tempo():
    print()
    print()
# con questi 2 prints faccio andare a capo 2 volte questa funzione in modo da non essere sulla stella linea dell'input
    count = 0
    while 1==1:
        count += 1
        time.sleep(1)
        print(count , " secondo/i")
thread1 = threading.Thread(target=tempo , daemon=True)
# se il thread non fosse daemon continuerebbe anche dopo che l'input fosse inserito
thread1.start()
input = input("inserisci qua qualcosa : ")