# First ---------- Practice file io basics ------------
# Use - to store data while making programs 
# Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.
# to open a file - Use open() function to open a file. It takes two arguments: the name of the file and the mode of file .r .w .a 
#---------------------

# READ FROM A FILE :
# syntax to open a file -
# f = open('myfile.txt', 'r') # opened the file in read mode and stored it in a variable f
# text = f.read() # to read the file
# print(text) # to print the file
# f.close() # always close the file after opening it.
#---------------------

# WRITE TO A FILE :
# syntax to write to a file -
# f = open('myfile.txt', 'w') # opened the file in write mode and stored it in a variable f
# f.write('This is how you write to a file.') # to write to the file
# f.close() # Remember to always close.

# in case of append - 
# f = open('myfile.txt', 'a') # to add to the file
# f.write('This is how you append to a file.') # it will add this line to the file everytime you run the program in append mode.
#----------------------

# The 'with' statement - Alternatively, you can use the with statement to automatically close the file after you are done with it.

# with open('myfile.txt', 'r') as f:
# ... do something with the file
  
  # and you do not need to close *********
#----------------------
# MODES in file 

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
#--------

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
#--------

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
#--------

# create (x): This mode creates a file and gives an error if the file already exists.
#--------

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
#--------

# binary (b): used to handle binary files (images, pdfs, etc).
#----------------------

# METHODS of file -

# readlines() method - The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline() # readline() method reads a single line from the file.
#     if not line:
#         break
#     print(line)
# ----------------------

# writelines() method - The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# f = open('myfile.txt', 'w')
# lines = ['lineOne\n', 'lineTwo\n', 'lineThree\n']
# f.writelines(lines)
# f.close()

# This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.
#----------------------

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()
#-----------------------

# seek() and tell() functions
# Later practice - seek(), tell() and other functions | Python Tutorial - Day #51
#---------------------------------------------------------------------------------------

# @property decorator - getter - setter - deleter - it is used to define a method as a property (it can be accessed like an atttribute/variable). 
# benefit -  When reading, writing or deleting attributes, we can dd additional logic. it gives you getter, setter and deleter methods. 
# Create a Laptop class:, Private attribute _price, Getter to return price, Setter to update price only if it’s greater than 0,  Print "Price updated" when price changes

# class Laptop:
#     def __init__(self, price):  # __init__ is the constructor, automatically called when we create an object.
#         self._price = price # self._price stores the value of price internally (private attribute)

#     @property   # @property turns the method into a getter.
#     def price(self):  
#         return self._price  # getter to return the price

#     @price.setter # setting the price using setter.
#     def price(self, new_price): # new_price is the parameter that we pass to the setter.
#         if new_price > 0:  # if the new price is greater than 0, then update the price.
#             self._price = new_price  # update the price
#             print("Price updated")
#         else:
#             print("Invalid price")

# L = Laptop(20) # Created a Laptop object with _price = 50000.
# print(L.price)   # Printed the price using the getter.
# L.price = 50  # Updated the price to 60000.
# print(L.price)   # Printed the updated price.
# L.price = -1  # Tried to update the price to -1, since it is less than 0, it will print "Invalid price". as we set it in the setter.
#-----------------------------------------------------------------------------------------------------------------
# Day 62 - Access Modifiers in Python - Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
# Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier
#----------
# Public Access Specifier in Python - All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
# class Student:
#   #constructor is defined
#   def __init__(self, age, name):   # perameterized constructor
#       self.age = age               # public variable
#       self.name = name             # public variable

# obj = Student(21,"john")
# print(obj.age)
# print(obj.name) # accessing public data member outside the class will not cause any error.
#----------
# Private Access Modifier
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
# class Student: 
#   def __init__(self, age, name): 
#       self.__age = age      # An indication of private variable

      # def __funName(self):  # An indication of private function
#           self.y = 34
#           print(self.y)

# class Subject(Student):
#   pass

# obj = Student(21,"john")
# obj1 = Subject

# calling by object of class Student
# print(obj.__age)
# print(obj.__funName()) #since these are private member can not be accessed outside the class

# calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName()) #since the function is private it will give error.
# output - 
# AttributeError: 'student' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# AttributeError: 'subject' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'

# name mangling - it is a mechanism used to control the visibility of class attributes, particularly when dealing with inheritance. It's not a strict form of privacy like in some other languages, but it makes it less likely for attributes to be accidentally overridden or accessed from outside the class. 

#purpose - Name mangling primarily helps avoid naming conflicts when working with inheritance. 
# example- 
# class MyClass:
#   def __init__(self):
#       self._nonmangled_attribute = "I am a nonmangled attribute"
#       self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
# In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute
#----------
# Protected Access Modifier
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. 

# to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
# example - 
# class Student:
#   def __init__(self):
#       self._name = "john"

#   def _funName(self):      # protected method
#       return "all goo so far"

# class Subject(Student):       #inherited class
#   pass

# obj = Student()
# obj1 = Subject()

# calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())
#------------------------------------------------------------------------------------------------------------------
# Day 63 - RPS exercise - RPS game using python
# import random

# def check(comp, user):
#   if comp ==user:
#     return 0

#   if(comp == 0 and user ==1):
#     return -1

#   if(comp == 1 and user ==2):
#     return -1

#   if(comp == 2 and user == 0):
#     return -1

#   return 1


# comp = random.randint(0, 2) #this will generate a random number between the given range
# user = int(input("0 for rock, 1 for paper and 2 for sizer:\n"))

# score = check(comp, user)

# print("You: ", user)
# print("Computer: ", comp)

# if(score == 0):
#   print("Its a draw")
# elif (score == -1):
#   print("You Lose")
# else:
#   print("You Won")
#---------------------------------------------------------------------------------------------------------------------------

# Day 64 - Exercise 6 Solution - Library class - refer to day 64 - Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

# class Library:

