# #100 days of code python

# ("jyotika here")
# print("hello world").   #Strings are immutable in python. This means that once a string is created, it cannot be changed. If you try to change a string, you will get an error.


# print(10 * 26)

# # Comments (cnrl+/) , escape sequence \n , Print statement
# print("hey please double quote \"this\"")
# print("hey this is the how I will write\nnew line")

# # Variable, datatype, Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# print("date", 1,2,3.7, sep=":", end="!\n")
# variable_Dict = {"empName": "jyotika", "empId":"jyotika"}
# print(variable_Dict)
# mixed_Value_Dict= {"empName": "jyotika", "empId":123}
# #----------
# j=26.08
# d=None
# print("what is the type of j", type(j))
# print("what is the type of d", type(d))
#---------------------------------------------------------

# day 8
# Operators, Arithmetic operators, calculation using python, calculator Exercise 1
# j = 26
# b = 8
# sol1 = j+b
# print("Addition of",j, "and",b,"is", sol1)

# sol2 = j-b
# print("Subtraction of",j,"and",b,"is", sol2)

# sol3 = j*b
# print("Multiplication of",j,"and",b,"is", sol3)

# sol4 = j/b
# print("Division of",j,"and" ,b,"is", sol4)

# sol5 = j**b
# print("Floor Exponential of",j,"and",b,"is", sol5)
#---------------------------------------------------------
# Operator	OperatorName	Example
# +	        Addition	     15+7
# -	        Subtraction	   15-7
# *	     Multiplication	   5*7
# **	    Exponential	     5**3. # 5*5*5 (double into **) To the power of
# /.      	Division	     5/3 # returns quetient obvious.
# %	        Modulus	       15%7 #remainder of 15?7 = 1
# //	   Floor Division	   15//7 # 15/7 = 2.142857142857143. # 15//7 = 2

#----------------------------------------------------------
# day 9
# Typecasting in python Explicit (done by developer as per requirement) and Implicit (According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

#Explicit Type Conversion (Type Casting):
#This requires the programmer or developer to manually convert the data type using built-in functions.
# Implicit Type Conversion: python automatically converts one data type to another. This process doesn't need any user intervention.

# These functions include int(), float(), str(), list(), tuple(), set(), dict(), bool(), etc.
# Explicit conversion can lead to data loss if a larger data type is converted to a smaller one (e.g., converting a float to an integer truncates the decimal part).
# string = "50"
# number = 6.5
# typecast_String_To_Int = int(string) #it is basically converting string to integer.
# sum = number + typecast_String_To_Int #sum is now an integer.
# print("The Sum of both the numbers is: ", sum) #successfully typecasted string to integer.
#---------------------
# a="2"
# b="3"
# print(int(a)*int(b)) #typecasting string to integer.
#----------------------------------------------------------
# day 10
# Taking input user in Python.
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# But input function returns the value as string. *********Hence we have to typecast them whenever required to another datatypE**********

# name = input("enter your name :")
# print("my name is", name)
#---------------------------------------------------------
# x = input("enter first number: ")
# y = input ("enter second number: ")
# print(x + y) # it will give the output as string automatically or say by default. #remember this.
# print(int(x) + int(y)) #But since you typecasted it to integer, it will give the output as integer now! 
#--------------------------------------------------------
# firstName = input("enter your first name: ")
# secondName = input ("enter your second number: ")
# print(firstName, secondName) #it will simply print the first name and second name as concatinated strings.

# Excersize 2 ( input program using different operations )
# a = input("enter your first number : ")
# b = input("enter your second number : ")
# print(a+b)
# c = input("enter your first number : ")
# d = input("enter your second number : ")
# print(c + d) # it will give the output as string automatically or say by default.
# if you want to get the output as integer then you have to typecast it.

# x = input("enter the first number ")
# y = input("enter the second number ")
# print( x + y) # not in red becuase + will simply concatinate the strings.
# print( x - y)
# print ( x * y)
# print ( x / y) # operations wont work without having x y to be typecasted to integers first. that is why it shows in red color.
# print( int(x) + int(y))
# print( int(x) - int(y))
# print ( int(x) * int(y))
# print ( int(x) / int(y))
# print ( int(x) ** int(y))
# print ( int(x) // int(y))
# print ( int(x) % int(y)) #great! it worked.

