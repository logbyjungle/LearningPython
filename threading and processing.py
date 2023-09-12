import threading
# multithreading = diversi thread vengono eseguiti, ne può funzionare uno solo alla volta, meglio per
# programmi che richiedono input dall'utente
# moltiprocessing = diversi thread vengono eseguiti, possono funzionare insieme

import time
def cosa_da_fare_1():
    time.sleep(1)
    print("hai fatto la prima cosa")
def cosa_da_fare_2():
    time.sleep(2)
    print("hai fatto la seconda cosa")
def cosa_da_fare_3():
    time.sleep(3)
    print("hai fatto la terza cosa")
# cosa_da_fare_1()
# cosa_da_fare_2()
# cosa_da_fare_3()
# tutto questo impiega un totale di 6(1+2+3) secondi, con piu threads ci si può impiegare di meno
print(threading.active_count())
# questo mostra quanti thread attivi si ha
print(threading.enumerate())
# mostra che thread si ha attivi

thread1 = threading.Thread(target=cosa_da_fare_1)
# crea un thread con obiettivo cosa_da_fare_1
thread1.start()
# avvia il thread
thread2 = threading.Thread(target=cosa_da_fare_2)
thread2.start()
thread3 = threading.Thread(target=cosa_da_fare_3)
thread3.start()

print(threading.active_count())
print(threading.enumerate())
# come si può notare tutto ciò ha impiegato solo 3 secondi, l'avvio del thread attiva la funzione corrispondente

# per forzare il thread principale ad aspettare gli altri thread si può fare thread1.join() quindi, il thread
# principale si bloccherà a quel punto fino a quando il thread selezionato non finirà di svolgere la sua funzione

