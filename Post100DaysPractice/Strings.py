# Strings
from pandas.core.arrays.categorical import contains

# Take a string input from the user and:
# Print the string in uppercase.
# Print the string in lowercase.

# text = input("Enter a string: ")
#
# print("Uppercase:", text.upper())
# print("Lowercase:", text.casefold())
#--------------------------------------------------------------------------------------------------------

# 2 . Take a string input from the user and
# print the first 3 characters and the last 3 characters of the string.

# text = input("Enter a string: ")
#
# print("First 3 characters:", text[:3])
# print("Last 3 characters:", text[-3:])

#--------------------------------------------------------------------------------------------------------
# 3.
# Take a string input from the user and:
# Count the number of vowels in the string.
# Print the result.

# text = input("Enter a string: ").lower()
# vowels = ('a', 'e', 'i', 'o', 'u')
# count = 0
#
# for char in text:
#     if char in vowels:
#         count += 1
#
# print("Number of vowels:", count)
#--------------------------------------------------------------------------------------------------------
# 4. reverse a string

# text = input("Enter a string: ")
#
# print(text[::-1])
#--------------------------------------------------------------------------------------------------------
# 5.
# Take a string input and count the number of words in the string.

# text = input('Enter a string: ')
# wordsList = (text.split())
# print(len(wordsList))
#--------------------------------------------------------------------------------------------------------
# 6
# Take a string input and:
# Capitalize the first letter of each word (title case).
# Replace all occurrences of the letter 'a' or 'A' with @

# text = input('Enter a string: ')
# print(text.title())
# print(text.replace( "A","@").replace("a","@"))
#--------------------------------------------------------------------------------------------------------

# 7
# Take a string input from the user and count how many times each vowel appears in the string.

# def count_vowels():
#  text = input('Enter a string: ').lower()
#  vowels_dict = { 'a': 0 , 'e': 0 , 'i': 0 , 'o': 0 , 'u': 0 }
#  for item in text:
#    if item in vowels_dict:
#      vowels_dict[item] += 1
#  return vowels_dict
#
#
# result = count_vowels()
# print("Vowel counts:")
# for vowel, count in result.items():
#     print(f"{vowel} - {count} times")

#-----------------------------------------------
# def count_viwels(text):
#     vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#     return vowels_dict


#-------------------------------------------------------------------------------------------------------------------------
# 8 Take a string input from the user and check if it is a palindrome (reads the same forwards and backwards).

# def palindrome():
#   text = input('Enter a string: ').lower()
#   if text == text[::-1]:
#       print("It is a Palindrome")
#   else :
#       print("It is not a Palindrome")
#
# palindrome()
#------------------------------------------------------------------------------------------------------------------
# 9 .
# Take a string input and remove all vowels from it.

# def remove_vowels(text):
#     vowels = "aeiouAEIOU"
#     result = ""
#     for char in text:
#         if char not in vowels:
#             result += char
#     return result
#
# text = input("Enter a string: ")
# string_without_vowels = remove_vowels(text)
# print(f'New sentence : {string_without_vowels}')
#----------------------------------

# 10. Input a sentence as a string . Create a function which accepts this string and returns a new string
# with reversed words

# text = input("Enter a sentence: ")
# SenLen = int(input("Enter the length : "))
#
# def reversedSen(text):
#     return text[::-1].strip(" ")
#
# def reversedWords(text):
#   Words = text.split()
#   reversedWords = " ".join(word[::-1] for word in text.split())
#   return (reversedWords)
#
# def condReverse(text):
#
#     words = text.split()
#
#     ReversedWords = []
#     for letter in words:
#         if len(letter) == SenLen:
#             ReversedWords.append(letter[::-1])
#         else:
#             ReversedWords.append(letter)
#
#     NewsLine = " ".join(ReversedWords)
#     return NewsLine
#
#
# print(reversedSen(text))
# print(reversedWords(text))
# print(condReverse(text))
#---------------------------------------------------------------------------------------------------------
# 11.
# Write a Python function that takes a string and:
# Removes all duplicate characters (but keeps the first occurrence).
# Preserves the order of characters.

# def removeDupeChars():
#     string = input('Enter a string: ').lower()
#     words = string.split()
#     for letter in words:
#         if letter > 1 :
#             words.remove(letter)
#             return ' '.join(words)
#
#
# removeDupeChars()
#---------------------------------------------------------------------------------------------------------------------



































































