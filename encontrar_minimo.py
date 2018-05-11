import math

lista_numeros = map(int, input().split())
min = math.inf
for i in lista_numeros:
    if min > i : min = i
print(min)