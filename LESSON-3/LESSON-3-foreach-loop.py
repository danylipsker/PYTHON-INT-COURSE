# Targil 1
# Foreach loop
# addd any amount of numbers to a list
# sort them by size
# add them until they sum up to 100
# if the number is bigger than 100, break the loop
# print the list and the sum

print(
    ''' Lesson 3 --- Targil 1
    # Foreach loop Excercise
    # 1)Add any amount of numbers to a list
    # 2)Sort them by size
    # 3)Add them until they sum up to 100
    # 4)If the number is bigger than 100, break the loop
    # 5)Print the list and the sum
    ''')

numbers = [1, 6, 8, 9, 7, 12, 4, 8, 11, 13, 23, 45, 5]
print()
print("My original list is:", numbers)
print()
numbers = sorted(numbers)
print("The sorted list is:", numbers)
print()

result = 0
for number in numbers:
    result = result + number
    # print()
    print("The number added to result is: ", number, "  The Sum is: ", result)
    if result >= 100:
        break
