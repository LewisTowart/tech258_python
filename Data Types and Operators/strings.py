# Strings

# single_quotes = 'Look! single quotes'
# double_quotes = "Look! double quotes"
#
# print(single_quotes)
# print(double_quotes)

# Generally prefer double quotes because ' can be used for other things

# bad_string = 'It's not right''
# good_string = "It's not right"

# If you really have to use single quotes
# escape_example = 'I said \'Wow!\''
# print(escape_example)

# String slicing

# Hw = "Hello World!"
#
# print(len(Hw))
# print(Hw[0])
# print(Hw[11])
# print(Hw[-2])
# print(Hw[:3])

# String Methods

# white_space = "lot's of white space at the end                "
# print(len(white_space))
# print(len(white_space.strip()))
#
# example_string = "Here's some text with lot's of text"
# # Count a substring within a string
# print(example_string.count("text"))
# Shows how many times text appears in the string can be done with letters as well like a

# Make string lowercase
# print(example_string.lower())

# # Make Upper case
# print(example_string.upper())

# Replacing text
# print(example_string.replace(" with", ","))

# Concatanation and Casting

# a = "here "
# b = "more "
# c = "much more"
#
# # print(a + b + c)
#
# # Crossing data types
# x = 2
# y = 5.4
# z = " there's now a number 25.4 unless we put a space in"
# w = "30"
#
# print(str(x) + " " + str(y) + z)
# print(x + y + int(w))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

# name = "Snoopy"
# years = 52
#
# print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")
#
# # using f-strings to format number
#
# pi = 3.14159265359
#
# print(f"{pi:.3f}")
# print(f"{pi:.5f}")
#
# score = 16
# max_score = 26
#
# print(f"You scored {score/max_score}")
# print(f"You scored {score/max_score:%}")
# print(f"You scored {score/max_score:.0%}")




