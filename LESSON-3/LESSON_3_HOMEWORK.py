# HOMEWORK ANSWERS

# 1 .מתי כדאי להשתמש בלולאה?
#  A loop serves as an effective method to create repetitive operations
#  in which calculations and parameters may vary along independently

# 2 .מה ה syntax של לולאה בפייטון?
'''
for blablabla in cucucuc:
    Do something useful
'''

# 3 .אם נתונה לי רשימה של מספרים, לדוגמא [100, 8, 7, 5, 1 [וארצה לעבור בלולאה על מחצית
# המספרים הראשונים, כיצד אכתוב זאת?

nums = [1, 5, 7, 8, 100, 14, 78, 95, 46]
low_index = 0
high_index = len(nums) // 2

# print a range of numbers
print()
print()
print("Using just the print() function the output is: ", nums[low_index:high_index])
print()
print()

# create a new list with half the numbers
half_nums = nums[low_index:high_index]

# if doing it by using a foreach loop then:
for num in nums:
    print("Using a for loop the list is: ", half_nums)
    if nums[high_index]:
        break

# 4 .ייצר רשימה של מילים לדוגמא : [‘coding of world’, ’pen’, ‘python’, ‘hello .[‘כתוב לולאה העוברת
# על הרשימה ומדפיסה כל מילה באותיות גדולות

print()
names = ["hello", "python", "pen", "world of coding"]
print("original list is: ", names)
print()
for name in names:
    print("creating UPPER CASE OF A GIVEN LIST: ", name.upper())

#  5.שנה את תרגיל 4 ,אם נתקלת במילה הקצרה מ- 4 אותיות, צא מהלולאה

print()
names = ["hello", "python", "pen", "world of coding"]
print(names)
print("the length of names list is: ", len(names))
print()

for name in names:
    print("the length of {} in names list is: ".format(name), len(name))
    if len(name) < 4:
        break
print()
print("The word with 3 letters is: ", name)

my_name = "Daniel Lipsker"

x = len(my_name)
y = my_name.split()
z = list(y[0])
w = list(y[1])

# print(x)
# print(y)
# print(z[3])
# print(z)
# print()

print("the length of my name is: ", x)
print("Print the 5 last letters of my name: ", my_name[-5:len(my_name)])
print("Print the first third of the string: ", my_name[0:x // 3])
print("The ammount of times the letter 'a' appears in my name is: ", my_name.count("a"))
print("Does the 'b' letter appears in my name???", "b" in my_name)
print("My name is divided into two separated strings", my_name.split())
print("My name in reverse order: ", my_name[::-1])
print("Change only the last name to UPPER CASE: ", y[1].upper())
print("remove the middle letter in my name: ", z.remove(z[2]))
print("After all modifications my name is: ", z, w)

greetings = "hello world!"
print("The location of the First 'o' is: ", greetings.find("o"))
print("The location of the Last 'o' is: ", greetings.rfind("o"))
print("The result of typing from start to first 'o' is: ", greetings[0:greetings.find("o")])
print("The result of typing from last 'o' to the end is: ", greetings[7: -1])

print("print the greetings without any 'o' letter: ", greetings.replace("o", ""))
print()
print()

nums = [8, 1000, -3, 2, 5]
print("original list: ", nums)
a = len(nums)
print("the length of list: ", a)
sum_nums = sum(nums)
print("The sum of the numbers is: ", sum_nums)
avg = sum_nums / a
print("The average of the numbers is: ", avg)
print()
print("The given list of numbers is:", nums)
print("The sum of these numbers is:", sum(nums))
print("The biggest number of these numbers is:", max(nums))
print("The smallest number of these numbers is:", min(nums))
print("The average of these numbers is:", sum(nums) / a)
print("Remove the middle number from the list: ", nums.pop(2))
nums.sort()
print("the sorted list looks like: ", nums)
print("This list multiplied by 5: ", nums * 5)
print("Remove the first item from the list: ", nums.pop(0), " The reminding list is:  ", nums)

nums = [8, 1000, -3, 2, 5]
i = 0
new_list = []
for i in range(len(nums)):

    if nums[i] < avg:
        print("The numbers below the average are: ", nums[i])
        new_list.append(new_list)

print()
print()
numbers = [1, 5, 7, 8, 100, 234, -67, 453, 1095]
max = numbers[0]
for number in numbers:
    if number >= max:
        max = number
print("The maximal number from this list is: ", max)

print()
print()

numbers = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]
#----------------------
sub_list_0 = numbers[0]
print("The values of this sub list are: ", sub_list_0)
min_value_0 = 0

for i in sub_list_0:
    if i < min_value_0:
        min_value_0 = i
print("The lowest number of this sub list is: ",i)
#-------------------------

sub_list_1 = numbers[1]
print("The values of this sub list are: ", sub_list_1)
min_value_1 = 0

for j in sub_list_1:
    if j < min_value_0:
        min_value_0 = j
print("The lowest number of this sub list is: ",j)

#--------------------
sub_list_2 = numbers[2]
print("The values of this sub list are: ", sub_list_2)
min_value_2 = 0

for k in sub_list_2:
    if k < min_value_0:
        min_value_0 = k
print("The lowest number of this sub list is: ",k)

new_list=[min_value_0,min_value_1, min_value_2]
print(new_list)

