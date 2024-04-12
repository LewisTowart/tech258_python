# Sets and frozensets

# create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# sets are UNORDERED AND UNINDEXED

# add an element
fruits.add("orange")
print(fruits)

# remove element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
# There can  be no duplicated in a set
fruits.add("banana")
print(fruits)

# convert list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a | set_b)
# Difference
print(set_a - set_b)

# Frozen set is an immutable set

frozen_set = frozenset(["hello", "world"])
print(frozen_set)


# frozen_set.add("!")
# print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)
