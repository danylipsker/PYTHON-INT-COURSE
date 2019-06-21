# import a library
'''
import random
print(random.randint(1,5)) # returns an INTEGER random number from 1 to 5 INCLUDING 5

for x in range(10):
    print(random.randint(1,10))
'''
'''
## guessing program
import random

a = random.randint(1, 100)
print(a)
n = int(input("\nEnter a number between 1 and 100: "))
trials = 0

while a != n:
    if a == n:
        print("\nYou nailed it !!!")
        trials = trials + 1
        break

    elif a > n:
        print("\nThe Number is bigger, try again: ")
        n = int(input("enter a number between 1 and 100: "))
        trials = trials + 1
        continue

    elif a < n:
        print("\nThe Number is smaller, try again: ")
        n = int(input("enter a number between 1 and 100: "))
        trials = trials + 1
        continue

print("\n\nYou found it !!! in", trials, "times")
'''

'''
# create a function "PRINT NUMBERS"
# Accept parameters Maximum
# PRINT numbers 1 to Maximum


def printNumbers(maximum):
    a= int(input("\nEnter a number please: "))
    r=range(1,a+1)
    w=list(r)
    print(f"\nThe list until your Maximum number is: ", w)
    print(f"\nThe Maximum number is: ", a)

printNumbers("")
'''
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

'''
 1) Write a function with parameter x and return x**2
 2) write a function with parameter x,y and return x+y
 3) write a function with parameter x....this function calculates the x! factorial
 4) write a function with parameter x...this function returns boolean True if X is even...False if Odd
 5) write a function myAverage with parameter l1 (=list)...it returs the average of the list
6) write a function myConcat with parameters s1, s2 (=string)...return s1+ "" + s2
'''
# SOLUTION 1

# print("\nLets calculate the square of a number")
# number = int(input("\nEnter a number please: "))
#
#
# def squareNumber():
#     squared = number ** 2
#     return squared
#
#
# print(squareNumber())
#
# print(f"\nThe SQUARE of {number} is: {squareNumber()}")

# SOLUTION 2
# print("\nLets calculate the SUM of 2 numbers")
# number1 = int(input("\nEnter a number please: "))
# number2 = int(input("\nEnter another number please: "))
#
#
# def sumOfNumbers():
#     adding = number1 + number2
#     return adding
#
#
# print(sumOfNumbers())
#
# print(f"\nThe SUM of {number1} and {number2} is: {sumOfNumbers()}")

# SOLUTION 3
# print("\nLets calculate the FACTORIAL of a number")
# number3 = int(input("\nEnter a number please: "))
#
#
# r = range(number3, 0, -1)
# m = list(r)
# fact = 1
#
# def factOfNumber():
#     fact = 1
#     for i in r:
#         fact = fact * m[i-1]
#     return fact
#
# print(factOfNumber())
# print(f"\nThe FACTORIAL of {number3} is: {factOfNumber()}")

# SOLUTION 4
# print("\nLets calculate if a number is EVEN or ODD")
# number4 = int(input("\nEnter a number please: "))
#
# def evenNumber():
#     evenNumber = number4 % 2
#     if evenNumber == 0:
#         print("Even")
#     else:
#         print("odd")
#
#     return True
# evenNumber()

# SOLUTION 5
# print("\nLets calculate The average of A LIST OF NUMBERS")
# number5 = [2, 61, 9, 12.3, 18]
# o = (number5)
#
# print("\nYou entered: ", o)
#
#
# def listAverage(numbers):
#     listSum = sum(number5)
#     listLength = len(number5)
#     listAverage = sum(number5) / len(number5)
#
#     return listAverage
#
#
# print(f"The lenght of the list is: ", len(number5))
# print(f"The sum of the numbers in this list is: ", sum(number5))
# print(f"The average of those numbers are: ", listAverage(number5))

# SOLUTION 6
# print("\nLets CONCATENATE TWO STRINGS")
# print("\nEnter FIRST STRING: ")
# myString1 = str(input("\nEnter your FIRST STRING please: "))
# print("\nEnter SECOND STRING: ")
# myString2 = str(input("\nEnter your SECOND STRING please: "))
#
# def stringsConcatenator():
#     concatenatedString=myString1+" "+"+"+" "+ myString2
#     return concatenatedString
#
# print(f"The concatenation of these two strings is: ", stringsConcatenator())
