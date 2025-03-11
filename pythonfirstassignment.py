#Python to request 2 figures from user and the operand to add two numbers

""" Features
- Request first number input from user
- Request second number input from user 
- Request operand from user 
- Use if condition to select operation while operand is selected
 """
 
first_number = int(input("Kindly input the first number"))
second_number = int(input("Kindly input the second number"))
operand = input(f"Kindly input the operation \n + = For Addition \n - = For Subtraction \n * = For Product \n / = For Division")
if operand == '+':
    result = first_number + second_number
elif operand == '-':
    result = first_number - second_number
elif operand == '*':
    result = first_number * second_number
elif operand == '/':
    result = first_number / second_number
else:
    print (f"{operand} entered is an invalid operand")
print(f"{first_number} + {second_number} = {result}")
