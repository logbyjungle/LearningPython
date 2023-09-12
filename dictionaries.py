personaggi = {'one piece':'zoro',
              'naruto':'sasuke'}
# andare a capo non serve ma mostra bene le cose a coppie
print(personaggi)
print(personaggi['one piece'])
print(personaggi.get('bleach'))
# .get mostra se esiste o no nel dizionario
print(personaggi.keys())
print(personaggi.values())
personaggi.update({'seven deadly sins':'meliodas'})
personaggi.update({'one piece':'katakuri'})
print(personaggi)
personaggi.pop('naruto')
print(personaggi)
personaggi.clear()
print(personaggi)