print(
    '''
    1) Type in a list of numbers
    2) Include list within lists
    3) Create a ne variable to hold the sum of each sub list
    4) Run a foreach loop until the sum is bigger than 100
    5) Check the sum and break from the loop if the local sum reaches 100 or more
    '''
)
numbersList = [[1, 103, 5], [2, 7, 96, 8, 10], [27, 105, 200]]
sum = 0

for currentList in numbersList:
    # zero set the "sum" variable
    sum = 0
    print()
    print(currentList)

    # number is the item of the sub list
    for number in currentList:
        sum = sum + number
        print("the list number is: ", '\t', "{:4}".format(number), '\t', "The sum until break is: ", '\t', sum)
        if sum >= 100:
            break
print('''
"I am breaking the loop here !"
''')