#     def __init__(self): 
#         self.no_of_books = 0  # Created instance attribute and set it to 0. This will track how many books the library has. 
#         self.books = [] # Created instance attribute books & initialized it as an empty list. This will store book titles.              
#     def add_book(self, book):  # created method addBook - that takes one argument book, in addition to self.
#         self.book = book # stored the value of book as self.book
#         self.books.append(book)  # in the list of books append book
#         self.no_of_books = len(self.books)  # update the number of books with the length of the list of books.

#     def showbooks(self):
#         print(f"The library has the following books: {self.no_of_books}")     # prints the number of books
#         for i in self.books: #for loop to iterate over the list of books counter i (iterable)
#             print(i)

# obj = Library()            # created an object of the class Library and named it obj.
# obj.add_book(" Mystery")  # calling the method by typing - ( object dot method name ) and passed the argument "Mystery"
# obj.add_book(" Thriller") # calling the method by typing - ( object dot method name ) and passed the argument "Thriller"
# obj.add_book(" Romance")  # calling the method by typing - ( object dot method name ) and passed the argument "Romance"
# obj.showbooks()   # calling the method by typing - ( object dot method name )

#---------------------------------------------------------------------------------------------------------
# Day 65 - Static Methods in Python - A static method in Python is a method inside a class that Belongs to the class, not to a specific object (instance) it Doesn’t need self because it doesn’t work with instance variables.Can be called using the class name or an object.Is mostly used for utility/helper functions related to the class.

# # example - 
# class MathHelper:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(MathHelper.add(5, 3)) # Calling by using the class name
# # Output: 8

# obj = MathHelper() # Calling using object (also works)
# print(obj.add(10, 2))  # Output: 12
#---------------------------------------------------------------------------------------------------------
# OOPS - Object Oriented Programming - It is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods).

# Below are the examples of default constructor and parameterized constructor in python.

# class employee1:       # Defines a new class named employee1.
#     def __init__(self, name):  # init contsructor is called when an object is created automatically.
#         self.name = name   # Stores the arguement name as self.name
#     def showdetails(self):  # method to show details
#         print(f"Thne name of the emploee is {self.name}")  # pritns
        
# obj = employee1("Volt")  # created an object of the class employee1 and named it obj.
# obj.showdetails()  #calling the method by typing - ( object dot method name )
# #----------------------------------------------------------------------------------------------------------
# class employee: # class ctreated 
#     def __init__(self):    # default constructor
#       self.name = "Volt"    # we have to give the value of name as no arguments are passed in default one.
#     def showdetails(self):   # method to show details
#         print(f"Thne name of the emploee is {self.name}")  #prints
        
# obj = employee() # created an object of the class employee, and named it obj.
# obj.showdetails() # calling the method by typing - ( object dot method name )
# employee.showdetails(obj) # we can also call the method by typing - ( class name dot method name and passing the object name as an argument)
#----------------------------------------------------------------------------------------------------------

# Day 66 - Instance vs class variables - In Python, variables can be defined at the class level or at the instance level. uderstanding them both is important for writing and understanding the dode. 

# Class Variables - defined outside of any methods of the class.

# 1. Class variables are defined at the class level and are shared among all instances of the class. 
# 2. They are defined outside of any method and are usually used to store information that is common to all instances of the class. 

# example of class variable -
# class MyClass:
#     class_variable = 0  # ******CLASS VARIABLE******* 

#     def __init__(self):     # method to increment the class variable
#         MyClass.class_variable += 1   # incrementing the class variable by 1

#     def print_class_variable(self):
#         print(MyClass.class_variable)         # method to prints the class variable


# obj1 = MyClass()              # object 1 created
# obj2 = MyClass()              # object 2 created

# obj1.print_class_variable()    # calling the method by typing - ( object dot method name )
# # Output: 2
# obj2.print_class_variable()    # calling the method by typing - ( object dot method name )
# # Output: 2
#------------------

# Instance Variables - defined inside of the init method or inside of any other method of the class.

# 1. Instance variables are defined at the instance level and are unique to each instance of the class. 
# 2. They are defined inside the init method and are usually used to store information that is specific to each instance of the class.

# # example of instance variable -
# class MyClass:            
#     def __init__(self, name):          # perameterized constructor
#         self.name = name                # stored the value of name as self.name

#     def print_name(self):               # method to print the name
#         print(self.name)

# obj1 = MyClass("John")                   # object 1 created with ''' john instance variable ''
# obj2 = MyClass("Jane")                   # object 2 created with '' jane instance variable ''

# obj1.print_name()          # calling the method by typing - ( object dot method name )
# # Output: John
# obj2.print_name()          # calling the method by typing - ( object dot method name )
# # Output: Jane

# # In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.
#----------------------------------------------------------------------------------------------------------
# Day 68 - Exercise 7 - Clear the Clutter - Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. 

# For example:
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

# first I downloaded some pngs and jpegs and saved them in a folder named clutter. then I ran the following code:

# import os

# Lst_Files = os.listdir("ClutteredFolder") 
# i = 1  # start counter

# for file in Lst_Files:
#     if file.endswith(".png"):
#         old_path = f"ClutteredFolder/{file}"   # old file path
#         new_path = f"ClutteredFolder/{i}.png" # new file path

#         os.rename(old_path, new_path)  # rename file
#         print(f"Renamed: {file} -> {i}.png")

#         i += 1


# os.listdir("path") # returns a list of all the files, folders 4 D given path.
# os.rename(sourc, destination) # renames the file from source to destination.) 
#----------------------------------------------------------------------------------------------------------------------------
# Day 69 - Class Methods in Python - Allows operations related to the class itself, not instances.

# They takes 'cls' as the first argument instead of 'self'. self reffers to any obj created from that class. 
# unlike cls
# cls represents the class itself 

# Syntax -        @classmethod
# just above the def () Method 

# Example - 
# class Student:
#     count = 0 
    
#     def __init__(self, name, gpa):        #constructor to increase the count of students
#         self.name = name 
#         self.gpa = gpa
#         Student.count += 1

