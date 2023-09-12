def addizione(*robe):
# crea la funziona addizione che funziona usando *robe
    totale = 0
# si imposta il totale a 0
    for cosi in robe:
        totale += cosi
    return totale
# si aggiunge ognuno dei cosi al totale
print(addizione(1,2,3,4,5))