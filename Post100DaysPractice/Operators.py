# 🔹 Operators – Q1
#
# Write a program that:
# Takes two numbers as input.
# Performs addition, subtraction, multiplication, and division.
# Prints the results clearly.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
#----------------------------------
# 🔹2
# Write a program that:
#
# Takes two numbers as input.
# Checks and prints:
# Which number is greater (using comparison operators).
# Whether the two numbers are equal or not.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num2 == num1
#     print('Both numbers are equal')
# elif num1 > num2:
#     print(f'{num1} is greater')
# else :
#     print(f'{num2} is greater')

#-------------------------------------
# 🔹3
# Write a program that:
#
# Takes a number as input.
# Checks whether the number is positive and even, positive and odd, or negative.

# num = int(input("Enter a number: "))
#
# if num >= 0 and num % 2 == 0:
#     print("The number is a positive and even")
# elif num >= 0 and num % 2 != 0:
#     print("The number is a positive and odd")
# else :
#     print("The number is a negative number")
#-------------------------------------------------------
# 🔹4  Write a program where you:

# Start with a number (say num = 10).
# Use assignment operators (+=, -=, *=, /=) step by step.
# Print the value of num after each operation.

# num = 10
# print(f"Starting number: {num}")
#
# num += 5
# print(f"After += 5 : {num}")
#
# num -= 3
# print(f"After -= 3 : {num}")
#
# num *= 2
# print(f"After *= 2 : {num}")
#
# num /= 4
# print(f"After /= 4 : {num}")
#---------------------------------------------
# 🔹Q5:
# Write a program that:

# Take two numbers as input and check if number is greater than 100
# and at the same time if their sum is an even number. Print the result accordingly.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > 100 :
#  print(f"{num1} is greater than 100" )
#
# elif num2 > 100 :
#  print(f"{num2} is greater than 100" )
#
# else :
#  print(f"{num1} is less than 100" )
#
# def sum():
#  if (num1 + num2) % 2 == 0 :
#     print(f"The sum of {num1} and {num2} is an even number.")
#
# sum()
#-----------------------------------------------
# 🔹# Write a program that:
#
# Take three numbers from the user.
# Check if the first number is the largest.
# AND if the difference between the second and third number is divisible by 5.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# if num1 > num2 and num1 > num3:
#     print(f'{num1} is larger than {num2} and {num3}')
#
# diff = num2 - num3
# if diff % 5 == 0:
#     print(f'The difference between {num2} and {num3} is divisible by 5')
#---------------------------------------------------------------------------
# 🔹Q6
# Write a program that:
# Checks if the product of the two numbers is greater than 500.
# If it is, print the product.
# Otherwise, print their sum.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 * num2 > 500 :
#     print("The product of both the numbers is: ", (num1 * num2))
# else :
#     print("The sum of numbers is ", (num1 + num2))
#--------------------------------------------------------------------------------------------
# 🔹Q7

# Write a program that takes three numbers as input.
# If the sum of all three numbers is even, print their average.
# Otherwise, print the largest number among them.
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# sumNum = num1 + num2 + num3
# average = (num1 + num2 + num3) / 3
# largestNum = max(num1, num2, num3)
#
# if sumNum % 2 == 0:
#     print(f'Average : {average}')
# else :
#     print(f'The largest number is : {largestNum}')
#--------------------------------------------------------------------------------------------------------
# 🔹Q8
# Write a program that takes 4 numbers as input.
# Find their sum and average.
# If the average is greater than 50, print the difference between the largest and the smallest number.
# Otherwise, print the product of all 4 numbers.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))
#
# sumNum = num1 + num2 + num3 + num4
# averageNum = (num1 + num2 + num3 + num4) / 4
# largestNum = max(num1, num2, num3, num4)
# smallestNum = min(num1, num2, num3, num4)
# DiffNum = largestNum - smallestNum
# productNum = num1 * num2 * num3 * num4
#
# if averageNum > 50 :
#     print(DiffNum)
# else :
#     print(productNum)
#--------------------------------------------------------------------------------------------------------
# 🔹Q9
# write a program that Takes two numbers as input.
# If the first number is divisible by the second, print the quotient.
# Otherwise, print the remainder.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# remainder =  num1 % num2 == 0
# quotient = num1 // num2
#
# if num1 % num2 == 0:
#     print("The quotient is: ", quotient)
# else :
#     print("The remainder is: ", remainder)
#--------------------------------------------------------------------------------------------------------

# 🔹Q10

# Write a program that takes three numbers as input.
# If their sum is divisible by 3 and 5, print "Divisible by both 3 and 5".
# If only divisible by 3, print "Divisible by 3".
# If only divisible by 5, print "Divisible by 5".
# Otherwise, print "Not divisible by 3 or 5".

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# sumNum = num1 + num2 + num3
# if sumNum % 3 == 0 and sumNum % 5 == 0:
#     print("Divisible by both 3 and 5")
# elif sumNum % 3 == 0:
#     print("Divisible by 3")
# elif sumNum % 5 == 0:
#     print("Divisible by 5")
# else :
#     print("Not divisible by 3 or 5")
#--------------------------------------------------------------------------------------------------------













































































































