#---------------------------------------------------------

# Day 11 Strings in python ( String is a sequence of characters enclosed in quotes. Python provides various ways to work with strings. We can use single quotes, double quotes, or triple quotes to define a string.
# name = "Alice"
# print("Hello, " + name)
#Output : Hello, Alice

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
# Multiline Strings
# If our string has multiple lines, we can create them like this:
# a = """this is how you use tripple quotes to
# write multiline string in python
# and it will print the output as it is"""
# print(a)

#Now how do we use double quotes inside a string that is enclosed in double quotes? We can escape the double quotes using a backslash, like this:

# x = "He said, \"like 'this\"" #or
# we can use single quotes inside a string that is enclosed in double quotes.
# y = 'He said, "like this"'

# print (x)
# print (y)
# output will be same for both
#-------------------------------------------------------
# [] what is indexing in python [] - Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on. For example, if we have a string "Hello", we can access the first letter "H" using its index 0 by using the square bracket notation: string[0] example below :
# name = "jyotika"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7]) # it will throw error as the index is out of range. #remember this.

#for loop in python - when we have to perform indexing of a long string then we use for loop instead of writing the print statement for each index.
# for loop code is below :
# for i in name:
#   print (i)

# Example of indexing in python using 'for loop' is below :
# delhi = '''delhi is the capital of india, it is my home town,
# it is poluted however since i spent most
# of my childhood here, thats why i love it.'''
# for character in delhi:
#   print(character)

# ---------------------------------------------------------

# String slicing Day 12

# name = "mango is sweet"
# print(len(name)) #len() function is used to find the length of the string. output will be 14
# print(name[0:5]) #output will be mango
# # python takes the first index as 0 and the last index is excluded. #remember this.

# exercise 3
# nm = "Harry"
# len is 5 so if we want to print the last 4 charecters then we have to write the code as below :
# print(nm[-4:-2])
# print(nm[1:3])
# the output will be ar

# ---------------------------------------------------------

#Day 13 :
# String method in python 
# Python provides a set of built-in methods that we can use to alter and modify the strings.

# print (len(J)) #output will be 7
# there are  string methods in python like upper(), lower(), replace(), find(), capitalize(), center(), count(), endswith(), startswith(), isalnum(), isalpha(), islower(), isupper(), isprintable(), isspace(), istitle(), swapcase(),
#---------------
# J = "jyotika"
# J.upper() to turn the string into uppercase and J.lower() to turn the string into lowercase.
# print(J.upper()) #output will be JYOTIKA
#--------------
# J. rstrip (" ") to remove the trailing spaces from the string.
#example : J = "jyotika is good girl....."
# print(J.rstrip(".")) #output will be jyotika is good girl 
#eample -
# j = "Hello @@@@"
# print(j.rstrip("@")) #output will be Hello without @

# J.replace, it replaces the string with the new string. for example J.replace("Jyotika", "priyanka") will replace Jyotika with priyanka. 

# J.split it splits the string into a list. for example J.split(" ") will split the string into a list of words. output will be ['Jyotika', 'is', 'good', 'girl'] so jyotika is first element of the list and so on.

# J.capitalize- The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

# Pythondiaries = "i have studied python for 13 days" 
# print(Pythondiaries.capitalize()) the output will be 
# I have studied python for 13 days, it turned only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

# J.center() - The center() method aligns the string to the center as per the parameters given by the user. for example J.center(50) will align the string to the center of 50 spaces.

# J.count() - The count() method returns the number of times the given value has occurred within the given string. for example J.count("Jyotika") will return 1 as Jyotika is present only once in the string.

# J.endswith() - The endswith() method checks if the string ends with a given value. If yes then return True, else return False. for example J.endswith("girl") will return True as the string ends with girl.
 # endswith() method example with string slicing below :
# sum = "jyotika is good girl"
# print(sum.endswith("girl", 4, 8)) #output will be false as the string does not end with girl from index 4 to 8. 

