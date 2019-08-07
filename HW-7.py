# 1)
# Does a memory cell local or global?
# if it is declared outside a function it is GLOBAL
# if inside a function is LOCAL

# 2)
# Calling from a function to a global memory cell is LEGAL?
# in general, a memory cell is a place holder for a value
# When declared, the value is set and it stays as data prepared to be used in later times.
# if we call it from a function and we change it's value during calculation, we, in fact create anothe memory cell
# with similar name.
# due to that, we use memory cells INSIDE or OUTSIDE Functions
# in case we need to keep using a single one along the program, we can use the keyword GLOBAL before the name of
# the variable and this will alloww singularity along the program

# 3)
# If we change a global value within a function, an ERROR will occur

# 4)
# Functions are dynamic elements.
# within functions, values may change according to math operations until the funtion return a result
# if the value changes after it is declared as global, a clash will occur thus truncating the rest of the program

# 5)
# GLOBAL means, use it along the program as a know value that you do not have intention to alter
# due to the common use between several parts of the program with the same value

# 6)
# How to return 2 or more values from a function using return?
# We can return a LIST of values instead
# later on we can dismantle it and get each parameter separatedly

# 7)
# What is a SET?
# a set is a collection of values that do not repeat themselves
# if we as for a list [1,2,3,4,4,4,5,6,7}
# a SET of the list will be {1,2,3,4,5,6,7}

# 8)
# While asking to deal with existing files stored in the Hardisk, we use the OPEN() method to deal with
# the inner information stored there

# 9)
# open can be done in 6 ways, each with its conditions and specifications:
# r
# w
# a
# r+
# w+
# a+

# 10)
# While dealing with any file stored in the hardisk or elsewhere, the files gets "BUSY" by the open() method
# in order to return it to normal harddisk storage and use, we need to CLOSE() it
# the fail of closing it will prevent it's use and also prevent any change to it to be permanently set

# 11)
# How to assure tha file is automativcally closed?

# 12 A)
# What does SEEK() Do?
# It allows the user to point where to start dealing with the data stored in the file at a certain position

# 12 B)
# What does TELL() Do?
# It allows the user to know where in positional value how long is the data stored in the file at a certain position

# 13)
# write a program that gets  numbers from the user until -1 is entered
# as a return, print the amount of numbers entered
# as a return, print the amount of numbers entered without duplications
# as a return, print the amount of numbers entered, how many of them are duplicated

# ********************************************************
def get_list_of_numbers():
    '''
    It creates and empty list by input numbers
    :return: a list of non sorted numbers
    '''
    list_of_num = []
    EOF = "-1"
    last_input = None
    while last_input != EOF:
        last_input = input("\nEnter a number (to end your input type -1): ")
        if last_input != EOF:
            list_of_num.append(int(last_input))
        else:
            return list_of_num
# ********************************************************

# ********************************************************
def print_counts_of_list_values(list_of_num):
    '''
    counts how many...
    :param list_of_num:
    :return:
    '''
    unique_num = set(list_of_num)
    for i in unique_num:
        print(i, " : ", list_of_num.count(i))
# ********************************************************

# ********************************************************
def number_of_appearances_in_list(list_of_num):
    '''
    Shows the amount of appearances of a number in the list
    :param list_of_num:
    :return: counter of values
    '''
    counts_of_values = {}
    unique_num = set(list_of_num)
    for i in unique_num:
        counts_of_values[i]= list_of_num.count(i)

    return counts_of_values
# ********************************************************

# ********************************************************
def print_duplicates_in_list(list_of_num):
    '''
    Finds if in a list are duplicates
    :param list_of_num:
    :return: a dictionary of keys and values showing the duplicated values
    '''
    uniques_dict = number_of_appearances_in_list(list_of_num)
    print(uniques_dict)
    for i in len(uniques_dict):
        if uniques_dict>1:
            print("\n The duplicates are: ", uniques_dict[i])

    #print("\n The duplicates numbers are: ", [[uniques_dict.keys[i], uniques_dict[i]] for i in uniques_dict if uniques_dict[i] > 1])


# ********************************************************


# QUESTION 13 of HW-7
# call the function prepared earlier

# function 1
list_of_numbers = get_list_of_numbers()
print("\nThe length of the original list is: ", len(list_of_numbers))
print("\nThe numbers entered by the user are: ", list_of_numbers)
print("\nUnique numbers found are: ",set(list_of_numbers))

# function 2
print_counts_of_list_values(list_of_numbers)

counters = number_of_appearances_in_list(list_of_numbers)

print("\nthe counters are: ",counters)

# ********************************************************

# 14)
# write a program the inputs words from the user until the word "exit" is typed.
# every entered word type it to a file
# after ending, print the inside of the file

# ********************************************************
def get_list_of_words():
    '''
    It creates and empty list by input numbers
    :return: a list of non sorted words
    '''
    list_of_words = []
    EOF = "exit"
    last_input = ""
    while last_input != EOF:
        last_input = input("\nEnter a word (to end your input type exit): ")
        if last_input != EOF:
            list_of_words.append(last_input)
        else:
            return list_of_words
# ********************************************************

# ********************************************************

list_of_words=get_list_of_words()
print(list_of_words)
list_of_words=str(list_of_words)
f1=open(r"d:\python\int-course-materials\words.txt","a+")
f1.write(list_of_words)
f1.close()

f1=open(r"d:\python\int-course-materials\words.txt","a+")
str2=f1.read()
print(str2)
f1.close

# 15)
# Create a file with number in rows, each number in each row
# Write a program that sums the numbers written in an existing file
# each number in a separate row and type to that file the sum at the last row

#
f2 = open(r"d:\python\int-course-materials\numbers.txt", "a+")


def open_file_name(name):
    sum_of_numbers=0
    for line in open(name):
        line = int(line)
        sum_of_numbers = sum_of_numbers + line

    return sum_of_numbers


sum = open_file_name(r"d:\python\int-course-materials\numbers.txt")
print(sum)
f2.write("\n")
f2.write("Sum of Numbers: ")
f2.write("\n")
f2.write(str(sum))
f2.write("\n Done by Dany Lipsker")
f2.close()



# 16)
# write a function which gets a file and a word
# if that word exist in the file, return True
# else return False

f3 = open(r"d:\python\int-course-materials\word-compare", "a+")
list_of_words = f3.readlines()
f3.close()

def compare_words_written_to_a_file(wwww):
    counter=0
    anyWord = input("Type a word: ")
    print(anyWord)
    while True:
        for word in open(wwww):

            if anyWord == word:
                return True
                counter = counter + 1
                continue
            else:
                return False
                counter = counter + 1
                continue




ccc=compare_words_written_to_a_file("d:\python\int-course-materials\word-compare")

f3.write("\n")
f3.write("Compared words are: ")
f3.write("\n")

f3.write("\n Done by Dany Lipsker")
f3.close()

# 17)
# Write a program that takes a source file and a target file
# the file will copy the contents of the original file and type it to the new one in reverse order
