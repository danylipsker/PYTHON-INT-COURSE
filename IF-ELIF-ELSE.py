# fullName=input("Enter your full name!")
# list = fullName.split();
#
# firstName=list[0];
# lastName=list[1];
# print("Your full name is: {}, {}".format(firstName, lastName))

formula = input("Enter calculation, remember to type a space between members\
 , format: X + Y: ")

numList = formula.split();
print(numList)

if numList[1] == "+":
    print("plus")
elif numList[1] == "-":
    print("minus")
elif numList[1] == "*":
    print("multiplication")
elif numList[1] == "/":
    print("division")
else:
    print("Wrong operator")

a = float(numList[0]);
b = float(numList[2]);
operator = numList[1];

plus = a + b;
print(formula);
print("{}{}{} ".format(a, operator, b))