# J.find() - it finds the first index of the string. for example J.find("is") will return 8 as is is present at index 8, always starting from 0, in case the value is absent from the string it returns as -1. #remember this.
# example : J = "jyotika is good girl"
# print(J.find("in"))
# output will be -1 as in is absent from the string.

# J.index() - The index() method is same as find () however, it searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string it returns a ValueError. 

# J.isalnum() - The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# example : 
# J = "jyotika123"
# print(J.isalnum()) #output will be true as the string only consists of A-Z, a-z, 0-9.


#J.isalpha() - The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
# example :
# J = "jyotika"
# print(J.isalpha()) #output will be true as the string only consists of A-Z, a-z.

# J.islower() - The islower() method returns True if all the characters in the string are lower case, else it returns False.
# example :
# J = "jyotika"
# print(J.islower()) #output will be true as all the characters in the string are lower case.

# J.isprintable() - The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# example :
# J = "jyotika\n"
# print(J.isprintable()) #output will be false as the string contains a newline character.

# J.isspace() - The isspace() method returns True only and only if the string contains white spaces, else returns False.
# example : J = " "
# print(J.isspace()) #output will be true as the string contains white spaces. #white space is a space that is not visible and marked by using spacebar or tab key.

# J.istitle() - The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# example :
# J = "Jyotika Is Good Girl"
# print(J.istitle()) #output will be true as the first letter of each word of the string is capitalized.

# J.isupper() - The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# example : 
# J = "JYOTIKA"
# print(J.isupper()) #output will be true as all the characters in the string J I G G are upper case.

# J.startswith() - The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
# example :
# J = "jyotika is good girl"
# print(J.startswith("jyotika")) #Output will be true as the string starts with jyotika.

# J.swapcase() - The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# example :
# J= "Jyotika Is Good Girl"
# print(J.swapcase()) #Output will be jYOTIKA iS gOOD gIRL.

# J.title() - The title() method capitalizes each letter of the word within the string.
# example : 
# J = "jyotika is good girl"
# print(J.title()) #output will be Jyotika Is Good Girl.

#----------------------------------------------------------

#Day 14 
# if-else, elif, nested Statements. 

# In Python, if, elif, and else statements are used for decision-making, allowing your program to execute different blocks of code based on whether certain conditions are true or false. Nested statements involve placing one or more if, elif, or else statements inside another.

#1. if statement:
# The if statement executes a block of code only if a specified condition is true.
# example : 
# age = 18
# if age >= 18:
#     print("You are an adult.") #the output will be You are an adult. as the condition is true.

# 2. else statement:
# The else statement provides an alternative block of code to be executed if the if condition is false.
# example :
# age = 15
# if age >= 18:
#    print ( "you are an adult")
# else:
#    print("you are a minor")

# 3. elif statement:
# The elif (short for "else if") statement allows you to check multiple conditions sequentially. If the preceding if or elif conditions are false, the elif condition is evaluated.
# example :
# score = 80 
# if score >= 90:
#    print(" Grade A")
# elif score >= 80:
#   print(" Grade B")
# else :
#   print("Grade c")

# 4. Nested if-else statements:
# Nested if-else statements occur when you place an if-else (or elif) structure inside another if, elif, or else block. This is useful for evaluating conditions hierarchically.
# example :
# temprature = 25
# if temprature > 40:
#   print(" it is a warm day")
# elif temprature >=5 and 17:
#    print("it is a cool day")
# elif temprature >= 25:
#       print("today its humid")
# else:
#  print("it is a windy day")


# Day 15 : Good morning sir, Exercise 4, using if else, elif statements.

# time= int(input("Enter the time in 24 hours foprmat: "))
# if time >= 5 and time < 12:
#   print('Good morning')
# elif time >12 and time <17:
#   print("Good afternoon")
# elif time >17 and time <20:
#   print("Good evening")
# else: 
#   print("Good night")
# ------------- Time module functions in python -------------------Self------------

# First off import time, so start with :
# Import time and then in next line use time module functions as per the task, such as :

# import time - The statement import time in Python is used to import the built-in time module. This module provides various functions for working with time-related operations

