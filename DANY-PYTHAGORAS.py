# Pythagoras example


from math import *
#from math import sin, cos, tan, asin, acos, atan

# input of dat from user
print('enter a')
a = int(input())
print('enter b')
b = int(input())

#squares calculation
sq_a = a * a
sq_b = b * b

#square root calculation
c = sqrt(sq_a + sq_b)

#angle calculations
first_angle = acos(a / c) * (180.0 / 3.14159263)
second_angle = asin(a / c) * (180.0 / 3.14159263)

#outputs
print("You entered:", a)
print("a Squared equals:", sq_a)
print()
print("You entered:", b)
print("b Squared equals:", sq_b)
print()
print("The Pythagoras of a and b is:", c)
print()
print("The angle between a and c is: ", first_angle)
print()
print("The angle between b and c is: ", second_angle)
print()