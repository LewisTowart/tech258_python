# Calculator code

def addition(int1, int2):
    return int1 + int2

def subtraction(int1, int2):
    return int1 - int2

def multiplication(int1, int2):
    return int1 * int2

def division(int1, int2):
    return int1 / int2


print("Welcome to my calculator, please enter two numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter your operator (+, -, *, /): ")

if operator == '+':
    print("Result:", addition(num1, num2))
elif operator == '-':
    print("Result:", subtraction(num1, num2))
elif operator == '*':
    print("Result:", multiplication(num1, num2))
elif operator == '/':
    if num2 != 0:
        print("Result:", division(num1, num2))
    else:
        print("You can't divide by zero.")
else:
    print("Invalid operator")
