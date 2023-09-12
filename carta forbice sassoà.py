import random
scelta = input(str("scrivi qui carta o forbice o sasso : "))
if scelta != "carta" and scelta != "forbice" and scelta != "sasso":
    print("noob")
scelta_avversario = random.randint(1,3)
scelta_avversario = str(scelta_avversario)
if scelta_avversario == "1":
    scelta_avversario = "carta"
elif scelta_avversario == "2":
    scelta_avversario = "forbice"
else:
    scelta_avversario = "sasso"
if scelta == scelta_avversario:
    print("pareggio")
if scelta == "carta" and scelta_avversario == "forbice":
    print("hai perso")
elif scelta == "carta" and scelta_avversario == "sasso":
    print("hai vinto")
elif scelta == "forbice" and scelta_avversario == "carta":
    print("hai vinto")
elif scelta == "forbice" and scelta_avversario == "sasso":
    print("hai perso")
elif scelta == "sasso" and scelta_avversario == "forbice":
    print("hai vinto")
elif scelta == "sasso" and scelta_avversario == "carta":
    print("hai perso")