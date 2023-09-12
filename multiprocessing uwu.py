# il multiprocessing fa una funzione per ogni cpu core
from multiprocessing import Process, cpu_count
import time

def contando(numero):
    count = 0
    while count < numero:
        count += 1
def main():
    print(cpu_count())
# print(cpu_count()) è dentro a questo per evitare di farlo chiamare ripetute volte
    if cpu_count() == 1:
        processo1 = Process(target=contando, args=(1000000000,))
        processo1.start()
        processo1.join()
    elif cpu_count() == 2:
        processo1 = Process(target=contando, args=(500000000,))
        processo2 = Process(target=contando, args=(500000000,))
        processo1.start()
        processo2.start()
        processo1.join()
        processo2.join()
    elif cpu_count() == 4:
        processo1 = Process(target=contando, args=(250000000,))
        processo2 = Process(target=contando, args=(250000000,))
        processo3 = Process(target=contando, args=(250000000,))
        processo4 = Process(target=contando, args=(250000000,))
        processo1.start()
        processo2.start()
        processo3.start()
        processo4.start()
        processo1.join()
        processo2.join()
        processo3.join()
        processo4.join()
    elif cpu_count() == 8:
        processo1 = Process(target=contando, args=(125000000,))
        processo2 = Process(target=contando, args=(125000000,))
        processo3 = Process(target=contando, args=(125000000,))
        processo4 = Process(target=contando, args=(125000000,))
        processo5 = Process(target=contando, args=(125000000,))
        processo6 = Process(target=contando, args=(125000000,))
        processo7 = Process(target=contando, args=(125000000,))
        processo8 = Process(target=contando, args=(125000000,))
        processo1.start()
        processo2.start()
        processo3.start()
        processo4.start()
        processo5.start()
        processo6.start()
        processo7.start()
        processo8.start()
        processo1.join()
        processo2.join()
        processo3.join()
        processo4.join()
        processo5.join()
        processo6.join()
        processo7.join()
        processo8.join()
    print("ci ha impiegato ", time.perf_counter())
# in questo caso in base al numero di core della cpu il codice distribuisce tra i core il lavoro

if __name__ == '__main__':
    main()
# questo codice è fatto per non creare un errore sui dispositivi windows