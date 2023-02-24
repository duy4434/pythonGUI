weight = float(input("weight(kg):  "))
height = float(input("height (m):" ))
bmi = weight / height **2
result = " "
if  bmi < 18.5 :
    result = "Underwweight"
elif bmi >= 18.5 and bmi < 25 :
    result = "Nolmal weight"
elif bmi >= 25 and bmi < 30 :
    result = "Overweight"
else :
    result = "Obesity"
print ("BMI is %.1f"%bmi)
print (result)