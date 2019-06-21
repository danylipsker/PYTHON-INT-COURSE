formula = input("enter calculation,\
 PAY ATTENTION to SPACES between member format: X+Y:")
numList = formula.split()

operand = numList[1]
a = numList[0]
b = numList[2]

if numList[1] in ["+", "-", "*", "/"]:

    print("{} is a legal operand".format(numList[1]))
    if numList[1] == "+":
        print("{} {} = {}".format(a, operand, b))
    elif numList[1] == "-":
        print("{} {} = {}".format(a, operand, b))
    elif numList[1] == "*":
        print("{} {} = {}".format(a, operand, b))
    elif numList[1] == "/":
        print("{} {} = {}".format(a, operand, b))
    else:

## end this targil
