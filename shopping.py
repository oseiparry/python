product=input('Enter the name of your product; ')
quantity=float(input(f'Enter the number of {product} you want to buy; '))
price=float(input(f'Enter tht price of {product} '))
total=quantity*price
print(f'Your total cost of {product} is ${total}')