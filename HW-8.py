#1)
# What is the use or *args
# by using the *args one is not limited to pre determine the amount of arguments and values while using the function
# *args is basically a TUPLE type of elements
# it is a list of member that can not be altered

# What is the use of **kwargs
# this kind of argument allows the user to return a structure in the form of a dictionary, values and keys

#2)
# What is so special in a tuple
# tuple is an immutable list of data
# it means that it can keep data that it can not be changed
# it is used as a safe method of keepinf arrays of information
# very few methods exist for tuples

#3)
# OOP means that we create a prototype of something that contains veriables, functions, results etc.. and this prototype
# can be instatiated by creating an "OBJECT" from it
# the OBJECT has the same behavior and methods that the prototype has been given in the first place
# the prototype is called a CLASS
# CLASS or classification is a joint of many things and properties together.
# The modern way of using objects is much more flexible, robust and easy to follow than older methods of programming

#4)
# What is the difference between a class and an instance
# see my anser in #3

#5)
# how a class is declared in python???
# first: type the keyword "class" in small letters
# second: type the name of the class "capitalizing the first letter"
# end it with a "semi colon"
'''
class Moshe:
    moshesHeight=189
    moshesWeight=89
    pass

    #etc
    #etc

from now on, each parameter is a method which can be called and used by typing a "dot" after the class name
'''


#6)
# which function is read automatically at the object creation
# __init__(self)

#7)
# show two (2) ways a property can be changed in an XAML



#8)
#why there is "__" in the function names?
# it is a way python uses to protect the names of its internal methods and prevent mistakenly changing them

#9)
#what distinguishes functions and methods?
# Functions can be used anywhere inside and outside other types
# Methods are part of specific classes and were pre determined by the function creator in the first place

#10)
# How can we "hide a function"?
# by using 2 (two) underscores prior of writing the name of the function
# while the function is in hidden status, en error will occur if I call this method or try to use this methods
# for example:
# def __dany(self):


#11)
# write a function having *args as numbers and returns a sorted list
# convert it to "TUPLE"

def sortedNumbers(*args):
    l = list(args)
    print(f"The original list of numbers: ", l)
    s = sorted(l)
    print(f"The sorted list of numbers: ", s)
    t = tuple(s)
    print(f"The converted list of numbers to Tuple: ", t)

    return (t)


a = sortedNumbers(2, 8, 5, 3, 6, 7, 9, 4, 1, 0)
print(a)

#12)
#Write a function in python having  in the **kwargs a "key value" and dictionary and returns true if
# the parameter **kwargs is equal to the dictionary, else, return false



#13)
#write a class named SUPERHERO with the methods:
#forceSpeed()
#Climb()
#Fly()

class SuperHero():
    def __init__(self):
        return self
        print("Comics books came to life")

    def forceSpeed(self):
        return self
        print("I am strong as Steel")

    def climb(self):
        return self
        print("I climb like a gekko")

    def fly(self):
        return self
        print("I fly like an Eagle")

superRachel=SuperHero()
superDany=SuperHero()
superBar=SuperHero()

print(superRachel.climb())
print(superRachel.forceSpeed())
print(superRachel.fly())


# in the __init__ function, print: "new super hero is born"
# after that, create 3 superheros and use their methods accordingly
