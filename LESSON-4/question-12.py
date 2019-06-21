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