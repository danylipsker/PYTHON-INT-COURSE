#1) what does slice do?
#slice allows to reach and maneuver srings lists and the like by filtering what items to deal with

#2) What does concatenation does on a string?
# concatenation allows the annexation of several strings into a single one
# this is done using the + (plus) sign between those strings

#3) What is List Comprehension???
# It is an effective way to deal with lists and ranges of element in a single sentence
# in fact it is an hybrid combination of a for loop, within a range with certain conditions
# the advantage is that in one row of code a set of operations can be arranged efficiently.

#4) What is a dictionary??
# dictionary is a sub system to hold data, arranged by a key and a value
# each piece of data is arranged with a key
# dict={a:khhj, b:sgjh, c:yuyty}
# a, b and c are the keys and the relevant are the values
# the keys and the values may be of any kind, ie: integers, strings, floats, lists and even other dictionaries

#5) what types are allowed in dictionaries?
# integes, strings, characters, etc???

#6) what is an Entry
# entry is a pair consisting of a "key" and "value"

#7) XML dictionary is built using <body> and <\body> for every definition
# an example fro the internet...
# <note>
# <to>Tove</to>
# <from>Jani</from>
# <heading>Reminder</heading>
# <body>Don't forget me this weekend!</body>
# </note>

# an example of a cd recording list (only 3 items)
# <CATALOG>
# <CD>
# <TITLE>Empire Burlesque</TITLE>
# <ARTIST>Bob Dylan</ARTIST>
# <COUNTRY>USA</COUNTRY>
# <COMPANY>Columbia</COMPANY>
# <PRICE>10.90</PRICE>
# <YEAR>1985</YEAR>
# </CD>
# <CD>
# <TITLE>Hide your heart</TITLE>
# <ARTIST>Bonnie Tyler</ARTIST>
# <COUNTRY>UK</COUNTRY>
# <COMPANY>CBS Records</COMPANY>
# <PRICE>9.90</PRICE>
# <YEAR>1988</YEAR>
# </CD>
# <CD>
# <TITLE>Greatest Hits</TITLE>
# <ARTIST>Dolly Parton</ARTIST>
# <COUNTRY>USA</COUNTRY>
# <COMPANY>RCA</COMPANY>
# <PRICE>9.90</PRICE>
# <YEAR>1982</YEAR>
# </CD>

#7) JSON dictionary is built using {} etc in  this example...
# {
#   "firstName": "John",
#   "lastName": "Smith",
#   "isAlive": true,
#   "age": 27,
#   "address": {
#     "streetAddress": "21 2nd Street",
#     "city": "New York",
#     "state": "NY",
#     "postalCode": "10021-3100"
#   },
#   "phoneNumbers": [
#     {
#       "type": "home",
#       "number": "212 555-1234"
#     },
#     {
#       "type": "office",
#       "number": "646 555-4567"
#     },
#     {
#       "type": "mobile",
#       "number": "123 456-7890"
#     }
#   ],
#   "children": [],
#   "spouse": null
# }

# #8
# # creation of a dictionary
# tel = {'Arnold': 11111, 'Boaz': 22222, 'Charlie': 33333, 'Dany': 44444}
#
# # adding entries to "tel" dictionary
# tel['Ernest']=55555
# tel['Fanny']=66666
#
# ## overwriting entries to "tel" dictionary
# tel['Ernest']=77777
# tel['Arnold']=88888
#
# # deleting entries to "tel" dictionary
# del tel['Boaz']
# del tel['Charlie']

# 9 and 10
# How to get all the keys from a dictionary?
# tel = {'Arnold': 11111, 'Boaz': 22222, 'Charlie': 33333, 'Dany': 44444}
# print (tel.keys())
# print (tel.values())
# print (tel)

# sorted(tel.keys())
# print(tel)

# 11
# LIST COMPREHENSION
# without list comprehension
# sentence="I love to eat ice cream in the beach"
# x=len(sentence)
# print(x)
#
# for i in range(x):
#     sentence=sentence.upper()
# print(sentence)

