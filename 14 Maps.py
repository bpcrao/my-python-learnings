def add(x):
    return x+2


newList = [1, 2, 3, 4, 5]

print(list(map(add,newList)))

print(list(filter(lambda x: x%2 == 0, newList)))