#     # INSTANCE METHOD
#     def getInfo(self):
#         return f"{self.name} has a GPA of {self.gpa}"

#     # CLASS METHOD
#     @classmethod
#     def getCount(cls):
#         return f"There are {cls.count} students in the class."

# student1 = Student("Volt", 60)
# print(Student.getCount())
#--------------------------------------------------------------------------------------------------------------------------------------------
# Day 70 - Class Methods as Alternative Constructors - When you are provided the data in different methods - for example strings.
# so first you have to convert it into the required format and then use it with the help of class methods as alternative constructors.

# In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

# However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

# A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:

# class Person:
  # def __init__(self, name, age):
  #     self.name = name
  #     self.age = age
#-------------------------------
# But what if you want to create a Person object from a string that contains the person's name and age, separated by a comma? You can define a class method named "from_string" to do this:

# class Person:
  # def __init__(self, name, age):
  #     self.name = name
  #     self.age = age

  # @classmethod
  # def from_string(cls, string):
  #     name, age = string.split(',')
  #     return cls(name, int(age))

# rectangle = Rectangle.square(10)   # Now you can create a square rectangle like this.
#----------------------------------------------------------------------------------------------------------------------------------------
# Day 71. 
# dir(), __dict__() and help() attribute/methods in python - They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). 

# 1. The dir() method - This function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. Example:

# x = [1, 2, 3]
# print(dir(x))                     # tells you what you can do with the list x.
# output - ['__add__', '__class__', '__class_getitem__' etc.

#-----------------

# 2. The __dict__ attribute - This attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example:

# class Person:
#    def __init__(self, name, age):
#          self.name = name
#          self.age = age
# p = Person("John", 30)
# print(p.__dict__)            # __dict__ returns a dictionary representation of the object's attributes.
#------------------

# 3. The help() mehthod - This function is used to get help documentation for an object, including a description of its attributes and methods. Example:

# class Person:
#    def __init__(self, name, age):
#          self.name = name
#          self.age = age


# p = Person("John", 30)
# print(p.__dict__)   


# help(Person)
#------------------
# help() - you can enter the name of any module, keyword, or topic to get help on writing Python programs and using Python modules.  To get a list of available modules, keywords, symbols, or topics, enter "modules", "keywords","symbols", or "topics".
#------------------------------------------------------------------------------------------------

# Day 72 - Super function in Python - it is a shortcut that lets a child class call methods from its parent (superclass). 

# or can say that it is used to give access to the methods of a parent class. it returns a temporary object of a parent class when used.

# Syntax - super().__init__(args) no self required in super() or any method where you want to extend or override parent class functionality.

# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       print(f"Person: {self.name}, {self.age} years old")

# class Employee(Person):
#   def __init__(self, name, age, employee_id, salary):
#       super().__init__(name, age)    # Call Parent constructor with its arguments
    
#       self.employee_id = employee_id # Add Employee's own properties
#       self.salary = salary
#       print(f"Employee: ID={self.employee_id}, Salary={self.salary}")

# emp = Employee("Alice", 30, "E123", 50000)  # Create Employee object

#------------------------
# Example of super() 
# class Parent:
#   def show(self):
#       print("This is Parent show()")

# class Child(Parent):
#   def show(self):
#       super().show()   # calls Parent's show()
#       print("This is Child show()")

# c = Child()
# c.show()


# So super() is not limited to __init__.
# You can use it in any method where you want to extend or override parent class functionality.
#--------------------------------------------------------------------------------------------------------

# Day 73 - Magic/Dunder Methods in Python - Dunder method (double underscore) these are the special methods ex - __init__() , __str__(), __len__() etc. They are automatically called by many of python's built- in operations. They allow developers to define or customize the behavior of objects. 

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#         return self.num_pages > other.num_pages

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author

#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"Key '{key}' was not found"

# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
# book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book1)  # Calls __str__
# print(book1 == book3)  # Calls __eq__
# print(book1 < book2)  # Calls ___lt__
# print(book2 > book3)  # Calls __gt__
# print(book1 + book2)  # Calls __add__
# print("Lion" in book3)  # Calls __contains__
# print(book3['title'])  # Calls __getitem__
#--------
# __call__ - Normally, in Python, functions can be called like f().

# objects are not usually callable. But if you define the __call__ method inside a class, then its objects become callable like function. That means you can “call” an object just like you call a function.
# example - 

# class Logger: # created a class Logger which will act like a wrapper around any function we pass in.
#   def __init__(self, func):  
#       self.func = func  #It stores this function in self.func 

#   def __call__(self, *args, **kwargs):   # This makes objects of Logger callable like functions.
#       print(f"Calling {self.func.__name__} with args={args}, kwargs={kwargs}")                      # *args → collects positional arguments. 
#       result = self.func(*args, **kwargs)  # Calls the original function (self.func) with the given arguments.                                   # **kwargs → collects keyword arguments.
    
#       print(f"Result: {result}")    # Shows what the function returned.
#       return result  # Returns the result back, so the wrapped function behaves normally.

# # Example function
# def add(a, b):
#   return a + b

# logged_add = Logger(add)  # creates a Logger object, passing the add function into it.
# logged_add(2, 3)  # calls __call__
#--------------------------------------------------------------------------------------------------------------------------------------------

# Day 74 - Method Overriding in Python - 
# Example - 

# class Animal:
#   def sound(self):
#       print("Animals make sound")

# class Dog(Animal):
#   def sound(self):   # overriding the parent's method
#       print("Dog barks")

# d = Dog()
# d.sound()  # calls Dog's sound() method
# # you simply make a method in the child class with the same name as the parent class method to override it.
#----------- Method overriding with super() -----------Example ------------
# class Shape:     # parents class 
#   def area(self):    # method of area in parent class
#       print("Calculating area...")

# class Circle(Shape):  # subclass of shape (child class)
#   def __init__(self, radius):     # constructor of child class
#       self.radius = radius  # storing the value of radius as self.radius

