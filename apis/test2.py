import requests
import random

# Function to get Pokémon data from the API
def get_pokemon_data(pokemon_name):
    pokemon_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon_data = pokemon_req.json()
    return pokemon_data

# Function to select a random Pokémon
def get_random_pokemon():
    poke_name_req = requests.get("https://pokeapi.co/api/v2/pokemon")
    poke_name_data = poke_name_req.json()
    pokemon_names = [pokemon['name'] for pokemon in poke_name_data['results']]
    random_pokemon_name = random.choice(pokemon_names)
    return random_pokemon_name

# Function to play a round of the game
def play_round(player1_pokemon, player2_pokemon, attribute):
    player1_data = get_pokemon_data(player1_pokemon)
    player2_data = get_pokemon_data(player2_pokemon)

    player1_value = player1_data[attribute]
    player2_value = player2_data[attribute]

    print(f"{player1_pokemon} ({player1_value}) vs {player2_pokemon} ({player2_value})")

    if player1_value > player2_value:
        return 1
    elif player2_value > player1_value:
        return 2
    else:
        return 0

# Main game loop
def main():
    player1_pokemon = get_random_pokemon()
    player2_pokemon = get_random_pokemon()

    print("Player 1's Pokémon:", player1_pokemon)
    print("Player 2's Pokémon:", player2_pokemon)

    attributes = ['height', 'weight', 'base_experience']
    player1_score = 0
    player2_score = 0

    for attribute in attributes:
        input("Press Enter to compare " + attribute + "...")
        winner = play_round(player1_pokemon, player2_pokemon, attribute)
        if winner == 1:
            player1_score += 1
            print("Player 1 wins the round!")
        elif winner == 2:
            player2_score += 1
            print("Player 2 wins the round!")
        else:
            print("It's a tie!")

    print("Final Scores:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    main()