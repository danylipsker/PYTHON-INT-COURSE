# 1)  WHEN TO USE "RANGE" IN A LOOP??
# 2) how range is defined?
'''
RANGE IS A WISE METHOD AND FUNCTION SERVING AS A WAY TO STORE SERIES OF VALUES
THESE VALUES ARE DETERMINED BY:
A START VALUE = a
A FINAL (NOT INCLUDED) = b
A STEPPING VALUE = c

TYPICAL SYNTAX: range(a,b,c)

a can be smaller or bigger than b
if c is positive then the values grows
if c is negative then the values shrinks

examples:
A) range(3,287,6)
it returns
3
9
16
...
...
282

it starts with 3, it ends with 286, stepping every 6 numbers

B) range(287,3,6)
it returns an empty list due to the stepping

C) range (287,3,-6)
it returns
287
281
275
...
...
9
'''

# ---------------------------------------------------------

'''
# 3) how to convert range into a list???
# (' \n'
# 'simply by casting it with \n'
# 'list(range(a,b,c)) \n')
# a = list(range(3, 287, 6))
# print(a)
'''
# ---------------------------------------------------------

'''
# 4) Why do we need DO While and While loops???
#
# 4A) DO WHILE does not really exists, "while True:" is the right syntax instead

# Using while True loop serves mainly when the programmer forces the program to use the loop and check it at least once

# 4B) WHILE loops are used to comply with a certain logical condition until it is complied
# ('\n'
# 'The condition is always written as an opposite to what we want to achieve\n'
# 'example: \n'
# 'while t<100:\n'
# '    Do something....\n'
# '    \n'
# '    it means that as long as the logical condition is true, keep doing the loop\n')
# '''
# ---------------------------------------------------------

'''
# 5) What is the difference between While True and While???
# 5A) While true checks a logical condition after the program enters the loop:
# 5B) While loops starts immediately by acting as a logical condition and the program does not have to pass trough the while loop is the condition is not met at all

# 6) How can we use the do-while loop in python
# Example:
'''
# ---------------------------------------------------------

'''
average = 0
stop = "s"
numberOfGrades = 0
sumOfGrades = 0

while stop.upper() != "s":
    a = int(input("Enter your Exams grade: "))
    sumOfGrades = sumOfGrades + a
    numberOfGrades = numberOfGrades + 1
    average = sumOfGrades / numberOfGrades

# output statuses

    print(f"You Entered: {a}")
    print(f"Summing up your grades: {sumOfGrades}")
    print(f"You entered {numberOfGrades} grades so far")
    print(f"The average of your grades is: {average}")

# loop behaviour and conditions
    if a > 100:
        print("Come on, No grades are bigger than 100, bluff someone else:"
              "\n breaking out")
        numberOfGrades = numberOfGrades - 1
        continue

    if a < 0:
        print("No negatives grades exist !!! ")
        print("\n enter another grade instead")
        numberOfGrades = numberOfGrades - 1
        continue
    
    ########## this part does not work well, ask ITAY what's wrong
    if stop.upper == "s":
        print("You asked to stop !!! ")
        print("\n Please RUN AGAIN")
        break
'''
# ---------------------------------------------------------
'''
# 7 
The keyword "continue" allows the loop to keep going unless a certain condition exist
in Short: continue allow a huge tolerance while input of data
'''

# ---------------------------------------------------------
'''
#8 write a program that prints all the integer numbers from 200 down to 2 (not included) in descending order

r=range(200,2,-1)
for n in r:
    print (n)
'''
# ---------------------------------------------------------
''' 
#9 write an effective program that prints all the factor of 7 ranging from 1 up to 100
print(list(range(1,100,7)))
'''
# ---------------------------------------------------------
'''
#10 write a program that input numbers until a negative number is input
# print all those numbers without the negative one
n=0
sum=0
pos=True

while n>=0:
    n=int(input("Enter a number:"))
    sum=sum+n
    continue

    if n<0:
        sum=sum-n
        break
print(f"The sum of the 'legal numbers is: ",sum)
'''
# ---------------------------------------------------------
'''
 #11 Write a program to calculate the factorial of that number
#Variables and initial values
fact = 1
n = int(input("Enter a number:"))
r = range(1, (n + 1))
m = list(r)
#Status and OUTPUT
print(f"You entered {n}")
print(f"The range of numbers you enteres is: ", m)
print(f"The value of the number you entered is: ", m[n - 1])
# TESTS:
# print(m[n-1])
# fact=fact(m[n+1]*m[n])
# print(fact)

for i in r:
    fact = fact * m[i - 1]
print(f"The factorial of the number you entered is: ", fact)
'''
# ---------------------------------------------------------
# 12
#
# import os
# os.system('cls||clear')

# STARTING VALUES
guessNumber = 0
i = 0  # just a counter
r = range(2, 49, 10)  # create a list of 5 numbers:  2,12,22,32,42
luckyList = list(r)  # convert the range to a list:  [2,12,22,32,42]
luckyListLength = (len(luckyList))  # calculate the length of the list: 5
trials = 0  # how many trials until THE USER guess ALL 5 NUMBERS

# SOLUTION NUMBERS

print()
print("--------------------------")
print("HIDDEN FROM THE USER !!!!")
print(f"The length of the list is: {luckyListLength} members long")
print("The Members of this list are: ", luckyList)
print("--------------------------")

# while i != 0:
while luckyListLength > 0:
    guessNumber = int(input("\nEnter a number from 2 up to 49 INCLUDED:\t"))

    if guessNumber >= 2 and guessNumber < 50:
        print(f"\nYou typed number: ", guessNumber)
        trials = trials + 1
        print(f"\nThe amount of trials:\t", trials)
    else:
        print(f"\nType numbers ONLY within THE range 2 to 49:\t", guessNumber)
        print()
        guessNumber = int(input("\nEnter a number from 2 up to 49 INCLUDED\t"))
        trials = trials + 1
        print(f"\nThe amount of trials:\t", trials)
        continue

    while guessNumber in luckyList:
        print("\nYou typed one of the lucky numbers")
        luckyListLength = luckyListLength - 1
        break

# print(luckyList)
print("\n Congratulations!!! You guessed all 5 lucky numbers")
print(f"\n The amount of trials: ", trials)
