lista_numeros = map(int, input().split())
max = 0
for i in lista_numeros:
    if max < i : max = i
print(max)