def calculator(x,y):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Invalid Operator"

num1 = float(input("Enter the 1st number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter the 2nd number: "))

calc = calculator(num1,num2)
        



print(calc)