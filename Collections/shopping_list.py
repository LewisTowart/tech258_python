# Collections are a way to store multiple pieces of data in one reference
# List are the most common/simplest collections
# Lists are often known as arrays in other languages

# Create the shopping list
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Print the shopping list and it's data type
print(shopping_list)
print(type(shopping_list))

# Print certain items in the list
print(shopping_list[0])
print(shopping_list[-1])

# Change Bread to rice then print
shopping_list[1] = "rice"
print(shopping_list[1])

# Add the item carrots then show it has gone from 5 to 6 items
shopping_list.append("carrots")
print(len(shopping_list))

# Add two items at one time
new_items = ["toffee", "coffee"]
shopping_list.extend(new_items)
print(shopping_list)

# Remove bananas
shopping_list.remove("bananas")
print(shopping_list)

# Remove an item using pop
shopping_list.pop(-1)
print(shopping_list)
