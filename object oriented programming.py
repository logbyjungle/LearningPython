from modulomouse import Mouse
mouse1 = Mouse("20","cosi cosi","ma si dai è comodo")
print(mouse1.ergonominità)
mouse1.lancia()
print(mouse1.bottoni)
Mouse.bottoni = 20
print(mouse1.bottoni)