import math
a =int  (input("saisi le premier order ") )
b =int  (input("saisi le deuxiemme order ") )
c =int  (input("saisi le troisieme order ") )
def  equation (a,b,c) :
    delta = b**2  -4*a*c 
    jdelta = math.sqrt(delta)
    if delta > 0 :
        print('x1 :'+str((-b+jdelta)/2*a ))      
        print('x1 :'+str((-b-jdelta)/2*a ))  
        
    elif delta == 0 :
        print('x1 :'+str((0-b)/2*a ))
        
equation(a,b,c)