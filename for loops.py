# un while loop esegue il codice un numero infinito di volte mentre il for loop lo fa un numero di volte limitato
for abdul in range(10):
    print(abdul)
# cosa è successo? il codice conta i caratteri (abdul) da 0 a 9 poichè (10) vale come (0,10,1) ma tenendo conto che
# il primo valore è incluso mentre il secondo è escluso
for parola in "parolaaa":
    print(parola)
# si può creare un countdown con tutto questo si deve però importare il tempo per creare un attesa

import time

for tempo in range (10,0,-1):
    print(tempo)
    time.sleep(1)
print("countdown finito")
# time.sleep ferma il codice per in questo caso un secondo