#   def area (self):   # "" OVERRIDING "" parent's area() method by making a method with the same name in child class
#       print("Calculating area of a circle...")  # prints
#       super().area()   # calls parent's area() method
#       return 3.14 * self.radius * self.radius  # returns the area of the circle

# c = Circle(5)    # created an object of the class Circle and named it c.
# print("Area:", c.area())  # calling the method by typing - ( object dot method name ) 
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Day 75 - Refer to Day 68 - Exercise 7 - Clear the Clutter - 

# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# - sfdsf.png --> 1.png
# - vfsf.png --> 2.png
# - this.png --> 3.png
# - design.png --> 4.png
# - name.png --> 5.png
# ---------------------_SOL------ IN DAY 68-----------------------------------------------------------------------

# import os

# Lst_Files = os.listdir("ClutteredFolder") 
# i = 1  # start counter

# for file in Lst_Files:
#     if file.endswith(".png"):
#         old_path = f"ClutteredFolder/{file}"   # old file path
#         new_path = f"ClutteredFolder/{i}.png" # new file path

#         os.rename(old_path, new_path)  # rename file
#         print(f"Renamed: {file} -> {i}.png")

#          i += 1
     
# output :
# Renamed: 1.png -> 1.png
# Renamed: 2.png -> 2.png
# Renamed: 3.png -> 3.png
# Renamed: 4.png -> 4.png
# Renamed: 5.png -> 5.png

#-------------- Conclusion-------------to sol-------day 68--------------
# first I downloaded some pngs and jpegs and saved them in a folder named clutter. and import is module that is used for file manipulation.

# then I ran the above code.
# -----------------------------------------------------------------------------------------------------------------------------------
# Day 76 - Merge the PDF using pypdf, it is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

# Functions and classes from pypdf that helps you while working on PDF merging:

# PdfReader → for reading an existing PDF file.
# PdfWriter → for creating a new PDF or combining multiple PDFs.
# add_page() → to add a page to your PdfWriter.
# append() → to add all pages from another PDF.
# merge_page() → to overlay one page on top of another
# pages attribute → lets you iterate over all pages in a PDF.
# getPage() / pages[i] → to access a specific page.
# write() → to save the final merged output into a file.

#  TO MERGE PDFs - always check basic example of os module site before using it. Since these are timely renaed or updated. 

# from pypdf import PdfWriter

# merger = PdfWriter()

# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

#-------------Keys to remember----------------------------

# pdfs = ["pdf1","pdf2","pdf3"]    

# # Creates a list of PDFs in the order you want, remember to include the path [f"{folder}/pdf1", f"{folder}/pdf2", f"{folder}/pdf3"]

# writer = PdfWriter()  # Creates a PdfWriter object 

# for pdf in pdfs:
#     reader = PdfReader(pdf)  # Read each PDF
#     for page in reader.pages:
#         writer.add_page(page)  # Add each page to the writer

# with open("merged.pdf", "wb") as output_file:
#     writer.write(output_file)  # Writes the merged result into merged.pdf.

#--------------------------------------------Self------------------------------------------------------------------

# Method overloadind - 

# 1. it means we are defining multiple methods with same name but different parameters within the same class. 
# 2. it is considered as a feature of complile time polymorphism. since the which method is to used is desided during compile time.
# 3. it occurs within the same class, as we have all the methods in the same class. although it is not supported in python.
# 4. Method must have the same name but different parameters.


# Pyhton does not support method overloading but it supports method overriding. However we can achieve method overloading by using default arguments/ variable-length arguments or *args.
#-----------------------------------------EXAMPLE OF METHOD OVERLOADING IN PYTHON-------------------------------------------

#               METHOD OVERLOADING USING DEFAULT ARGUMENTS | = 0 (DEFAULT ARGUMENT)
# class plus:
#   def add(self, a, b, c= 0):  # we set it to default 0 so that it can take 2 or 3 arguments.
#     return(a + b + c)

# obj = plus()
# print(obj.add(1, 9))
# We can run it with 2 or 3 arguments since we set the c as defualt. 

#------------------ Now example with *args ----------------------------
# *args = means “accept any number of positional arguments”; inside the function, will be a tuple of all the positional arguments passed in.


# class demo:
#   def add(self, *args):  
#     total = 0
#     for i in args:
#       total = total + i
   
#     total = 0
#     for i in args:                 # i = argument one by one at a time
#       total = total + i            # total = total (0) + argument 
#     return total                   # return the total
      
# obj = demo()
# print(obj.add(2, 3))
# print(obj.add(8,9,5,2,3,4))
# print(obj.add(1,2,3,4,5,6,7,8,9,10))

#-------------REMEMBER-------------

# tuple - A collection of items or values. Tuple are created by adding comma separated values inside parentheses ( ) Python tuple are immutable wherein once values are added to tuple, they can't be changed.

#---------------------------------EXAMPLE OF METHOD OVERRIDING IN PYTHON----------------------------------------------------------------

# # 1. Where as method overriding is a feature of run time polymorphism. since which method is to be called is decided during run time. 
# 2. It is implimented in inheritenc as when we need to have parents and child class for this one.
# 3. It occurs in two classes, it occurs in inheritance, there should be a parent class and a child class. 
# 4. Method must have the same name and same parameters.
  
# class Father:
#   def sleep(self):
#     print("sleeps from 10 pm to 6 am")

#   def eat(self):
#     print("eats lunch at 2 pm")

# class child(Father):
#   def sleep(self):                          # overriding the parent class sleep method 
#    print("sleeps from 2 am to 11 am")
#    super().eat()                         # calling the parent class eat method using super()
#    super().sleep()                        # calling the parent class sleep method using super()
    
# c = child()           # object of child class created
# c.sleep()     # child class sleep method is called 

# since child class method has parents class method inherited in the def, so it will be called like that, mentioned line by line below:

# sleeps from 2 am to 11 am    -  child class sleep method prints in first line 
# eats lunch at 2 pm     -  parent class eat method prints in second line since we called it using super()
# sleeps from 10 pm to 6 am  -  parent class sleep method prints in third line since we called it using super() 
#-------------------------------------------------------------------------------------------------------------------------------------

