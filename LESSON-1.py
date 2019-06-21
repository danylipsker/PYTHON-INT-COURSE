print('hello')  # this is a string                                  --output--> a string : hello
print(10 / 2)  # this is a float                                   --output-->5.0
print(10 // 2)  # this is a whole number division                   --output-->5
print(89 % 10)  # this is a MODULO ---> the remainder of a division --output-->9
print(89 // 10)  # this is a whole remainder division                --output-->8
print(8 // 3)  # this is a whole remainder division                --output-->2
print(7 % 2)  # this is a modulo                                  --output-->1

# memory cells
# storing data

age = 55  # int number of my age
address = "kazir"  # string of my address
status = "married"  # string of my marital status
numberOfChildren = 2  # int number of my kids  ---> this is CAMMEL STYLE WRITTING, each word starts with small letter and the next words stsrt with CAPITAL

# once we have some data stored, it is possible to manipulate and play with it

# let's add some more data
weight = 80.8  # float number of my weight

salary = 10000  # int number of my salary

# living costs can also be stored in data
rent = 2345.3  # numerical data
food = 1256.85  # numerical data
fun = 1897.24  # numerical data
carExpenses = 3125.69  # numerical data

# remain = 0.0  # declared an unknown number as a float - this is due to unknown data entered by the user
livingCosts = rent + food + fun + carExpenses
# the amount were declared earlier, now we can calculate
# livingCosts is now a sum or a calculation of many elements and numeric variable

salary = salary - 1234.56
# I reduced my salary to check if the calculation still works
# the writting here can be:

# salary = salary + 1234
# or
# salary += 1234

# instead of + we can type any operation such as +,-,*,/ etc

remain = salary - livingCosts  # another calculation

# the order of declarations and operations is important
# the formulas are based on the last iupdated data
# in my case, the salary was reduced from 10000 by 1234.56
# now the calculation is : 10000-1234.56/ livingCosts

print(remain)  # how to concatenate a bunch of strings????


# what is the TYPE of data entered or calculated?
# use the type() and find out

print(type(remain)) #in this case the type is flaot type
print(type(address))# in this case this is and str --> string type

#type can also chech the math operation and then the result type
# for example

print(type(3456.78/34))     #in this case the type is flaot type
print(type(3456.78//34))    #in this case the type is flaot type

print(type(3456/34))        #in this case the type is flaot type
print(type(3456//34))       #in this case the type is int type


