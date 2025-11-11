
# Common Dictionary Methods :

# Method	                                        Description	                                          Example
# keys()	                                 Returns all keys in the dictionary.	                  student.keys()
# values()	                             Returns all values in the dictionary.	                  student.values()
# items()	                                 Returns key-value pairs as tuples.	                      student.items()
# get(key, default)	                     Returns value for key, or default if key not found.	  student.get("age", 0)
# update(dict2)	                         Merges dict2 into the dictionary.	                      student.update({"age": 26})

# pop(key, default)	                     Removes key and returns its value (or
#                                          default if key not found).	                              student.pop("grade")

# popitem()	                             Removes and returns the last
#                                          inserted key-value pair.	                              student.popitem()

# setdefault(key, default)	             Returns value for key, else sets it to default.	      student.setdefault("city", "Unknown")
# clear()	                                 Removes all items from the dictionary.	                  student.clear()
# copy()	                                 Returns a shallow copy of the dictionary.	              new_dict = student.copy()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Practice Basic :
#
# Write a Python program that prints all numbers from 1 to 20,
# but replaces multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
#
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#--------------
from numpy.ma.core import append


# Write a Python program that Asks the user to enter two numbers. Adds those numbers together. Prints the result.

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# print(num1 + num2)
#---------------

# Write a Python program that: Asks the user to enter a number. Checks whether the number is even or odd. Prints the result.

# num = int(input("Enter a number : "))
# if num % 2 == 0:
#   print(f"{num} is even")
# else:
#   print(f"{num} is odd")
#-----------------

# Asks the user to enter three numbers, Finds the largest number among them. Prints the result

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
#
# if num1> num2 and num1 > num3 :
#     print(f"{num1} is greater")
# if num2> num1 and num2 > num3 :
#     print(f"{num2} is greater")
# if num3> num1 and num3 > num2 :
#     print(f"{num3} is greater")
# else :
#     print("Some numbers are equal")

#----------------------

# Asks the user to enter a word. Prints the word in reverse order.

# word = input("Please enter the word : ")
# print(word[-1::-1])

#---------------------

# Asks the user for a number. Prints the multiplication table for that number (from 1 to 10).

# num = int(input("Enter a number: "))
# count = 1
# for item in range(1,11):
#     print(f"{num} * {count} = {num * count}")
#     count += 1
#----------------------

# Write a Python program that: Asks the user to enter 5 numbers.Stores them in a list.
# Prints the sum of those numbers. Prints the largest number from the list.

# num1 = int(input("Enter the first "))
# num2 = int(input("Enter the second "))
# num3 = int(input("Enter the third "))
# num4 = int(input("Enter the fourth "))
# num5 = int(input("Enter the fifth "))
#
# ListNums = [num1 , num2 , num3 , num4 , num5]
# SumNum = sum(ListNums)
# LargestNum = max(ListNums)
# print(f"The sum of numbers is {SumNum}")
# print(f"The largest number is {LargestNum}")
#-------------------------------------------------------------------

# Write a Python program that: Asks the user to enter any 5 numbers. Stores them in a list.
# Prints only the even numbers from that list. Prints only the odd numbers from that list.

# evens = []
# odds = []
#
# for i in range(5):
#     num = int(input(f"Enter number {i + 1}: "))
#
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)
#
# print("Even numbers:", evens)
# print("Odd numbers:", odds)
#----------------------------------

# Ask the user to enter 7 numbers, Store them in a list. Print only the numbers greater than 10.

# Lst = []
#
# for i in range (7):
#     num = int(input(f"Enter number {i+1}: "))
#
#     if num > 10 :
#         Lst.append(num)
#
# print(Lst)
#--------------------------

# Ask the user to enter 6 numbers.Store them in a list. Print only the negative numbers from the list.

# Lst = []
# for i in range(6):
#  num = int(input(f" Please enter number {i+1}: "))
#
#  if num < 0 :
#   Lst.append(num)
# print(Lst)
#----------------------

# Write a Python program that: Asks the user to enter 8 numbers. Stores them in a list.
# Separates the numbers into three different lists:  Even numbers , Odd numbers. Numbers greater than 50
# Prints all three lists.

# L1 = []
# L2 = []
# L3 = []
#
# for i in range(8):
#  num =  int(input(f"Enter number {i +1}: "))
#
#  if num % 2 == 0:
#     L1.append(num)
#  if num % 2 != 0:
#     L2.append(num)
#  if num > 50 :
#     L3.append(num)
#
# print(f"Even numbers: {L1}")
# print(f"Odd numbers: {L2}")
# print(f"Greater than 50 : {L3}")
#---------------------------------