# Day 77 - Operator Overloading in Python: An Introduction 

# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.


# Why do we need operator overloading?

# Operator overloading allows you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:
#-------------------------------------

# How to overload an operator in Python?

# You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:

# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# < : __lt__
# > : __gt__
# == : __eq__
#-------------------------------------

# For example, if you want to overload the + operator to add two instances of a custom class, you would define the add method:
# class Point:
#   def __init__(self, x, y):
#       self.x = x
#       self.y = y

#   def __add__(self, other):
#       return Point(self.x + other.x, self.y + other.y)
    

# CONCLUSION FOR OPERATION OVERLOADING -

# Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code. By redefining the behavior of mathematical and comparison operators for custom data types, you can write code that is both concise and expressive. However, it's important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.
#----------------------------------------------------------------------------------------------------------------------

# Day 78 - Single Inheritance in Python --------MOST COMMON TYPE OF INHERITANCE-------

# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

# Syntax - 

# class ChildClass(ParentClass):
#   # class body

# class Animal:
#   def __init__(self, name, species):
#       self.name = name
#       self.species = species

#   def make_sound(self):
#       print("Sound made by the animal")

# class cat(Animal):
#   def __init__(self, name, breed):
#       self.name = "Kitty"
#       self.breed = "Persian"
#       self.species = "cat"

#   def eats(self):
#       print("cat eats fish")
    
#   def make_sound(self):
#       print("meow")
#       super().make_sound()

#   def cat_details(self):
#     print(f"Name: {self.name}, Breed: {self.breed}, Species: {self.species}")
    
# c = cat("Kitty", "Persian")
# c.cat_details()
# c.make_sound()

#----------------------------------------------------------------------------------------------------------------------------

# Day 79 - MULTIPLE INHERITANCE IN PYTHON

# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

# Syntax
# In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

# class ChildClass(ParentClass1, ParentClass2, ParentClass3):                    
  # class body 

# Example

# class Animal:         # parent class 1
#   def __init__(self, name, species):
#       self.name = name
#       self.species = species

#   def make_sound(self):
#       print("Sound made by the animal")

# class Mammal:         # parent class 2
#   def __init__(self, name, fur_color):
#       self.name = name
#       self.fur_color = fur_color

# class Dog(Animal, Mammal):           # child class inherits from both parent classes animal and mammal
#   def __init__(self, name, breed, fur_color):
#       Animal.__init__(self, name, species="Dog")
#       Mammal.__init__(self, name, fur_color)
#       self.breed = breed

#   def make_sound(self):
#       print("Bark!")
#       super().make_sound

# d = Dog("Buddy", "Golden Retriever", "Golden")
# d.make_sound()

# In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.

# class A:   # Base class (parent of all)
#   def show(self):
#       print("show from Class A")

# class B(A):   #  Child of A
#   def show(self):
#       print("show from Class B")
      
# class C(A):   #  Child of A
#   def show(self):
#       print("show from Class C")
#       super().show()  # it calls the show method of the parent class A

# class D(B, C):   # Child of B and C (so indirectly of A too)
#   pass 

# d = D()       #  Create object of D (grandchild class)
# d.show()
# print(D.mro())  # output - [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#-----------------MRO--------------UNDERSTANDING-----------Method Resolution Order---------------









#----------------------------------------------------------------------------------------------------------------------------
# DAY 80 - MULTIL LEVEL Multi-level inheritance is when a class is derived from another derived class.

# Think of it like a chain of inheritance.

# The child class inherits from the parent, and then another child inherits from that child.

# # Base class (Grandparent)
# class Animal:
#     def eat(self):
#         print("Animal can eat")

# # Derived class (Parent)
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal can walk")

# # Derived class (Child)
# class Dog(Mammal):
#     def bark(self):
#         print("Dog can bark")

# # Create an object of Dog
# d = Dog()
# d.eat()    # from Animal
# d.walk()   # from Mammal
# d.bark()   # from Dog

#------------------------------------------------------------------------------------------------------------------------

# Day 81 - Hybrid Inheritance in Python meansn simple inheritance + multiple inheritance = hybrid inheritance.

# ______________  TYPES OF INHERITANCE ________________

# single/simple inheritance - A child class inherits from only one parent class.

# parentClass -> ChildClass

# class Parent:
#   def method1(self):
#       print("Method from Parent")

# class Child(Parent):
#   def method2(self):
#       print("Method from Child")

#----------------------------------

# Multiple Inheritance - A child class inherits from multiple parent class.

# parentClass1 -> ChildClass 
# parentClass2 -> ChildClass

# class Parent1:
#   def method1(self):
#       print("Method from Parent1")

# class Parent2:
#   def method2(self):
#       print("Method from Parent2")

# class Child(Parent1, Parent2):
#   def method3(self):
#       print("Method from Child")
#------------------------------------

# Multilevel Inheritance - A class inherits from a class that is itself derived from another class, forming a chain.

# parentClass -> ChildClass -> GrandChildClass

# class Grandparent:
#   def method_gp(self):
#       print("Method from Grandparent")

# class Parent(Grandparent):
#   def method_p(self):
#       print("Method from Parent")

# class Child(Parent):
#   def method_c(self):
#       print("Method from Child")
#------------------------------------

# Hierarchical Inheritance -  '' Multiple child classes '' inherit from a single parent class.

# parentClass -> ChildClass1
# parentClass -> ChildClass2

# class Parent:
#   def common_method(self):
#       print("Common method from Parent")

# class Child1(Parent):
#   def method1(self):
#       print("Method from Child1")

# class Child2(Parent):
#   def method2(self):
#       print("Method from Child2")
# #------------------------------------

# Hybrid Inheritance - A combination of two or more of the above types of inheritance.
#-------------------------------------------------------------------------------------------------------------

