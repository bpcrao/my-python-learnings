def evennumbers(limit):
    for i in range(limit):
        if(i%2==0):
            yield i

#print even nummbers

for ii in evennumbers(100):
    print (ii)