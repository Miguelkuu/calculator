
while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("That was a invalid number")

while True:
    ope = input("Enter a operation: ").strip()
    if ope in ("+", "-", "*", "/"):
        break
    print("Invalid operator, Try + - * /")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("That was an invalid number")

def calcu():
    if ope == "+":
        print(num1 + num2)
    elif ope == "-":
        print(num1 - num2)
    elif ope == "/":
        print(num1 / num2)
    elif ope == "*":
        print(num1 * num2)

calcu()