# Day - 82 - Refer to Day - Day 76 - SOLUTION ---- Merge the PDF using pypdf, it is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
#-----------------------------------------------------------------------------------------------------------------

# Day 83 - Exercise ------Shoutout to everyone-------

# Write a program to pronounce list of names using upm add pywin32win32 API on wondows. If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, try to figure out how to do the same thing using some other package

#-----------------------------------------------Sol-----------------------------------------------------

# installed pyttsx3 pyobjc

# import pyttsx3

# engine = pyttsx3.init()
# engine.say(" Shout out to me for being consistent for more than 80 days")
# engine.runAndWait()
#-----------------------------------------------------------------------------------

# Or the easiest way for MAC

# from os import system
# system(' say you have completed 83 days yeeyyy! ')
#-----------------------------------------------------------------------------------------------------------------
# DAY 84 - The time Module in Python

# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios.

# time.time()  - Returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 (UTC)).
# example - 
# import time
# print(time.time())
# Output: 1755952135.9822147


# This brings in Python’s built-in time module, which lets you work with dates, times, and clocks.

# Without importing it, you can’t use time.localtime() or time.strftime().

#--------------

# time.sleep() - This function suspends the execution of the current thread for a specified number of seconds. It takes a single argument, which is the number of seconds to sleep.

# Usage - This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. 

# Here's an example:

# import time

# print("Start:", time.time())
# time.sleep(3)
# print("End:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376

#---------------

# time.strftime() - This  function formats a time value as a string, based on a specified format.

# usecase - for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. 
# example - 

# import time  
# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(formatted_time)

# Output: 2025-08-23 18:09:17

#-----------------Points to remember while using time module in python----------------------------

# First offf Import the time module - import time

# ------------- t = time.localtime()   --------------
# created a variable t and stored the value of time.localtime() in it.


# above variable time.localtime() gives you the current local date and time (according to your computer’s clock).

# It returns a struct_time object (like a container) with year, month, day, hour, minute, second, etc.

# Example: time.struct_time(tm_year=2025, tm_mon=8, tm_mday=23, tm_hour=18, tm_min=12, tm_sec=45, ...) We need to conver this into string format to read it. and that why we use time.strftime() function. after using localtime() function.

#----------------- time.strftime() ---------------------

# time.strftime() means “string format time”.
# It takes two things:
# 1. The time object (t) you want to format.

# Together, it converts the time into a nice readable string like:
# "2025-08-23 18:12:45"
#--------------------------------

# Conclusion
# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. Whether you are writing a script, a library, or an application, the time module is a powerful tool that can help you perform time-related tasks with ease and efficiency.
#-----------------------------------------------------------------------------------------------------------------------------

# Day 85 - Creating command line utility in python 

# A command line utility is just a Python program that you run from the terminal/command prompt instead of clicking it like an app.
# It usually accepts commands, options, and arguments from the user and then performs some task.

# Example:  ls -l       # Here ls is a command line utility that lists files, and -l is an option. 
#----------------

# Why use Python for command line utilities?

# Python is great for making CLI (Command Line Interface) tools because It’s easy to handle arguments (sys.argv or argparse).

# Cross-platform (works on Mac, Linux, Windows). Lots of libraries to make powerful tools quickly.
#----------------------------------------------------------------------------------------------------------------

# Day 86 - Walrus Operator
# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Here's an example of how you can use the Walrus Operator in a while loop:

# numbers = [1, 2, 3, 4, 5]

# while (n := len(numbers)) > 0:       # if the length of the list is greater than 0
    # print(numbers.pop())              # print the last element of the list   
  
# pop() removes the last element of the list and returns/prints it.
#-----------------
# example 2 


# names = ["John", "Jane", "Jim"]

# if (name := input("Enter a name: ")) in names:      
#     print(f"Hello, {name}!")
# else:
#     print("Name not found.")
#-------------------
# example 3

# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)

# In this example, the user input is assigned to the variable name using the Walrus Operator. The value of name is then used in the if statement to determine whether it is in the names list. If it is, the corresponding message is printed, otherwise, a different message is printed.

# It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.

# In conclusion, the Walrus Operator is a useful tool for Python developers to have in their toolkit. It can help streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability.
#----------------------------------------------------------------------------------------------------------------------------

# Day 87 - Shutil Module in Python - this module that provides a higher level interface for working with file and directories. 

# The name "shutil" is short for shell utility. 

# It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. 
#-----------------

# First off Importing shutil                  ""INBUILT MODULE""
#-----------------

# --------------------------------- SHUTIL MODULE FUNCTIONS -----------------------------------------

# 1. shutil.copy(src, dst) - This function copies the file located at src to a new location specified by dst. If dst is a directory, a new file with the same name will be created in

# 2. shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

# 3. shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

# 4. shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

# 5. shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.
# ---------------

# Examples

# import shutil

# shutil.copy("src.txt", "dst.txt") # Copying a file

# shutil.copytree("src_dir", "dst_dir") # Copying a directory

# shutil.move("src.txt", "dst.txt") # Moving a file

# shutil.rmtree("dir") # Deleting a directory

# In conclusion, the shutil module is a powerful tool for automating file and directory-related tasks in Python. Whether you are a beginner or an experienced Python developer, the shutil module is an essential tool to have in your toolbox.
#----------------------------------------------------------------------------------------------------------------------------

# Day 88 - Day 83 - Exercise ------Shoutout to everyone------- Refer to day 83 
#----------------------------------------------------------------------------------------------------------------------------

# Day 89 - Request Module in Python - The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.

# FIRST OFF - Install requests module - pip install requests
# Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:

#  GET REQUEST - 
# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

# POST REQUEST - Here is another example that sends a POST request to a web service and includes a custom header:

# import requests

# url = "https://api.example.com/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Content-Type": "application/json"
# }
# data = {
#     "username": "myusername",
#     "password": "mypassword"
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

# In this example, we send a POST request to a web service to authenticate a user. We include a custom User-Agent header and a JSON payload with the user's credentials.

#---------------

