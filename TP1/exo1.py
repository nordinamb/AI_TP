a =int  (input("saisi le premier order ") )
b =int  (input("saisi le deuxiemme order ") )
c =int  (input("saisi le troisieme order ") )
while a<=20 and c<=20 and b<=20 :
    a =int  (input("saisi le premier order ") )
    b =int  (input("saisi le deuxiemme order ") )
    c =int  (input("saisi le troisieme order ") )
def avg(x ,y ,z ) :
 
     return ( x + y + z )/ 3
m = avg(a,b,c)
print(m )
if m >= 10 and m<=12 :
    print('passable')
elif m > 12 and m<=14 :
    print('assez bien ')
