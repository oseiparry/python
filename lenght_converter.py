num1=float(input("Enter the value: "))
unit1=input("Enter the unit of the value(mm,cm,m,km); ")
unit2=input("Enter the unit to be converted into(mm,cm,m,km); ")
#mm to other units
if unit1=="mm" and unit2=="cm":
    length=num1/10
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=='mm' and unit2=='m':
    length=num1/1000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=='mm' and unit2=='km':
    length=num1/1000000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

#cm to other units
elif unit1=="cm" and unit2=="m":
    length=num1/100
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="cm" and unit2=="mm":
    length=num1*10
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="cm" and unit2=="km":
    length=num1/100000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')


#m to other units
elif unit1=="m" and unit2=="mm":
    length=num1*1000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="m" and unit2=="cm":
    length=num1*100
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="m" and unit2=="km":
    length=num1/1000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')


#km to other units
elif unit1=="km" and unit2=="m":
    length=num1*1000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="km" and unit2=="mm":
    length=num1*1000000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')

elif unit1=="km" and unit2=="cm":
    length=num1*100000
    print(f'The value of {num1} in {unit2} is {length}{unit2}')