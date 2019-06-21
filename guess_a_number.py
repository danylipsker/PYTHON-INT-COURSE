#STARTING VALUES

guessNumber = 0
r = range(2, 49, 10) #2,12,22,32,42
luckyList = list(r) #[2,12,22,32,42]
luckyListLength=(len(luckyList)) # 5
trials = 0

# SOLUTION NUMBERS

print()
print("--------------------------")
print("ALL THESE NUMBER MUST BE HIDDEN FROM THE USER !!!!")
print("The length of the list is: ", len(luckyList))
print("The Members of the list are: ",luckyList)
print(luckyList[0])
print(luckyList[1])
print(luckyList[2])
print(luckyList[3])
print(luckyList[4])
print("--------------------------")

# loop until the length of the list is "0"
# in other words

while luckyListLength != 0:
    for i in r:
        guessNumber = int(input("Enter a number from min 2 and up to 49 max"))
        print(f"You typed: {guessNumber}")
    
    '''
       if guessNumber != luckyList[0] and guessNumber != luckyList[1] and guessNumber != luckyList[2] and guessNumber != \
                luckyList[3] and guessNumber != luckyList[4]:
            guessNumber = int(input("Enter a number from min 2 and up to 49 max"))
            print(f"You typed: {guessNumber}")
            trials = trials + 1
            continue
    '''
       
            if guessNumber == luckyList[luckyListLength - 5]:
                del luckyList[0]
                print(luckyList)
                trials = trials + 1
                continue

            elif guessNumber == luckyList[luckyListLength - 4]:
                del luckyList[1]
                print(luckyList)
                trials = trials + 1
                print("Numbers remaining to guess: ", luckyListLength)
                continue

            elif guessNumber == luckyList[luckyListLength - 3]:
                del luckyList[2]
                print(luckyList)
                trials = trials + 1
                print("Numbers remaining to guess: ", luckyListLength)
                continue

            elif guessNumber == luckyList[luckyListLength - 2]:
                del luckyList[3]
                print(luckyList)
                trials = trials + 1
                print("Numbers remaining to guess: ",luckyListLength)
                continue

            elif guessNumber==luckyList[luckyListLength - 1]:
                del luckyList[4]
                print(luckyList)
                trials = trials + 1
                print("Numbers remaining to guess: ",luckyListLength)
                break

    luckyListLength = luckyListLength - 1

print(f"You guessed: ",guessNumber)
# print(luckyList)
print(f"The number of trials untill you guessed is: ", trials)
print("Numbers remaining to guess: ",luckyListLength)
