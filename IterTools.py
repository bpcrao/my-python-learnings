from itertools import accumulate, takewhile

lista = list(accumulate(range(10)))
print(lista)

print(list(takewhile(lambda x: x < 10, lista)))