# print(time.ctime(0)) # it converts time expressed in seconds since epoch to a readable string, epoch is the point where your computer thinks time begins (1 January 1970) 0 refers to the number of seconds after epoch.

# print(time.time()) # return current seconds since epoch, the output will be some million seconds.

#import datetime - The datetime module in Python provides classes for manipulating dates and times. It is part of the standard library and is widely used for various date and time-related operations.
#a = datetime.datetime.now()
#print(a) the output will be current date and time.

# strftime() - The strftime() method in Python is a powerful function used to format datetime objects into human-readable strings. The name "strftime" stands for "string format time." It allows for customized representations of dates and times by specifying a format string. 
# Common Directives (Examples):
# %Y: Year with century (e.g., 2025)
# %m: Month as a zero-padded decimal number (e.g., 07)
# %d: Day of the month as a zero-padded decimal number (e.g., 10)
# %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 15)
# %M: Minute as a zero-padded decimal number (e.g., 14)
# %S: Second as a zero-padded decimal number (e.g., 30)
# %A: Full weekday name (e.g., Thursday)
# %B: Full month name (e.g., July)


# Exercise by harry :
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# Will learn more about it later.--------------------------------

# DAY 16 : Match case statements in python
# Match case statements in Python are a powerful feature introduced in Python 3.10. They provide a more concise and readable way to handle multiple conditions compared to traditional if-elif-else statements. The match case statement is particularly useful for pattern matching and can be used to match values against a series of patterns.

# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)

# ---------------------------------------------------------
#  Day 17 : For loop in python - A for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each element in the sequence.

# Two types of loops for and while loop, a while loop is used to iterate over a block of code as long as a certain condition is true. or when we do not know the numbers of loops to be executed unlike for loop. 

# there are three arguments or parameters in for loop, start, stop, step.
# start (optional): The starting value of the sequence (inclusive). Defaults to 0 if not specified.
# stop: The end value of the sequence (exclusive). The sequence will not include this value.
# step (optional):The increment or decrement between each number in the sequence. Defaults to 1 if not specified. 

# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
#  Basic for Loop Syntax:
# for variable in iterable:
#   print(variable) #iterable can be a list, tuple, dictionary, set or string.
#---------------------------------
# Example: iterating over a string:
# name = 'Abhishek'
# for i in name:
#     print(i, end=", ") #output will be A, b, h, i, s, h, e, k,
#---------------------------------
# Example: iterating over a list:
# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)
# Output:
# Red
# Green
# Blue
# Yellow
#--------------------------------
# NESTED FOR LOOP : EXAMPLE ******
# for x in range (3): #this line means(out loop) kitni bar loop chalega 
#   for y in range (1, 9): #this line of inner loop means kaha se kaha tk chalega excluding the last number. 
#     print(y, end=",") #this line means kya print karna hai seperation kya dena hai. 
# ---------------------------------------------------------
#range function in python - The range() function in Python is used to generate a sequence of numbers. It is often used in for loops to iterate over a specified range of values. The range() function can take one, two, or three arguments.
# ---------------------------------------------------------
# name = "Jyotika"
# for char in name:
#  print(char)
# ---------------------------------------------------------


# Day 18 While loops - A while loop in Python is used to repeatedly execute a block of code as long as a specified condition is true. Unlike a for loop, which iterates over a sequence, a while loop continues to execute as long as the condition remains true.
# for example : take the input from the user to enter a number and print the number until the user enters a number that is greater than 38, then the loop will stop and print done with the loop.

# i = int(input("Enter the number: "))
# print(i)
# while(i<=10):
#   i = int(input("Enter the number: "))
#   print(i)

# print("Done with the loop")

#Decrementing loop
# i = int(input("Enter the number: ")) #input from the user was  5 in this case.
# while(i>0):
#   print(i)
#   i = i - 1
# print("Done with the loop")
# the output will be 5 4 3 2 1 Done with the loop
# ----------------------------------------------------------
# Do-While loop in python - Python does not have a built-in do-while loop construct like some other programming languages (e.g., C++, Java). However, its behavior can be emulated using a standard while loop with a break statement or by ensuring the loop body executes at least once before the condition is checked. 
# Emulating do-while behavior using while True and break:
# This method uses an infinite loop (while True) and a conditional break statement to exit the loop once the desired condition is met.

