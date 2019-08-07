# 1) QUESTION
# How to define "data in an Object"???
#
# 1) ANSWER:
# for example lets create a class named Cars
# cars have functionality and properties a s well
# once a property is set it can not be deleted
# instead, it can be UNUSED or NOT DEFINED ITS VALUE
'''
class Cars():
    pass


def __init__(self):
# properties
    color = self.color
    size = self.size

    return color

def startMethod(self):

    key=self.key
    button=self.button
    card=self.card

subaru=Cars()
subaru.color="yellow" # this is a local property given only to Subaru
subaru.size=457 # This is also a property given only for Subaru
'''


# 2) QUESTION:
# in which function we declare data about objects?
# 2) ANSWER:
# in the __init__() function

# 3) QUESTION:
# how to send parameters to the init function:
# 3) ANSWER:
# just create them with or without a value
# this value will serve as the default one
# this value can be overwritten while creating an object of by passing data to and from the object

# 4) QUESTION:
# What other name does the INIT function has:
# 4) ANSWER:
#


# 10 QUESTION
# Create a class named BankAccount
# in the init function it gets:
# a) an account number
# b) user name
# c) user family name
# d) balance

# A - create an STR and REPR functions


class BankAccount():
    def __init__(self, accountNumber, firstName, lastName, balance, country):
        self.accountNumber = accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        self.country = country

    def __str__(self):
        return f" Sir/Madam {self.firstName + self.lastName} the Balance in account {self.accountNumber}is: {self.balance}"

    def __repr__(self):
        return f" Sir/Madam ({self.firstName + self.lastName}) the Balance in account ({self.accountNumber})is: ({self.balance})"

    def __sub__(self, other):
        return self.balance - other.balance

        print("the gap is: ", self.__sub__)

    def __add__(self, other):
        return self.balance + other.balance

        print("the sum is: ", self.__add__)

    def __mul__(self, other):
        return self.balance * other.balance

        print("the multiplication is: ", self.__add__)

    def getBalance(self, country):

        if country == "usa":
            self.balance = self.balance * 3.7
            #print(self.balance)

        elif country == "france":
            self.balance = self.balance * 3.88
            #print(self.balance)

        else:
            self.balance = self.balance
            #print(self.balance)


danyAccount = BankAccount("ABCD1234 ", "Dany ", "Lipsker", 15000, "france")

rachelyAccount = BankAccount("HIJK7890 ", "Rachely ", "Lipsker", 12000, "israel")

if danyAccount.balance == rachelyAccount.balance:
    print("Both accounts:\n", danyAccount.__str__(), "\nand,\n", rachelyAccount.__str__(), "\n\nhave the same amount")
    print()

    print(danyAccount.__repr__(), "\nand\n", rachelyAccount.__repr__())

elif danyAccount.balance > rachelyAccount.balance:
    print("\nDany's account is richer than Racheli's\n", danyAccount.__str__())

else:
    print("\nRacheli's account is richer than Dany's\n"), rachelyAccount.__str__()

print("Are our accounts equal: ???", danyAccount.balance == rachelyAccount.balance)

minus = danyAccount.balance - rachelyAccount.balance

plus = danyAccount.balance + rachelyAccount.balance

multip = danyAccount.balance * rachelyAccount.balance

getBal = danyAccount.getBalance("france")

print("the difference between those accounts is: ", minus)
print("the sum between those accounts is: ", plus)
print("the multiplication between those accounts is: ", multip)
print("Dany's account foreign currency balance is: ", getBal)
