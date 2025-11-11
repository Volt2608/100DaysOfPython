
# Without List comprehension :
#
# list = []
# for number in range(11) :
#     if number % 2 == 0: #even
#         list.append(number)
# print(list)

#---------------------------------------------------
# Now With List comprehension :

# Syntax for list comprehension -
# [ Expression, for item in iterable(range, or other), if condition ]

# list1 = [i for i in range(1,11) if i % 2 ==0]
# print(list1)

#-----------------------------------------------------------------------------------------------

# Dictionary without comprehension :

# dict1 = {}
# for number in range(1,11) :
#     if number % 2 == 0 :
#         dict1[number] = number*2
# print(dict1)
#---------------------------------------------------
# Now with Dictionary comprehension :

# syntax for dict comprehension -
# {key : value, for item in iterable, if condition}

# dict2 = { number : number*2 for number in range(1,11) if number % 2 == 0 }
# print(dict2)
#-----------------------------------------------------------------------------------------------------------------

# Dict comprehension practice chatgpt :


# You have a list of words :
# Write one dictionary comprehension to create a dictionary where:
# key = each word
# value = the length of that word


# words = ["apple", "banana", "cherry", "kiwi"]
#
# words1 = { word : len(word) for word in words }
# print(words1)
#-----------------------------------------------------------------------------------------------------------------

# 🔹 Next question: You have a dictionary of numbers, Write a dictionary comprehension
# to create a new dictionary where:
#
# key = the same number
# value = the square of the original value

# nums = {1: 2, 2: 3, 3: 4}
# dict2 = {num : nums[num]**2 for num in nums}
# print(dict2)
#-----------------------------------------------------------------------------------------------------------------

#
# 🔹Next Question: Using one dictionary comprehension, create a dictionary where:

# You have this list:
# Key = the number
# Value = the square of the number
# but only include numbers that are even.

#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# dictEven = { num : num*num for num in numbers if num % 2 == 0 }
# print(dictEven)
#-----------------------------------------------------------------------------------------------------------------

class student:
    def __init__(self,name, rollNum, marks):
        self.name = name
        self.rollNum = rollNum
        self.marks = marks
        self.checkMarks(self.marks)

    @staticmethod
    def checkMarks(marks):
        if marks< 35:
         raise  lowMarksError

class lowMarksError(Exception):
    print("Marks less than 35")

studentObject = student("Rahul",2, 29)




















































