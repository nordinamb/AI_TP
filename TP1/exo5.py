num1 = int(input("saisir le premier nombre  "))
num2 = int(input("saisir le premier nombre  "))
operation = input("saisir une opération soit * / + -    ")
if operation =="+" :
    print(num1+num2)
elif operation =="-" : 
    print(num1-num2)
elif operation == "/" :
    print(num1/num2)
else :
   print(num1*num2)