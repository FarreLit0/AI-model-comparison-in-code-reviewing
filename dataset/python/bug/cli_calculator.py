def calculate():
    op = input("Enter operation (+, -, *, /): ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        print(x / y)
    else:
        print("Invalid operation.")