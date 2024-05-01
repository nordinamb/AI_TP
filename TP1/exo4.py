
age =  int(input("saisir votre âge "))
sex = input("saisir votre sex soit F ou M ")
while sex !="F" and sex !="M" :
    sex = input("saisir votre sex soit F ou M ")
if sex == "F" and age >= 18 :
    print("vous payer les impôts")
elif sex =="M" and age>=20 :
    print("vous payer les impôts")
else:
    print("pas d impôts")
    
