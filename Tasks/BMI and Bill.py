# Get the user's height and weight
#
# print("What is your height in Metres?")
# height = float(input())
#
# print("What is your weight in Kilograms?")
# weight = float(input())
#
# # Calculate their BMI from the height and weight given
#
# m_squared = height * height
# bmi = weight / m_squared
# # Apparently BMI values are given to one decimal place
# bmi_rounded = round(bmi, 1)
#
# # Print the BMI as a message to the user
#
# print("Your BMI is", bmi_rounded)

# Let's help with generating a bill with tips added and allow the user to split among a number of people

#Get the bill from the user

print("How much was your bill?")
bill = float(input())

# Calculate the tip (assume a percentage of 10-15%)

print("What percent tip of 10 to 15% do you want to add?")
percent = float(input())
tip = bill * (percent / 100)
tip = round(tip, 2)
print("Your 10% tip will be", tip)

# Calculate bill with the tip added

bill_total = bill + tip
print("Your total bill is", bill_total)

# Ask how many people they want to split with

print("How many people would you like to split the bill with?")
split = int(input())

# Calculate the bill divided by the split amount

split_amount = bill_total / split

# Print the split bill per person, being rounded to 2 decimal places - you will have to research how to display to 2 decimal places

split_amount = round(split_amount, 2)
print("Total paid by each person is", split_amount)
