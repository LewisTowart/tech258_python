# Bools and None

# Booleans can be: True or False

# a = True
# b = False

# print(a == b) # False
# print(a != b) # True
#
# print(a >= b) # True
# print(a <= b) # False
#
# # False is ALWAYS 0

# Booleans methods

# hi = "Hello World"

# # we can use these to make decisions based on conditions
# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.isupper()) # False
# print(hi.endswith("d")) # True
# print(hi.startswith("H")) # True

# print(bool("a")) # True if not empty
# print(bool("")) # False if empty

# 0 Always false any other number is true even if it's negative
# print(bool(0)) # False
# print(bool(40)) # True
# print(bool(-40)) # True

# The value of None

# None is an object, it is essentially a placeholder

# None when converted to bool is False
# print(bool(None))
#
# # None != False
#
# x = None
#
# print(x == False) # False
# print(x == None) # True
#
# print(type(x))

# None is best to use over an empty string etc. it is less likely to cause problems
# , takes less memory and gives clarity to others

