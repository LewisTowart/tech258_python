list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# This loop will double each number assigning the new value until the i counter is bigger than the amount of "items
# in the list

i = 0
while i < len(list_data):
    list_data[i] *= 2
    i += 1

print(list_data)

# Each list in embedded_lists is a sublist this loop prints each on until all have been printed
for sublist in embedded_lists:
    print(sublist)

# This loop prints each sublist then individually prints each item (value within that sublist)
for sublist in embedded_lists:
    print(sublist)
    for item in sublist:
        print(item)

# This loop is simply printing all the keys available in dict_data
for key in dict_data:
    print(key)

for values in dict_data.values():  # Starts a loop that goes over the values in the dictionary associated with the key
    for value in values.values():  # This loop catches the value associated to those values and prints it
        print(value)

# This loop looks through each of the values labelled money and prints them until there is none left
for item in dict_data.values():
    print(item["money"])
