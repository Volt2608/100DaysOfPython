
# Lambda functions
# A lambda function in Python is an anonymous, single-expression function defined using the lambda keyword.
# It is commonly used for short, throwaway functions where a full function definition is unnecessary.
#---------------------------------------------------------------------------------------------------------------------
#
# 1.Syntax of Lambda Functions :
#     ------>                  lambda arguments: expression                   <-------

# lambda → Keyword to define a lambda function
# arguments → Input parameters (comma-separated)
# expression → The operation performed (must be a single expression, not multiple statements)
#
# Example: Simple Lambda Function :
#
# square = lambda x: x ** 2
# print(square(5))  # Output: 25
#---------------------------------------------------------------------------------------------------------------------

# 2. Using Lambda Functions with map(), filter(), and reduce()

# 2.1 Using map() with Lambda :
# Applies a function to each element of an iterable.
#
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # Output: [1, 4, 9, 16]
#---------------------------------------------

# 2.2 Using filter() with Lambda :
# Filters elements based on a condition.
#
# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Output: [2, 4, 6]
#---------------------------------------------

# 2.3 Using reduce() with Lambda :
# Reduces an iterable to a single value (requires functools.reduce).
#
# from functools import reduce
#
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 24
#---------------------------------------------------------------------------------------------------------------------

# 3. Lambda with Multiple Arguments
# Example: Adding Two Numbers
#
# add = lambda x, y: x + y
# print(add(3, 7))  # Output: 10
#---------------------------------------------

# Example: Finding the Maximum o> y else y
# print(maximum(10, 5))  # Output: 10f Two Numbers -
# maximum = lambda x, y: x if x
#---------------------------------------------------------------------------------------------------------------------

# 4. Lambda in Sorting Functions -
# Sorting a List of Tuples -
#
# students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]
# students.sort(key=lambda student: student[1])  # Sort by score
# print(students)  # Output: [('Bob', 78), ('Alice', 85), ('Charlie', 92)]
#---------------------------------------------------------------------------------------------------------------------

# 5. When to Use Lambda Functions?

# Use Lambda Functions When:
#
# The function is short and simple.
# Used temporarily inside another function (e.g., map, filter).
# Avoiding defining a full function with def.
#
#---------------------------------------------
# Avoid Lambda Functions When:
#
# The function is complex (use def for readability).
# Multiple operations/statements are needed.
#---------------------------------------------------------------------------------------------------------------------
# 6.

# Feature                                          	Example
#
# Basic Lambda Function	                            lambda x: x**2
# With map()	                                        map(lambda x: x**2, numbers)
# With filter()	                                    filter(lambda x: x % 2 == 0, numbers)
# With reduce()	                                    reduce(lambda x, y: x * y, numbers)
# Multiple Arguments	                                lambda x, y: x + y
# Sorting with Lambda	                                sort(key=lambda x: x[1])
























