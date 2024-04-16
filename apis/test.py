import requests
import json
import random

# Send a request to the API to get the list of Pokémon
poke_name_req = requests.get("https://pokeapi.co/api/v2/pokemon")
poke_name_data = poke_name_req.json()

# Extract names of Pokémon from the response
pokemon_names = [pokemon['name'] for pokemon in poke_name_data['results']]

# Select two random names from the list of names
poke_one = random.choice(pokemon_names)
poke_two = random.choice(pokemon_names)

# Function to get height of a Pokémon by its name
def get_pokemon_height(pokemon_name):
    pokemon_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon_data = pokemon_req.json()
    return pokemon_data['height']

# Get the height of the selected Pokémon
height_poke_one = get_pokemon_height(poke_one)
height_poke_two = get_pokemon_height(poke_two)

# Print the randomly selected Pokémon names and their heights
print("Player 1:", poke_one, "Height:", height_poke_one)
print("Player 2:", poke_two, "Height:", height_poke_two)

# Comparing the heights tallest one wins
if height_poke_one > height_poke_two:
    print("Player 1 wins!")
elif height_poke_one == height_poke_two:
    print("It was a draw!")
else:
    print("Player 2 wins!")
