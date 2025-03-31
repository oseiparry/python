tempvalue=float(input("Enter the value of your temperature; "))
tempunit=input("Enter the unit of the temperature(K/C); ")
if tempunit=="C":
    temp=(tempvalue+273)
    print(f"Your temperature in Kelvin is {temp}K ")
elif tempunit=="K":
    temp=(tempvalue-273)
    print(f"Your temperature Celcius is {temp}C")
else:
    print("You have entered an invalid unit")
