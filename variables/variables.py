# Variable is a way to store data

# Variable name = variable data
# a = 1 #int
# b = 2 #int
# c = 3.5 #float
# hi = "Hello World!" #string

# print(hi)
# print(a + b)

# type method
# print(type(hi))

# overwriting variables
# x = 5
# y = x
# print("Before reassignment:")
# print("Value of x:" , x)
# print("ID of x:" , id(x))
# print("Value of y:" , y)
# print("ID of y:" , id(y))

# x = 10
# print("After reassignment:")
# print("Value of x:" , x)
# print("ID of x:" , id(x))

# user input
print("Hi please type your name?")
name = input()
print("Hi", name)

print("What is your age?")
age = input()

print("What is you DOB?")
dob = input()

print("What is you address?")
address = input()

print("What are your hobbies?")
hobbies = input()

print("Details:")
print(f"Name:{name} Age:{age} DOB:{dob} Address:{address} Hobbies:{hobbies}")