# Write a program that asks the user for a sentence and counts how many vowels (a, e, i, o, u) are in it.

# def vowelCount():
#     sen = input(" type a sentence : ").lower()
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for char in sen:
#         if char in vowels:
#             count += 1
#     print(f" There are {count} vowels in this sentence.")
#
# vowelCount()
#-------------------------------------

# Write a function factorial(n) that returns the factorial of a number. Example: factorial(5) → 120.

# def factorial_recursive(n):
#     if n < 0:
#         return "Factorial does not exist for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
#
# num = int(input(" Enter the number :  "))
# print(f"The factorial of {num} is {factorial_recursive(num)}")
#---------------------------------------------------

# Creates a dictionary with 3 students’ names as keys and their marks as values.
# Finds the student who scored the highest marks.
# Prints that student’s name and marks.


# students = { "John" : 78, " Patrick " : 82, " Cherry " : 91 }
#
# topper = max(students, key=students.get)
# marks =  students[topper]
# print(f" The top scorer is {topper} with {marks} marks!")

#----------------------------------

# Write a program that:
# Stores 5 students with their marks in a dictionary.
# Finds the student with the highest marks (topper).
# Finds the student with the lowest marks.
# Prints both names with their marks.

# def result():
#   students = {"Mat": 89, " Ron ": 87, "Sady": 85, "Rick": 92, "Peter": 70, "Kurt": 84}
#   TopStud = max(students, key= students.get)
#   topMarks = students[TopStud]
#   LowMarksStudent = min(students, key= students.get)
#   LowerMarks = students[LowMarksStudent]
#
#   print(f"Topper is {TopStud} with {topMarks} Marks.")
#   print(f"Lowest scorer is {LowMarksStudent} with {LowerMarks} marks.")
#
# result()
#-------------------------------------

# (Average & Above Average Students):
# Write a program that:
# Stores 6 students with their marks in a dictionary.
# Calculates the average marks of the class.
# Prints the average marks.
# Prints the names of students who scored above the average.

#
# students = {"Mat": 89, "Ron": 87, "Sady": 85, "Rick": 92, "Peter": 70, "Kurt": 84}
#
# average = sum(students.values()) / len(students)
# print(f"Class average = {average}")
#
# above_avg = []
# for name in students:
#     if students[name] > average:
#         above_avg.append(name)
#
# print("Students scoring above average:", ", ".join(above_avg))

#------------------------------------------

# Find the most expensive product. Find the cheapest product. Print their names with prices.

# products = {"Laptop": 55000, "Phone": 30000, "Tablet": 25000, "Headphones": 5000, "Monitor": 15000}
#
# expensive = max(products, key=products.get)
# priceE = products[expensive]
# cheaper = min(products, key=products.get)
# priceC = products[cheaper]
# print(f" The most expensive product costs : {expensive} with price : {priceE} ")
# print(f" The cheapest product costs : {cheaper} with price : {priceC} ")
#--------------------------------------------------------------------------------------

# Calculate the average population. Print the average. Print the names of cities above the average population.
#
# cities = {"Delhi": 32000000, "Mumbai": 21000000, "Chennai": 11000000, "Kolkata": 15000000, "Bengaluru": 12000000}
#
#
# average = sum(cities.values()) / len(cities)
# aboveAlist = []
# for city in cities:
#
#      if cities[city] > average:
#       aboveAlist.append(city)
#
# print(f"The average population is {average}")
# print(f"The cities with above average population are: {', '.join(aboveAlist)}")

#-----------------------------------------------------------------------------------------

# Calculate the average salary. Print the average. Print the names of employees earning above average.
# Print the names of employees earning below average.

# employees = {"Alice": 50000, "Bob": 60000, "Charlie": 45000, "Diana": 70000, "Eve": 55000}
#
# average = sum(employees.values()) / len(employees)
# aboveAlist = []
# belowAlist = []
# for name in employees:
#
#      if employees[name] > average:
#       aboveAlist.append(name)
#      if employees[name] < average:
#          belowAlist.append(name)
#
# print(f"The names of the employees earning above average are: {" , ".join(aboveAlist)}")
# print(f"The names of the employees earning below average are: {" , ".join(belowAlist)}")
#------------------------------------------------------------------------------------------------

# Practice 1: Counting letters in a word :
# Task:
#
# Take the word "banana"
# Use a dictionary to count how many times each letter appears.
# Use a loop and .get() exactly like we did before.
# Print the final dictionary.


# word = "banana"
#
# counts = {}
# for letter in word:
#     counts[letter] = counts.get(letter, 0) + 1
# print(counts)
#------------------------------------------------------------------------------------------------------

user_friends = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2}
}





























































