# day 10
# Taking input user in Python.
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# But input function returns the value as string. *********Hence we have to typecast them whenever required to another datatypE**********

name = input("enter your name :")
print("my name is", name)
#---------------------------------------------------------
x = input("enter first number: ")
y = input ("enter second number: ")
print(x + y) # it will give the output as string automatically or say by default. #remember this.
print(int(x) + int(y)) #But since you typecasted it to integer, it will give the output as integer now!
#--------------------------------------------------------
firstName = input("enter your first name: ")
secondName = input ("enter your second number: ")
print(firstName, secondName) #it will simply print the first name and second name as concatinated strings.

# Excersize 2 ( input program using different operations )
a = input("enter your first number : ")
b = input("enter your second number : ")
print(a+b)
c = input("enter your first number : ")
d = input("enter your second number : ")
print(c + d) # it will give the output as string automatically or say by default.
# if you want to get the output as integer then you have to typecast it.

x = input("enter the first number ")
y = input("enter the second number ")
print( x + y) # not in red becuase + will simply concatinate the strings.
print( x - y)
print ( x * y)
# print ( x / y) # operations wont work without having x y to be typecasted to integers first. that is why it shows in red color.
print( int(x) + int(y))
print( int(x) - int(y))
print ( int(x) * int(y))
print ( int(x) / int(y))
print ( int(x) ** int(y))
print ( int(x) // int(y))
print ( int(x) % int(y)) #great! it worked.