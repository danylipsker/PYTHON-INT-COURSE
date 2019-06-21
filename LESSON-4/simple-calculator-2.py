# SIMPLE CALCULATOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = ""

while operator.upper() != "Q":
    operator = input("Enter an Operator, +,-,*,/ : ")

    if operator in ["+", "-", "*", "/"] == False:
        continue
    if operator == "/" and b = 0:
        print("can not divide by zero !!!")
    break
    if operator == "+":
        print(f"{a}+{b}={a + b}")