# example of emulating do-while loop in python : (using while True and break) 
# - This is an infinite loop that continues asking the user for input until they enter a number that is not positive (i.e., 0 or a negative number) : 
                                                                                               
# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break
# line by line explanation:
# 1. while True:
# This creates an infinite loop. It means the loop will continue running forever, unless you use a break statement to exit it.

# 2. number = int(input("Enter a positive number: "))
# Prompts the user to enter input with the message "Enter a positive number: ".

# input() returns a string, and int(...) converts that string into an integer.

# The result is stored in the variable number.

# 3. print(number)
# This line prints out the number the user just entered.

# 4. if not number > 0:
# This is a conditional statement that checks if the number is NOT greater than 0, which is equivalent to: if number <= 0:

# 5. break
# If the condition is true (i.e., the number is not positive), the loop breaks and the program stops asking for more numbers.
# ----------------------------------------------------------

# Day 19 : Break and continue statements in python
#break statement - The break statement in Python is used to exit a loop, before it has completed all its iterations. When a break statement is encountered inside a loop, the loop is immediately terminated, and the program control is transferred to the next script.
# example - 
# for i in range(1,4,1):
#     print(i ,end=" ")
#     if(i==4):
#         break
#the output will be 1 2 3       
# ---------------------------------
# continue statement - The continue statement in Python is used to skip the specific iteration of a loop, When a continue statement is encountered inside a loop, the loop skips the remaining code inside the loop for the current iteration and moves on. 
# example - 
# for i in range(1,9,1):
#     print(i ,end=",")
#     if(i<=4):
#         continue
# ---------------------------------------------------------

# Day - 20 : Functions in python
# A function is a block of code that performs a specific task. Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
# There are two types of functions:

# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
# syntax of a user defined function is below :
# def function_name(parameters): 
#Examples below -
# def addNumbers(a, b): 
#     add = a + b
#     print(add)
# a=5
# b=5
# addNumbers(a,b)

# def calculatePercentage(part, whole):
#  percentage = (part/100)* whole
#  print(percentage)

# calculatePercentage(15,100)
# ---------------------------------------------------------
# Day 21 : Function arguments in python - There are four types of arguments that we can provide in a function:
# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments
# ------------------------
# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

#Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

#Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition. 

#Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

# There are two ways to achieve this:

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
# example below :                                       
# def average (*numbers):
#   total = 0
#   for i in numbers:
#     total = total + i
#   print ("Average is", total / len(numbers))

# average(5, 6,7)
# ---------------------------------------------------------


# Day 22 : List in python []                  -MUTABLE-
# - Lists are ordered collection of data items. They store multiple items in a single variable. List items are separated by commas and enclosed within square brackets []. Lists are changeable meaning we can alter them after creation

# *******" FIRST INDEX IS ALWAYS 0 IN PYTHON AND THE LAST INDEX IS -1 OR EXCLUDED "********
# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.
#----------------------------------------------------------
## List comprehension : List comprehension in Python offers a concise and efficient way to create new lists based on existing iterables (like lists, tuples, or strings). It provides a more readable and often faster alternative to traditional for loops for list generation and transformation.

# Syntax - new_list = [expression for value in iterable if condition]

# Components
# expression: The operation or transformation to be applied to each item. This determines what value will be added to the new_list.

# item: A temporary variable that represents each element from the iterable during the iteration.

# iterable: The source sequence (e.g., a list, range, string, etc.) that is being iterated over. 

# if condition (optional): A filtering condition that determines whether an item should be included in the new_list. Only items for which the condition evaluates to True are processed by the expression and added to the new list. 

# Examples:
# Squaring numbers in a list.

# numbers = [1, 2, 3, 4, 5]
# squares = [num**2 for num in numbers]
# squares will be [1, 4, 9, 16, 25]
#-------------------------------------------------------------
#Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")
#—————————————————————————————————————————————————————————————————————
# Day 23 : List methods in python - Python provides a set of built-in methods that can be used to alter and modify the lists. These methods are also known as list functions.