# bs4 Module        - beautiful soup 4 -  

# There is another module called BeautifulSoup which is used for web scraping in Python. 

# Is a Python library for parsing HTML and XML documents. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.
#---------------------------------------------------------------------------------------------------------------------------

# DAY 90 NewsAPI in Python ------------------- EXERCISE ---------------------
# The requests module in Python is a popular and user-friendly HTTP library designed to simplify the process of sending HTTP requests. It abstracts away the complexities of interacting with web services and APIs, making it straightforward to perform operations like fetching web pages, submitting forms, and interacting with RESTful APIs. 

# Key Features and Usage: Sending HTTP Requests: requests supports various HTTP methods, including GET, POST, PUT, DELETE, PATCH, and HEAD.
#------------------------------  
# EXERCISE - 

# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application


# import requests 
# import json

# query = input("What type of news are you interested in? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-01&sortBy=publishedAt&apiKey=d90631fb356541dda2030654044c6f0d"
# r = requests.get(url)

# news = json.loads(r.text)
# print(type(news))

# for article in news["articles"]:
#   print(article["title"])
#   print(article["description"])
#   print()
  
#----------------------------------------------------------------------------------------------------------------------------

# Day 91 Generators in Python - 

# Generators in Python are special type of functions that allow you to create an iterable sequence of values. 
# A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
#------------

#  -------MAIN -----
# Creating a Generator
# In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. Here's an example:

# example -
# def my_generator():
#   for i in range(5):
#       yield i

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # Output:
# 0
# 1
# 2
# 3
# 4
# in this example, the generator function my_generator() returns a generator object, which can be used to generate the values in the range 0 to 4. The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.

# The generator can be used in a for loop, just like any other iterable sequence. The generator is used to generate the values one-by-one as the loop iterates over it.
#----------------THEORY ABOUT GENERATORS-------------------

# Benefits of Generators
# Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

# Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.

# Conclusion
# Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit. So, if you haven't already, be sure to check out generators in Python and see how they can help you write better, more efficient code.
#----------------------------------------------------------------------------------------------------------------------------

# Day 92 - Function Caching in Python
# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

# In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.

# example - 
# import functools  # This module provides higher-order functions and decorators for functional programming.

# @functools.lru_cache(maxsize=None)   # decorator applied to the function fib() to cache its results.
# def fib(n):                             # fib stands for fibonacci sequence func
#     if n < 2:                                # Base condition for recursion.
#         return n   # Executes only when n is 0 or 1. Prevents infinite recursion by giving a stopping point.
    # return fib(n-1) + fib(n-2)     #formula to calculate fibonacci sequence.

# print(fib(20))

#----------------------- Points to remember -------------------------
# lru_cache stands for Least Recently Used Cache. It remembers (caches) the results of function calls so the same calculation isn’t repeated.
# maxsize=None means unlimited cache (store all results).

# Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... Base condition for recursion. If n is 0 → return 0. If n is 1 → return 1. These are the first two Fibonacci numbers.

#-----------------

# As you can see, the functools.lru_cache decorator is used to cache the results of the fib function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.
#-----------------

# Conclusion
# Function caching is a technique for improving the performance of a program by storing the results of a function so that you can reuse the results instead of recomputing them every time the function is called. In Python 3, function caching can be achieved using the functools.lru_cache decorator, which provides an easy and efficient way to cache the results of a function. 
#----------------------------------------------------------------------------------------------------------------------------
 
# Day 93 Solution to Exercise 9 - Refer to Day 90 - NewsAPI in Python ------------------- EXERCISE ---------------------
#----------------------------------------------------------------------------------------------------------------------------

# Day 94 - Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

# from os import system 
# import time
  
# def waterReminder():
#     while True:          
#       time.sleep(2)   
#       system(' say hello, it is time to drink water')
      
# waterReminder()
#----------------------------------------------------------------------------------------------------------------------------

# Day 95- Regular Expressions in Python 

# Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# First off - import re module - import re                  --------------INBUILT MODULE-----------

#----------------- Metacharacters in regular expressions-----------------------------
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs
#--------------------------------------------------------------
# Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
#--------------------
# re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. We can use re.search method like this to search for a pattern in regular expression:

# Searching for a pattern in re using re.search() Method - 
# example - 

# import re

# pattern = r"expression"      # Define a regular expression pattern

# text = "Hello, world!"       # Match the pattern against a string can be a peragraph or a sentence or a word.

# match = re.search(pattern, text)      # Search for the pattern in the text

# if match:
#     print("Match found!")
# else:
#     print("Match not found.")
# output - Match not found.  

#-----------------------------

# Uuse the re.findall function to find all occurrences of the pattern in a string:
# example -

# import re
# pattern = r"(cat|hat)"            # define the expression pattern you need to fine in r string.
# text = "The cat is in the hat."       # define the text in which you want to find the pattern.

# matches = re.findall(pattern, text)       # Find all occurrences of the pattern in the text

# print(matches)
# Output: ['cat', 'hat']
#------------------------------
# visit - https://regexr.com/ 
# to practice more on regular expressions.

# visit - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# to get the complete list of meta characters in regular expressions.
#----------------------------------------------------------------------------------------------------------------------------

# Day 96 - AsyncIO in Python - Asynchronous I/O, (input/output) or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

# Syntax -  first off import asyncio
# import asyncio

# async def my_async_function():        # async function named my_async_function
  
    # await asyncio.sleep(1)       # await means wait for the asyncio.sleep(1) to complete before moving to the next line.
    # return "Hello, Async World!"        # return the string "Hello, Async World!"

# async def main():             
#     result = await my_async_function()
#     print(result)

# asyncio.run(main())
#---------------CONCLUSION-----------------------------ASYN----IO------------------------

# Async IO in Python is a module that lets you run tasks at the same time without blocking each other.

# Instead of waiting for one thing to finish (like downloading a file or waiting for 1 second), your program can pause that task, go do something else, and then come back when it’s ready.
#----------------------------------------------------------------------------------------------------------------------------
# couldnt get harrys version of day 97 so bro code way -

