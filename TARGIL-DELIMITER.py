formula = input("Enter calculation, remember to type a space between members\
 , format: X + Y: ")
formList = formula.split();

# OPTIONAL INPUTS
# A +B       len()=3
# A+B        len()=1
# A + B     len()=5
# A+ B       len()=3
#  A+  B    len()=5
# ETC...

# the only acceptable option is when len() is 5
# what is the delimiter then???
# "+" is the delimiter we look for

print(len(formList))

if len(formList) > 1:

if formList[1] != " ":
    print("ADD SPACES BETWEEN NUMBERS AND TYPE AGAIN")

# formula = input("Enter calculation, remember to type a space between members\
# , format: X + Y: ")

if formList[1] == "+":
    print("plus")
elif formList[1] == "-":
    print("minus")
elif formList[1] == "*":
    print("multiplication")
elif formList[1] == "/":
    print("division")
else:
    print("Wrong operator")

a = float(formList[0]);
b = float(formList[2]);
operator = formList[1];

plus = a + b;
print(formula);
print("{}{}{} ".format(a, operator, b))
