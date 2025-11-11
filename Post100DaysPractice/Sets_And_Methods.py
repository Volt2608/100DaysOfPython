
# Sets & Set Methods
#
# A set in Python is an unordered, mutable, and unique collection of elements.
# It does not allow duplicate values.
#----------------------------------------------------------------------------------------------------------

# Creating a Set:

# empty_set = set()   # Empty set (must use set(), not {})
#
# numbers = {1, 2, 3, 4, 5}  # Set with elements
#
# mixed_set = {1, "Hello", 3.14, True}  # Mixed data types
#
# unique_numbers = set([1, 2, 2, 3, 4, 4, 5])  # Creating a set from a list
#
# print(unique_numbers)  # {1, 2, 3, 4, 5}

#----------------------------------------------------------------------------------------------------------
# Common Set Methods

# Method          	        Description	                                       Example

# add(x)	               Adds an element x to the set.	                    my_set.add(10)
# update(iterable)   Adds multiple elements from an iterable.	                my_set.update([6, 7, 8])
# remove(x)	     Removes x from the set (raises an error if not found).	    my_set.remove(3)
# discard(x)	    Removes x from the set (does not raise an error if not found). my_set.discard(3)
# pop()	            Removes and returns a random element.	                my_set.pop()
# clear()             	Removes all elements from the set.	                my_set.clear()
# copy()	              Returns a shallow copy of the set.	                new_set = my_set.copy()

#----------------------------------------------------------------------------------------------------------
# Set Operations

# Operation	                         Description	                              Example
#
# union(set2)	Returns a new set with all unique elements from both sets.	       set1.union(set2)
# intersection(set2)	Returns a set with elements common to both sets.	       set1.intersection(set2)
# difference(set2)	 Returns a set with elements in set1 but not in set2.	   set1.difference(set2)
#
# symmetric_difference(set2)	Returns a set with elements
# in either set1 or set2, but not both.	                                       set1.symmetric_difference(set2)
#
# issubset(set2)	Returns True if set1 is a subset of set2.                      set1.issubset(set2)
# issuperset(set2)	Returns True if set1 is a superset of set2.	                  set1.issuperset(set2)
#----------------------------------------------------------------------------------------------------------
#
# Example Usage:
#
# In Python, sets support intuitive operators for common operations like union (|), intersection (&), difference (-),
# and symmetric difference (^). These have equivalent method forms too, like .union(), .intersection(), etc.
# Here's a quick example:

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# # Union – combines all unique elements
# print(set1 | set2)            # {1, 2, 3, 4, 5, 6}
# print(set1.union(set2))       # same result
#
# # Intersection – common elements
# print(set1 & set2)            # {3, 4}
# print(set1.intersection(set2))# same result
#
# # Difference – in set1 but not in set2
# print(set1 - set2)            # {1, 2}
# print(set1.difference(set2))  # same result
#
# # Symmetric Difference – in either set, but not both
# print(set1 ^ set2)                     # {1, 2, 5, 6}
# print(set1.symmetric_difference(set2))# same result
#----------------------------------------------------------------------------------------------------------
# Key Properties of Sets:
#
# Unordered: No indexing or slicing.
# Unique Elements: Duplicates are automatically removed.
# Mutable: You can add or remove elements.