# # with list comprehension
# #11 a) create a list of the letters in each words in upper letters
# sentence = "I love to eat ice cream in the beach"
# upper_letters = [i.upper() for i in sentence]
# print()
# print()
# print("\nConvert each letter letter to uppercase: \t",upper_letters)
#
# #11 a) create a list of the words in upper letters
# sentence = sentence.split()
# upper_sentence = [i.upper() for i in sentence]
# print("\nConvert the words to uppercase: \t",upper_sentence)
#
# #11 b) create a list of the first letters of each word
# sentence = "I love to eat ice cream in the beach"
# firstLetterTopper=[word[0] for word in sentence.split()]
# print("\nConvert the first letter to uppercase: \t",firstLetterTopper)
#
# #11 c) create a list of the first letters of each word
# sentence = "I love to eat ice cream in the beach"
# fromThirdLetter=[word[2:] for word in sentence.split()]
# print("\nPrint from the third letter where possible: \t",fromThirdLetter)
#
# #11 d) create a list of the length of each word
# sentence = "I love to eat ice cream in the beach"
# lengthOfEachWord=[len(word) for word in sentence.split()]
# print("\nPrint the length of each word is: \t",lengthOfEachWord)
#
#
# #12 Use list comprehension to create a list of the power of 10 from 1 to 9
# # 10 power of 1, 10 power of 2 etc
#
# nums= [int(1+i) for i in range(0,10)]
# print("\nThis is the list created using list comprehension of numbers from 1 to 10: \t",nums)
#
#
# powerList=[10**i for i in nums ]
# print("\nThis is the powered list at the power of 10: \t",powerList)
# print()
# print()
# print()
#

# 13 Create a function named tryGetValue
# this function gets a dictionary and returns true if there is a value in it and types it to the screen
# # if there is no value it return false and prints none

# Dic = {"a": 1, "b": 2, "c": "none", "d": 4}
#
# def tryGetValue(d, v):
#     for value in Dic:
#         # to print the value of the key
#         print (Dic[value])
#         # to print just the value
#         print (value)
#         if (Dic[value] == v):
#             print ("true")
#             break
#         else:
#             print ("false")
#
#
# Dic = {"a": 1, "b": 2, "c": "none", "d": 4}
# tryGetValue(Dic, "none")


# 14 Create a function named getSortedKeys
# This function gets a dictionary and a key and it returns the entries sorted on the screen

def getSortedKeys(d, k):
    '''

    :param d:
    :param k:
    :return: a list of all the sorted entries
    '''



# 15 Create a function named mergeDictionary
# This function gets a dictionary and a key and it returns the entries sorted on the screen

def mergeDictionary(d1, d2):
    '''

    :param d1: first dictionary
    :param d2: second dictionary
    :return: returns the 2 dictionaries merged
    '''

    return (d1.update(d2))


dict1 = {1: "A", 2: "B", 3: "C", 4: "D"}
dict2 = {5: "E", 6: "F", 7: "G", 8: "H", 9: "I"}


print("first Dictionary entries are: ", dict1)
print("Second Dictionary entries are: ", dict2)

dict3 = mergeDictionary(dict1, dict2)
print("Merged dictionaries dict1 and dict2 are: ",dict1)


# 16 Write a program that inputs 2 values:
# a) full name
# b) ID number
# the ID will be the key for the dictionary
# the name will be the value
# Check if the the key already exists
# if it exists DO NOT OVERWRITE IT, instead print a message to the user
# if the key does not exists, add it to the dictionary
# repeat until the user enters -1 to the value field
# when finish. print all the entries#

def createDictionary(dic_name, dic_keys, dic_values):
    '''
    :param dic_name: the user will create a dictionary named "persons"
    :param dic_keys: The user will add ID numbers serving as the keys for the dictionary
    :param dic_values: The values will be their Full names as requested
    :return: the return will be the dictionary items until -1 was entered
    '''
    dic_name = {dic_keys[i]: dic_values[i] for i in range(len(dic_keys))}

    return dic_name

def get_user_key_and_values_lists(dic_keys, dic_values):
    endOfDict = '-1'
    full_name = ''
    while not full_name == endOfDict:
          full_name = input("Enter a given person name: ")
          ID_Number = input("Enter a given person ID number: ")

          if EOF == full_name:
             print("End of input values for person list")
             continue
          elif not ID_Number in dic_keys:
               dic_values.append(full_name)
               dic_keys.append(ID_Number)
          else:
              print("Person's Key is already in Persons Dictionary...")
              continue
    return dic_keys, dic_values

# persons_keys = ['1' ,'2', '3']
# persons_names = ['a', 'b', 'c']
persons_keys = []
persons_names =[]
persons_keys, persons_names = get_user_key_and_values_lists(persons_keys, persons_names)
persons = {}


persons = createDictionary(persons, persons_keys, persons_names)
# persons = {persons_keys[i]: persons_names[i] for i in range(len(persons_keys))}
print(persons.items())

#
# c=0
# persons={}
#
# endOfDict ='-1'
# full_name = ''
# while not full_name == endOfDict:
#     full_name=input("Enter your name: ")
#     ID_Number=int(input("Emter your ID please: "))
#
#     if full_name == endOfDict:
#         print("End of input values to dictionary")
#         continue
#     elif not ID_Number in persons.keys():
#        persons[ID_Number] = full_name
#        c=c+1
#
#     else:
#        print("Person's Key is already in Persons Dictionary...")
#        continue
#
# print(persons.items())


