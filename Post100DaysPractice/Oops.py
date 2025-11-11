
# Object Oriented Programming :
#
# Object-Oriented Programming (OOP) is a programming paradigm that organizes code
# into objects that contain both data (attributes) and behavior (methods).
#----------------------------------------------------------------------------------------------------------------

# Key Concepts of OOP
#
# Concept                             	  Description
#
# Class	                              A blueprint for creating objects.
# Object	                              An instance of a class with specific data and behavior.
# Attributes	                          Variables that store data for an object.
# Methods	                              Functions inside a class that define object behavior.
# Encapsulation	                      Restricting direct access to an object's data.
# Inheritance	                          Creating a new class from an existing class.
# Polymorphism	                      Using the same method name for different classes.
#----------------------------------------------------------------------------------------------------------------

# 1. Defining a Class and Creating an Object
# Creating a Class :

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute
#
#     def display_info(self):  # Method
#         return f"{self.brand} {self.model}"
#
# # Creating an Object (Instance)
# car1 = Car("Toyota", "Camry")
# print(car1.display_info())  # Output: Toyota Camry
#----------------------------------------------------------------------------------------------------------------

# 2. Encapsulation (Data Hiding) :
# Encapsulation prevents direct modification of attributes and allows controlled access
# using getter and setter methods.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private Attribute
#
#     def get_balance(self):  # Getter
#         return self.__balance
#
#     def deposit(self, amount):  # Setter
#         if amount > 0:
#             self.__balance += amount
#
# # Using Encapsulation
# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())  # Output: 1500
#----------------------------------------------------------------------------------------------------------------

# 🔹 Why use encapsulation?
# It protects data by restricting direct modification.
#----------------------------------------------------------------------------------------------------------------

# 3. Inheritance (Reusing Code)
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

# Example -
# class Animal:
#     def speak(self):
#         return "Animal makes a sound"
#
# class Dog(Animal):  # Inheriting from Animal
#     def speak(self):
#         return "Bark"
#
# dog = Dog()
# print(dog.speak())  # Output: Bark
#----------------------------------------------------------------------------------------------------------------

# 🔹 Why use inheritance?
# It promotes code reusability and maintains cleaner code structure.
#----------------------------------------------------------------------------------------------------------------

# 4. Multiple Inheritance
# A class can inherit from multiple parent classes.

# class A:
#     def method_a(self):
#         return "Method A"
#
# class B:
#     def method_b(self):
#         return "Method B"
#
# class C(A, B):  # Multiple Inheritance
#     pass
#
# obj = C()
# print(obj.method_a())  # Output: Method A
# print(obj.method_b())  # Output: Method B
#----------------------------------------------------------------------------------------------------------------

# 🔹 Why use multiple inheritance?
# It allows a class to inherit features from multiple parent classes.
#----------------------------------------------------------------------------------------------------------------

# 5. Polymorphism (Same Method, Different Behavior)
# Polymorphism allows different classes to use the same method name.

# Example -
# class Bird:
#     def fly(self):
#         return "Birds can fly"
#
# class Penguin(Bird):
#     def fly(self):
#         return "Penguins cannot fly"
#
# bird = Bird()
# penguin = Penguin()
#
# print(bird.fly())      # Output: Birds can fly
# print(penguin.fly())   # Output: Penguins cannot fly
#----------------------------------------------------------------------------------------------------------------

# 🔹 Why use polymorphism?
# It provides flexibility by allowing different classes to define the same method differently.
#----------------------------------------------------------------------------------------------------------------

# 6. Abstraction (Hiding Implementation Details) :
#
# Abstraction is used to define a method without implementing it in the base class.
# It is achieved using abstract base classes (ABC module).

# Example -
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass  # No implementation
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side  # Implemented in child class
#
# square = Square(4)
# print(square.area())  # Output: 16
#----------------------------------------------------------------------------------------------------------------

# 🔹 Why use abstraction?
# It enforces consistent implementation across child classes.
#----------------------------------------------------------------------------------------------------------------

# 7. Magic Methods (Dunder Methods)
# Magic methods allow objects to behave like built-in types.
# Example: __str__() and __len__()

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#
#     def __str__(self):  # String representation
#         return f"Book: {self.title}"
#
#     def __len__(self):  # Define behavior for len()
#         return self.pages
#
# book = Book("Python Basics", 300)
# print(str(book))  # Output: Book: Python Basics
# print(len(book))  # Output: 300
#----------------------------------------------------------------------------------------------------------------

# 8.      Class  vs.Static Methods :
#
# Method Type	                           Description	                      Uses self?	    Uses cls?
# Instance Method	                  Works with instance attributes	          ✅	          ❌
# Class Method                      Works with class attributes	                  ❌	          ✅
# Static Method	                  Does not use class or instance variables        ❌	          ❌

# Example -
# class Example:
#     class_var = "I am a class variable"
#
#     def instance_method(self):
#         return "Instance Method"
#
#     @classmethod
#     def class_method(cls):
#         return cls.class_var
#
#     @staticmethod
#     def static_method():
#         return "Static Method"
#
# obj = Example()
# print(obj.instance_method())  # Output: Instance Method
# print(Example.class_method()) # Output: I am a class variable
# print(Example.static_method()) # Output: Static Method
#----------------------------------------------------------------------------------------------------------------

# Summary of OOP Concepts :
#
#
#  Concept	                  Description	                                  Example
#  Class	                   A blueprint for creating objects	                 class Car:
#  Object	                   An instance of a class	                         car1 = Car()
#  Encapsulation	           Restrict direct access to data	                 self.__balance
#  Inheritance	           A class inherits from another class	             class Dog(Animal)
#  Polymorphism	           Using the same method in different ways	         def fly(self)
#  Abstraction	               Hiding implementation details	                 @abstractmethod
#  Magic Methods	           Special methods like __str__()	                 def __len__(self)
#  Class Methods	           Works with class variables	                     @classmethod
#  Static Methods	           Independent of class and instance	              staticmethod

# -------------------------------------------------------------------------------------------------------------
# class student:
#     def __init__(self, name, rollNum, marks):
#         self.name = name
#         self.rollNum = rollNum
#         self.marks = marks
#
# class lowMarksException(Exception):
#     pass
#
# try :
#     marks = int(input("Enter marks: "))
#     if marks < 35:
#         raise lowMarksException
# except lowMarksException:
#     print("failed")
# else :
#      print("passed")
#
# student_obj = student("Rohit", 35, 65)

#--------------------------------------------------











