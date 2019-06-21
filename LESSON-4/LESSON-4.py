## FOR LOOP
#
numberList = [[1, 300, 5], [7, 800, 9], [-4, 10000, 200]]
sum = 0

for currentList in numberList[1:]:
    print(currentList)
    for number in currentList:
        sum = sum + number
        print(number, sum)
        if sum > 100:
            break
    print("after list...")
print(sum)
print("####################")
#######################################################
names = ["aaa", "bbb", "ccc", "ddd", "eee"]

print("The original list is: ", names)
for n in range(len(names)):
    print(f'names in location [{n}],{names[n]}')

print()
print("Printing the same list in reverse order: ")

for n in range(len(names) - 1, -1, -1):
    print(f'names in location[{len(names) - n - 1}],{names[n]}')
print("####################")
###########################################

print("####################")
#######################################################
names = ["aaa", "bbb", "ccc", "ddd", "eee"]

print("The original list is: ", names)
for n in range(len(names)):
    print(f'names in location [{n}],{names[n]}')

print()
print("Printing the same list in reverse order: ")

for n in reversed(range(len(names) - 1, -1, -1)):
    print(f'names in location[{len(names) - n - 1}],{names[n]}')
print("####################")
###########################################

print("####################")
print("Create a list of numbers by using the range function")
lst = list(range(2, 46, 7))  ## pay attention to casting
rng = range(2, 46, 7)  ## pay attention to creation of a list
print(rng)
print(lst)

print("####################")
print("####################")
## WHILE LOOP

# foreach
# for number in numbers:...
# for
# for n in range(...)

# while x>0: # infinite loop or while True
#     x = int(input("Enter a number"))
#     print(x)
# print("outside loop....")


# x=1
# while x>0: # infinite loop or while True
#     x = int(input("Enter a number"))
#     print(x)
#       if x<0:
#           break
# print("outside loop....")


# x=1
# while False: # infinite loop
#     x = int(input("Enter a number"))
#     print(x)
print("####################")

# write a while loop which inputs a number from the user
# each time print the numbers between 1-number inputed
# the loop will terminate when the input number was 0 or below
print("####################")
# a=0
# while True:
#     x=int(input("Enter any number:"))
#     print(f"you entered {x}")
#     span=range(1,x+1,1)
#     print(list(span))
#     if x<0:
#         break
# print("only positive numbers please")
print("####################")

# Calculate the class average until average was above 90
# When negative grade was entered - break
# when grade was zero continue - student without grade - ignore

# average = 0
# numberOfStudents = 0
# sum = 0
#
# while average <= 90:
#     grade = float(input("Enter a student grade: "))
#     print(f"You entered: {grade}")
#     if grade < 0:
#         print(f"You entered a negative: {grade}")
#         break
#     if grade == 0:
#         print(f"You entered a zero: {grade}")
#         continue
#     sum = sum + grade
#     print(f"The sum of grades is: {sum}")
#     numberOfStudents = numberOfStudents + 1
#     print(f"The amount of students input is: {numberOfStudents}")
#     average = sum / numberOfStudents
#
# print(f"The Average of grades in the class is: {average}")
#
# print("####################")


# input 2 numbers
# print message: input +, -, *, /, Q
# + == sum...
# if user enter enters a different sign, ignore
# if user divides by "0" break the loop

result = 0
numberA = float(input("Enter first number"))
print(numberA)

numberB = float(input("Enter second number"))
print(numberB)

while numberB != 0:
    print(f"You entered a zero number, retype it{numberB}")
    # continue
    break

signs = str(input("Enter '+', '-', '*', '/' or 'Q'"))
print(f"You entered {signs}")

while signs != 'Q':
    if signs == '+':
        result = numberA + numberB
        print(f"the result is {result}")
        break

    if signs == '-':
        result = numberA - numberB
        print(f"the result is {result}")
        break

    if signs == '*':
        result = numberA * numberB
        print(f"the result is {result}")
        break

    if signs == '/':
        result = numberA / numberB
        print(f"the result is {result}")
        break

    if signs == 'Q':
        print(f"You exit the loop due to entering {'Q'}")
        break