# 1.     list.sort()
# This method sorts the list in ascending order. The original list is updated
# Example of numbers :
# num = [4,2,5,3,6,1,2,]
# num.sort()
# print(num) output will be [1, 2, 2, 3, 4, 5, 6]

# Example of strings :
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors) #output will be ['blue', 'green', 'indigo', 'voilet'] 
# sorting is done in lexicographic order, which is essentially alphabetical order (based on Unicode/ASCII values).
#----------------

# 2. reverse()
# This method reverses the order of the list.

# Example:

# num = [4,2,5,3,6,]
# num.reverse()
# print(num) output will be [6, 3, 5, 2, 4]
# -----------------

# 3. index()
#   This method returns the index of the first occurrence of the list item.

#   Example:
#   colors = ["voilet", "green", "indigo", "blue", "green"]
#   print(colors.index("green"))
#output will be 1
#-----------------

# 4. count()
# Returns the count of the number of items with the given value.

# Example:
# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))
#output will be 2 as green is present twice in the list.
#-----------------

# 5. copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# Example:
# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# Outputs will be :
# ['voilet', 'green', 'indigo', 'blue']
# ['voilet', 'green', 'indigo', 'blue']
#-----------------

# 6. append():
# This method appends items to the end of the existing list.

# Example:
# colors = ["voilet", "indigo", "blue"]
# colors.append("green")
# print(colors)
# Output:
# ['voilet', 'indigo', 'blue', 'green']
#-----------------

# 7. insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:
# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]

# colors.insert(1, "green")   #inserts item at index 1
# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexs              [0]       [1]       [2]      [3]
# print(colors)
# Output:
# ['voilet', 'green', 'indigo', 'blue']
#-----------------                 

# 8. extend():
# This method adds an entire list or any other " collection datatype " (set, tuple, dictionary) to the existing list.

# Example :
# #add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)
# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
#-----------------

# 9. Concatenating +
# you can concatinate two lists:
# You can simply concatenate two lists to join two lists.

# Example:
# colors = ["voilet", "indigo", "blue", "green"]
# colors2 = ["yellow", "orange", "red"]
# print(colors + colors2)
# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# or 

# odd = [1, 3, 5,7,9]
# even = [2,4,6,8,10]
# print(odd+even) #output will be [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#-----------------


# 10. clear()
# This method removes all items from the list.
#example : 
# colors = ["voilet", "indigo", "blue", "green"]
# colors.clear()
# print(colors) #output will be []
#-----------------

# 11. pop()
# This method removes the item at the given index from the list. The index is optional, if not specified, the last item is removed. 
# example :
# colors = ["voilet", "indigo", "blue", "green"]
# colors.pop(1)
# print(colors) #output will be ['voilet', 'blue', 'green']
#-----------------


# Day 24 : Tuples ()            - IMMUTABLE -

# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation. 
# Example :
# tup1 = (1,2,2,3,5,4,6)
# tup2 = ("Red", "Green", "Blue")
# print(tup1)
# print(tup2)

# Output:
# (1, 2, 2, 3, 5, 4, 6)
# ('Red', 'Green', 'Blue')

# if a single value of tuple is an integer then it should be written as tup1 = (1,)
# otherwise it will be considered as an integer and not a tuple.
#---------------------------------------------------------------

# Day 25. Manipulating Tuples
#   Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

# syntax to covert tuple to list :
# temp = list(tuple) #to convert tuple to list
# tup1 = tuple(temp) #to convert list to tuple
#------------------

# Example:
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)
# Output:
# ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
#------------------
#We can directly concatenate two tuples without converting them to list.

# Example:
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)
#output will be ('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
#-------------------

# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below 

# 1. count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.

# Syntax:
# tuple.count(element)

# Example
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)
# Output - 3
#------------------

# 2. index() method
# The Index() method returns the first occurrence of the given element from the tuple.

# Syntax:
# tuple.index(element, start, end)
# Note: This method raises a ValueError if the element is not found in the tuple.

# Example
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple.index(3) 
# print('First occurrence of 3 is', res)
# Output - 3
#-------------------------------------------------------------------------------
# yyyeeeeeeyyyyyyyyy Quuuaarrrttteeeeerrr of the ccoooourrrsee dooonneeeee weeellllll!!.....
#-------------------------------------------------------------------------------

