prices = {
    "starters": {
    "calamari": 4,
    "snails": 3,
    "halloumi": 2,
    },
    "mains": {
    "steak": 6,
    "burger": 5,
    "curry": 5,
    },
    "desserts": {
    "cake": 3,
    "pie": 3,
    "jelly": 2
    }
}

starters = ["calamari", "snails", "halloumi"]
print(f"Hi, here is a list of starters\n{starters}\nPlease choose a starter")
starter_choice = input()

mains = ["steak", "burger", "curry"]
print(f"Here is a list of mains\n{mains}\nPlease choose a main")
mains_choice = input()

desserts = ["cake", "pie", "jelly"]
print(f"Here is a list of desserts\n{desserts}\nPlease choose a dessert")
dessert_choice = input()

customer_order_list = [starter_choice, mains_choice, dessert_choice]

print(f"You have chosen...\n Starter:{starter_choice}\n Main:{mains_choice}\n Dessert:{dessert_choice}")