# Day 97 - MUTLITHREADING IN PYTHON - Used to perform multiple tasks concurrently (multitasking) it is Good for I/O bound tasks like reading files or fetching data from APIs

# import threading
# import time 

# def Walk_Dog():
#     time.sleep(4)
#     print("you walked the dog")

# def takeOutTheTrash():
#     time.sleep(3)
#     print("you took the trash out")

# def getMail():
#    time.sleep(2)
#    print("you got the mail")

# Walk_Dog()
# takeOutTheTrash()
# getMail()

# print("-----------------") # Total time here = 4 + 3 + 2 = 9 seconds, because they run one after another.

# now in order to run these tasks concurrently, we can use threading module - 
# so first create thread objects for each task - 

# chore1 = threading.Thread(target=Walk_Dog)        # Creates 3 separate thread objects, each assigned to one chore. # this is chore 1 
# chore1.start()  

# chore2 = threading.Thread(target=takeOutTheTrash)  # chore 2 
# chore2.start()

# chore3 = threading.Thread(target=getMail)          # chore 3 
# chore3.start()

# chore1.join()               
# chore2.join()
# chore3.join()

# print("all chores are completed") # it took 4 seconds in total.

#---------------------------------points to remember-----------------------------

# GIL = Global Interpreter Lock. It’s a lock used inside the main Python implementation (CPython). It ensures that only one thread at a time can execute Python bytecode (the actual Python instructions).

# multithreaded is basically a way to run multiple tasks at the same time ie concurrently, using threading module.

# making a thread object and starting it is the wat to run a task at the same time and it will be executed in the background, it will not wait for the task to complete before moving to the next line of code. however it starts all the assigned thread objects at the same time. 

# so the last execution will be the one that took the longest to run, in this case it is the Walk_Dog() function which took 4 seconds to run. so the total time taken to run all the tasks concurrently is 4 seconds.

#----------------------------------------------------------------------------------------------------------------------------

# Day 98 - Multiprocessing in Python - couldnt understand harrys version so bro code way- 

# multiprocessing = the act of running tasks in parallel on different cpu cores, bypasses GIL used for threading -
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)

# ✅ Rule of thumb

# For CPU-bound tasks → use
# cpu_count() = to check the cpu count so that you wont use more than the available cpu cores.
# or 
# cpu_count() - 1 =  you’re basically saying: “Use one less process than the total number of CPU cores.”

#----------Example of multiprocessing in python--------

# from multiprocessing import Process, cpu_count  
# import time


# def counter(num):
#     count = 0
#     while count < num:
#         count += 1


# def main():

#     print("cpu count:", cpu_count())

#     a = Process(target=counter, args=(500,))
#     b = Process(target=counter, args=(500,))

#     a.start()
#     b.start()

#     print("processing...")

#     a.join()
#     b.join()

#     print("Done!")
#     print("finished in:", time.perf_counter(), "seconds")
    
# if __name__ == "__main__":      # means: “Only run this code when the file is executed directly, not when it is imported.”
#     main()

# output - cpu count: 8
# processing...
# Done!
# finished in: 42921.464432793 seconds
#-----------------------------------------points to remember-----------------------------

# CPU core = A CPU core is an individual processing unit within a central processing unit (CPU) that executes instructions and performs calculations. Think of the CPU as the "brain" of your computer, and each core is a smaller, independent "brain" that can handle its own tasks simultaneously. Having multiple cores allows a computer to multitask more effectively, running several applications or processes at once by dividing the workload among the different cores.

# Do not forget to guard your main block of code with if __name__ == "__main__": to avoid recursive spawning of processes. This is a common pitfall when using the multiprocessing module. Especially when you are using multiprocessing in a script that you intend to import and use in another script.

# # ✅ Rule of thumb

# For CPU-bound tasks → use
# cpu_count() = to check the cpu count so that you wont use more than the available cpu cores.
# or 
# cpu_count() - 1 =  you’re basically saying: “Use one less process than the total number of CPU cores.”
#---------------------------------------------------------------------------------------------------------------------------------------------

# # Day 99 - Solution to drink water reminder exercise -------------refer to day 94-------------
#--------------------------------------------------------------------------------------------------------------------------------------------
# Day 100 - 

# Conclusion


# Congratulations on completing the 100 days of Python code challenge! You have likely gained a solid foundation in the language and developed a range of skills, from basic syntax to more advanced concepts such as object-oriented programming. However, this is just the beginning of your journey with Python. There are many more topics to explore, including machine learning, web development, game development, and more.

# Where to go from here:
# To continue your learning journey, consider exploring the following resources:

# Python books: There are many excellent books on Python that can help you deepen your knowledge and skills. Some popular options include "Python Crash Course" by Eric Matthes, "Automate the Boring Stuff with Python" by Al Sweigart, and "Fluent Python" by Luciano Ramalho. I would also like to recommend "Hands on Machine Learning book by Aurélien Géron"

# YouTube Projects: There are many YouTube projects available which can be watched after you have some basic understanding of python

# Python communities: There are many online communities where you can connect with other Python learners and experts, ask questions, and share your knowledge. Some popular options include the Python subreddit, the Python Discord server, and the Python community on Stack Overflow.

# GitHub repositories: GitHub is a great resource for finding Python projects, libraries, and code snippets. Some useful repositories to check out include "awesome-python" (a curated list of Python resources), "scikit-learn" (a machine learning library), and "django" (a web development framework).

# Link to some resources
# Tkinter - You can learn Tkinter which is used to create GUIs from here :
# Machine Learning - I loved this playlist from Google Developers
# Django - For Django, try the tutorial from the official documentation. Trust me its really good
# Overall, the key to mastering Python (or any programming language) is to keep practicing and experimenting. Set yourself challenges, 

# work on personal projects, and stay curious. Good luck!




























#-----------------------------------------------------------------------------------------------------------------------------------------

# Day 




  

































































































































































































































































































































































































