# Day 26: Good morning sir solution using time module, check day 15 for reference.

# Excersice : Good Morning !!

# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

# import time
# hour= int(time.strftime('%H'))
# print(hour)
# print(type(hour))
# if (hour>=0 and hour<12):
#   print("Good Morning dear user!")  
# elif (hour>=12 and hour<17):
#   print("Good Afternoon dear user!")
# elif (hour>=17 and hour<24):
#   print("Good Night dear user!") 

# more about this has been understood and explained in day 15, refer that -------------------------------------------------------------------------------------------------

# Day 27 : ********EXERCISE********

# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.




# print("Welcome to \"Kaun Banega Crorepati!\"")
# print("You will be asked 5 questions, you have to answer them correctly to win the total prize money of $500! Good luck!\n")
# print('Question number 1 for prize $100 is below:\n')
# print("1. What is the capital of France?")
# print("The options are: \nA) Rome\nB) Madrid\nC) Paris\nD) Berlin")

# Answer = input("Enter the correct option (A/B/C/D or full answer): ")

# if Answer.lower() == "c" or Answer.lower() == "paris":
#     print("Correct answer! You have won $100!")
# else:
#     print("Wrong answer! You have lost the game!")
#     exit()
# print()
# print('Question number 2 for prize $200 is below :')
# question1 = print("Which planet is known as the Red Planet?")
# options1 = print("The options are : \nA) Earth, B) Mars, C) Jupiter, D) Venus")
# print()
# Answer1 = input("Enter the correct option : ")
# for i in Answer1:
#  if Answer1 == "b" or Answer1 == "B" or Answer1 == "Mars":
#    print("Correct answer! You have won $200!")
# else :
#        print("Wrong answer! You have lost the game!")
# exit()  
# print()
# print()
# print('Question number 3 for prize $300 is below :')
# question2 = print("What is the largest mammal in the world?")
# answer2 = print("The options are : \nA) Elephant, B) Blue Whale, C) Giraffe, D) Hippopotamus")
# print()
# anwswer2 = input("Enter the correct option : ")
# for i in anwswer2:
#        if anwswer2 == "b" or anwswer2 == "B" or anwswer2 == "Blue Whale":
#         print("Correct answer! You have won $300!")
#        else : 
#         print("Wrong answer! You have lost the game!")
# Exit()  
# print()
# print()
# question3 = print("Question number 4 for prize $400 is below : \nWhat is the chemical symbol for . gold?")
# answer3 = print("The options are : \nA) Au, B) Ag, C) Fe, D) Pt")
# print()
# Answer3 = input("Enter the correct option : ")
# for i in Answer3:
#        if answer3 == "a" or answer3 == "A" or answer3 == "Au":
#         print("Correct answer! You have won $400!")
# else :
#        print("Wrong answer! You have lost the game!")
# exit()  
# print()
# print()
# question4 = print("Who wrote the novel \"To Kill a Mockingbird\"?")
# answer4 = print("The options are : \nA) Harper Lee, B) J.K. Rowling, C) Ernest Hemingway, D) F. Scott Fitzgerald")
# answer4 = input("Enter the correct option : ")
# for i in answer4:
#         if answer4 == "a" or answer4 == "A" or answer4 == "Harper Lee":
#           print("Correct answer! You have won $500!")
#         else :
#           print("Wrong answer! You have lost the game!")
#           print()
#           print()
#           question5 = print("What is the capital of Australia?")
#           answer5 = print("The options are : \nA) Sydney, B) Melbourne, C) Canberra, D) Brisbane")
#           answer5 = input("Enter the correct option : ")
#           for i in answer5:
#             if answer5 == "c" or answer5 == "C" or answer5 == "Canberra":
#               print("Correct answer! You have won $500! \n THANK YOU FOR PLAYING!")
#             else :
#                 print("Wrong answer! You have lost the game! \n THANK YOU FOR PLAYING!")
#----------------------------------------------------------
      
  

  




  
  


      
    


    
    
  
  








  



    
  
  

  
   
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































