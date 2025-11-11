# # 🔹 Q1:
# # Take a number as input and check if it is:
# # positive
# # negative
# # or zero
#
# num = int(input('Enter number : '))
#
# if num == 0 :
#     print(f'{num} is zero')
# elif num > 0:
#     print(f'{num} is a positive number')
# else:
#     print(f'{num} is a negative number')
#-------------------------------------------
# # Q2:
# #
# # Ask the user for their age.
# # If age < 18 → print "You are a minor"
# # Else → print "You are an adult"
#
# Age = int(input("Enter your age: "))
# if Age < 18:
#  print("You are a minor")
# else :
#   print("You are an Adult")
#----------------------------------------

# # 🔹 Q3:
# # Take a number as input and check if it is:
# # Positive
# # Negative
# # Zero
# # This is basically the 3-condition check we discussed earlier.
# # Try coding it yourself using if / elif / else.
#
# num = int(input('Enter the number : '))
# if num == 0: print('Zero')
# elif num < 1: print('Negative')
# else:
#  print('Positive')
#------------------------------------------------

# # 🔹 Q4:
# # Ask the user to enter two numbers and print which one is greater, or if they are equal.
#
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter second number: '))
# if num1 > num2: print(f'{num1} is greater than {num2}')
# elif num1 < num2: print(f'{num2} is greater than {num1}')
# else:
#     print('Both numbers are equal')
#----------------------------------------

# # 🔹 Q4 (slightly harder):
# # Ask the user to enter two numbers.
# # Print which number is greater, or print "Both numbers are equal".
# # Then, additionally, check if their sum is even or odd and print that too.
#
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter second number: '))
# if num1 > num2: print(f'{num1} is greater than {num2}')
# elif num1 < num2 : print(f'{num2} is greater than {num1}')
# else:
#     print('Both numbers are equal')
# def OddEven():
#     if (num1 + num2) % 2 == 0: print(f'And the sum of both the numbers is even')
#     else: print(f'And the sum of both the numbers is odd')
#
# OddEven()
#---------------------------------------------

# 🔹 Q5:
# Ask the user to enter marks.
# If marks ≥ 90 → Grade A
# If marks ≥ 75 → Grade B
# If marks ≥ 50 → Grade C
# Else → Fail

# Marks = int(input('Enter Marks: '))
# if  Marks >= 90: print('Grade A')
# elif Marks >= 75: print('Grade B')
# elif Marks >= 50: print('Grade C')
# else :
#     print('Fail')
#-----------------------------------------------

# 🔹 Q6:
# Ask the user to enter a year.
# Check if it is a leap year.

# Rules for leap year:
# Year divisible by 4 and not divisible by 100 → leap year

# Year divisible by 400 → leap year
# Else → not a leap year

# Use if / elif / else to implement this.

# year = int(input('Enter the year : '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(' It is a leap year')
# else :
#     print(' It is not a leap year')
#-------------------------------------------

# 🔹 Q6
# Write a Python program that asks the user to enter a number.

# If the number is divisible by both 3 and 5, print "FizzBuzz".
# # If it’s only divisible by 3, print "Fizz".
# # If it’s only divisible by 5, print "Buzz".
# # Otherwise, just print the number itself.

# num = int(input('Enter a number: '))
# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)
#------------------------------------------
# 🔹9
# Write a Python program that takes three numbers as input and prints out the largest among them.

# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# num3 = int(input('Enter the third number: '))
#
# if num1 > num2 and num1 > num3:
#     print(f'{num1} number is greater')
# elif num2 > num3 and num2 > num1:
#     print(f'{num2} number is greater')
# else :
#     print(f'{num3} number is greater')
#------------------------------------------------
# # 🔹10
# Write a Python program that takes a number as input and checks if it is a prime number or not.
#
# num = int(input('Enter a number: '))
#
# if num <= 1 :
#     print('It is not a prime number')
#
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
#---------------------------------------------------------------------








































































