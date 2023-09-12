# reduce() usa una funzione su una lista o robe del genere fino a quando non rimane un solo elemento
import functools
lettere = ["c","i","a","o"]
parola = functools.reduce(lambda x,y : x + y, lettere)
print(parola)