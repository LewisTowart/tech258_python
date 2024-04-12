# A list can be made up of different data types

print("What is your name?")
name = input()
print("Hi", name)

print("What is your age?")
age = input()
age = int(age)

print("What is you DOB?")
dob = input()

# print("What is you address?")
# address = input()

# print("What are your hobbies?")
# hobbies = input()

# print("Details:")
# print(f"Name:{name} Age:{age} DOB:{dob} Address:{address} Hobbies:{hobbies}")

# Printing variables in the list string and int
user_list = [name, age, dob]
print(user_list)
print(type(age))

# Get the user height and print it + the type
height = input("What is your height in cm?\n")
height = float(height)
user_list.append(height)
print(type(height))
print(user_list[-1])