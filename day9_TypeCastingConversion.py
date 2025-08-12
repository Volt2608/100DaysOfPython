# day 9
# Typecasting in python Explicit (done by developer as per requirement) and Implicit (According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

#Explicit Type Conversion (Type Casting):
#This requires the programmer or developer to manually convert the data type using built-in functions.
# Implicit Type Conversion: python automatically converts one data type to another. This process doesn't need any user intervention.

# These functions include int(), float(), str(), list(), tuple(), set(), dict(), bool(), etc.
# Explicit conversion can lead to data loss if a larger data type is converted to a smaller one (e.g., converting a float to an integer truncates the decimal part).
string = "50"
number = 6.5
typecast_String_To_Int = int(string) #it is basically converting string to integer.
sum = number + typecast_String_To_Int #sum is now an integer.
print("The Sum of both the numbers is: ", sum) #successfully typecasted string to integer.
#---------------------
a="2"
b="3"
print(int(a)*int(b)) #typecasting string to integer.