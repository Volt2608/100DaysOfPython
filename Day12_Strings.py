
# Day 11 Strings in python ( String is a sequence of characters enclosed in quotes. Python provides various ways to work with strings. We can use single quotes, double quotes, or triple quotes to define a string.
name = "Alice"
print("Hello, " + name)
#Output : Hello, Alice

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
# Multiline Strings
# If our string has multiple lines, we can create them like this:
a = """this is how you use tripple quotes to
write multiline string in python
and it will print the output as it is"""
print(a)

#Now how do we use double quotes inside a string that is enclosed in double quotes? We can escape the double quotes using a backslash, like this:

x = "He said, \"like 'this\"" #or
# we can use single quotes inside a string that is enclosed in double quotes.
y = 'He said, "like this"'

print (x)
print (y)
# output will be same for both
#-------------------------------------------------------
# [] what is indexing in python [] - Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on. For example, if we have a string "Hello", we can access the first letter "H" using its index 0 by using the square bracket notation: string[0] example below :
name = "jyotika"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7]) # it will throw error as the index is out of range. #remember this.

#for loop in python - when we have to perform indexing of a long string then we use for loop instead of writing the print statement for each index.
# for loop code is below :
for i in name:
  print (i)

# Example of indexing in python using 'for loop' is below :
delhi = '''delhi is the capital of india, it is my home town,
it is poluted however since i spent most
of my childhood here, thats why i love it.'''
for character in delhi:
  print(character)

# ---------------------------------------------------------

#String slicing Day 12

name = "mango is sweet"
print(len(name)) #len() function is used to find the length of the string. output will be 14
print(name[0:5]) #output will be mango
# # python takes the first index as 0 and the last index is excluded. #remember this.

# exercise 3
nm = "Harry"
# len is 5 so if we want to print the last 4 charecters then we have to write the code as below :
print(nm[-4:-2])
print(nm[1:3])
# the output will be ar