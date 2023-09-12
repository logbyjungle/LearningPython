tizio = ("bello", 69, "ultrabello")
print(tizio.count("bello"))
# dice quante volte compare il "bello"
print(tizio.index("ultrabello"))
# dice quale oggetto è (si parte dallo 0)
for tiz in tizio:
    print(tiz)
if 69 in tizio:
    print("funny number ahah")