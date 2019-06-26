# 1) WHAT IS A FUNCTION??/
# A FUNCTION IS A DEFINITION OF OPERATIONS ENCAPSULATED I A SINGLE OBJECT WITH THE ABILITY TO RECEIVE PARAMETERS AND ARGUMENTS AND RETURN A SOLUTION
#FUNCTIONS ARE CREATED OR USED TO CREATE REPETITIVE TASKS WITHIN PROGRAMS.
# THE SAME FUNCTION, BY INPUTING DIFFERENT VALUES , RETURNS DIFFERENT OUTPUT ALL ACCORDING TO THE PROCEDURES WITHIN

# 2) HOW TO DEFINE A FUNCTION???

# usually:
# def somethingUsefull(argument1, argument2, argument3, etc):
#     bla bla
#     calculate something we may need
#         return a value
#
# calling a function:
# somethingUsefull(argument1, argument2, argument3, etc)

# 3) HOW TO ADD A PARAMETER IN A FUNCTION:
# option A: "parameter not initialized yet"
#     def myFunct(parameter1)
#
# option B: "parameter initialized in the function"
#
#     def myFunct1(parameter1=123.45) -- numeriacal
#
#         or
#
#     def myFunct2(parameter=True) -- boolean
#
#         or
#
#     def myFunct3(parameter="Moishe") -- String
#
#         or
#
#     def myFunct3(parameter=["Moishe", 45, "yankale", 23] -- Lists
# Alignment:
# The last parameter must be aligned to the right in order to be valid
#
#4 How to use a parametric value within a function in PYTHON?
# def myFunction(parameter-1, parameter-2, etc)
# the parameters could be used in the function by changing their value according to will.

#5 Functions are very usefull as sub code to deal with a repetitive procedure
# If the end result of the procedure may be used lately, we use the Keyword : RETURN value
# this returned value is the solution of the calculated formula

#6 The return value might be various, all according to need
# one of them is an empty value or NONE
# other values are also possible such as booleann, numeric value, strings, lists and more.

#7 in order to use a random generator we use the random() function
# Python, by default saves space and this library is not loaded
# In order to use it we IMPORT it to our program using import random
# after we imported it we can access all its methods and options within
# for example
# 1) random.randint(a,b) --> return a random INTEGER between a and b INCLUDING
# 2) random.uniform(a,b) --> return a random FLOAT between a and b INCLUDING
# 3) and others as well

#8
'''
PP=3.14159263
print("\nLets calculate the area and the perimeter of a circle")
radius = int(input("\nEnter a radius please: "))


def areaOfCircle( radius ):
    area = PP * radius ** 2
    return area

def perimeterOfCircle( radius ):
    perimeter = PP * 2 * radius
    return perimeter


print(f"\nThe Area of a circle with radius {radius} is: {areaOfCircle(radius)}")
print(f"\nThe Perimeter of a circle with radius {radius} is: {perimeterOfCircle( radius )}")
'''
#9 create a calculator with 4 functions
# ADD, SUB, MUL, DIV
# input 2 numbers X and Y from the user and print out the 4 solutions

#CALCULATOR
'''
# DEFAULT VALUES
number1=0
number2=0

# USER INPUT AND VALUES CHECK
print("\nLets calculate THE SUM, THE SUBSTRACTION, THE MULTIPLICATION and THE DIVISION of 2 numbers")
number1 = int(input("\nEnter a number please: "))
number2 = int(input("\nEnter another number please: "))
if number2==0:
    number2 = int(input("\n\tEnter a non zero number please: "))
# DECLARING FUNCTIONS
def sumOfNumbers():
    adding = number1 + number2
    return adding

def subOfNumbers():
    substracting = number1 - number2
    return substracting

def mulOfNumbers():
    multiplying = number1 * number2
    return multiplying

def divOfNumbers():
    dividing = number1 / number2
    return dividing

# OUTPUT
print(f"\nThe SUM of {number1} and {number2} is: \t{sumOfNumbers()}")
print(f"\nThe SUB of {number1} and {number2} is: \t{subOfNumbers()}")
print(f"\nThe MUL of {number1} and {number2} is: \t{mulOfNumbers()}")
print(f"\nThe DIV of {number1} and {number2} is: \t{divOfNumbers()}")

'''
# 10
# #create a function named: getInRange
# the function takes 2 parameters, MIN and MAX
# the user inputs a value and the function checks if the value is within the range MIN-MAX
# ONLY when the value is within that range the output is OK


# import random
# min = 10
# max = 100
#
# number1 = int(input("\nEnter a number please between 10 and 100: "))
# print(f"You entered this number: {number1}")
#
# rr = random.randint(min, max)
#
# def getInRange(min,max):
#
#     print(rr)
#     return rr
#
#
# while False:
# #while number1 in range(min,max):
#
#     if rr == number1:
#         continue
#         print(f"Your Number: {number1} is Exactly the number we expected")
#
#
#     elif rr < number1:
#         continue
#         print(f"Your Number: {number1} is smaller than the acceped range : 10 to 100")
#
#     else:
#         continue
#         print(f"Your Number: {number1} is bigger than the acceped range : 10 to 100")
#
# print(getInRange(10,100))


# 11 write a function to find the lowest among 3 numbers
number1 = int(input("\nEnter a number please: "))
print(f"You entered {number1}")
number2 = int(input("\nEnter a number please: "))
print(f"You entered {number2}")
number3 = int(input("\nEnter a number please: "))
print(f"You entered {number3}")


def lowOfThree(number1, number2, number3):
    if number1 <= number2 and number1 <= number3:
        lowest = number1
    if number2 <= number3 and number2 <= number1:
        lowest = number2
    if number3 <= number1 and number3 <= number2:
        lowest = number3
    return lowest


print(f"The lowest of the numbers you entered is: ", lowOfThree(number1, number2, number3))
