# This is the project file for CFG python course
import random
import requests

players_id = random.randrange(1,151)
computers_id = random.randrange(1,151)
url = "https://pokeapi.co/api/v2/pokemon/"

print("Hello and welcome to this Pokémon game!")
print("Getting you a random pokemon card")
print("------------")
print("------------")

def get_pokemon(id):
    response = requests.get(url + str(id))
    pokemon_data = response.json()

    return {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"]
    }

players_pokemon = get_pokemon(players_id)
computers_pokemon = get_pokemon(computers_id)

print("Your Pokémon is {}".format(players_pokemon["name"]))
print("It's id is {}, it's height is {} and it's weight is {}".format(players_pokemon["id"], players_pokemon["height"], players_pokemon["weight"]))

stat_choice = input("Which stat would you like to use?")

def compare_stats(stat):
    if players_pokemon[stat] > computers_pokemon[stat]:
        return "player"
    elif players_pokemon[stat] < computers_pokemon[stat]:
        return "computer"
    else:
        return "draw"

game_result = compare_stats(stat_choice)

print("You chose {}".format(stat_choice))
print("Your Pokémon's {} is {}".format(stat_choice, str(players_pokemon[stat_choice])))
print("The computer's Pokémon's {} is {}".format(stat_choice, str(computers_pokemon[stat_choice])))

if game_result == "player":
    print("YOU WIN!")
elif game_result == "computer":
    print("The computer wins")
elif game_result == "draw":
    print("It's a draw")
