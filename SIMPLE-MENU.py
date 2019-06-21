#  1. shekel to dollar
print("Menu: ")
print()
print("(1) Shekel to Dollar")
print()
print("(2) Dollar to Shekel")
print()
print("(3) Exit")

shekel_dollar  = 3.616
dollar_shekel = 1/shekel_dollar

#loop get user option and execute until exit

option_str=input('Your choice:')
while option_str.isdigit() and option_str !=3:
    option=int(option_str)

    if option ==1:
        shekel = int(input('How many Shekels?'))
        result=shekel*dollar_shekel
        print("for {} Shekels you get {} dollars".\
              format(shekel, result))
    elif option ==2:
        dollar = int(input('How many Dollars?'))
        result = dollar * shekel_dollar
        print("for {} Dollars you get {} Shekels". \
              format(dollar, result))
    else:
        print("option does not exist.\
        please contact support ")
        option_str=input('Your choice')
print("goodbye")