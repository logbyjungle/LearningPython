import time
# time.ctime converte il tempo alla data riferita al secondo, ovvero riferendosi a quando il tempo è "iniziato"
print(time.ctime(0))
print(time.time()) # quanti secondi sono passati dal momento di inizio del tempo
print(time.ctime(time.time())) # converte i secondi in data mostrando quindi che data è oggi
print(time.localtime()) # scrive che tempo è completamente