p = input("enter a number")
n = input("enter a number")
r = input("enter rate of interest")



p = int(p)
n = int(n)
r = int(r)

if (r > 10) :
    print("too much intrest")

print ((p*n*r)/100)