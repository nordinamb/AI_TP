n = int(input("saisir un nombre  "))
s= 0
for i in range(0,n+1):
    s+= 10**i
print ("le nombre est ",s)