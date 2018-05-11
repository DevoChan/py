import sys
sys.setrecursionlimit(2002)

def numero_elementos (tamano):
    if tamano == 1: return 1
    return tamano * tamano + numero_elementos(tamano-1)

tamano = int(input("Write the piramid size: "))
print(numero_elementos(tamano))
