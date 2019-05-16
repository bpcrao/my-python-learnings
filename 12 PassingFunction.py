def add(a,b):
    return a+b

def doubles (func,  a, b):
    return func(func(a, b), b)


print(doubles(add, 10, 11))