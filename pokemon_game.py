# This is the project file for CFG python course
import random
import requests
import time

url = "https://pokeapi.co/api/v2/pokemon/"

def get_random_pokemon():
    random_num = random.randrange(1,151)
    response = requests.get(url + str(random_num))
    pokemon_data = response.json()

    return {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"]
    }

def compare_stats(stat, players_pokemon, computers_pokemon):
    if players_pokemon[stat] > computers_pokemon[stat]:
        return "YOU WIN!"
    elif players_pokemon[stat] < computers_pokemon[stat]:
        return "The computer wins"
    else:
        return "It's a draw"

# def display_results(result):
#     if result == "player":
#         return "YOU WIN!"
#     elif result == "computer":
#         return "The computer wins"
#     elif result == "draw":
#         return "It's a draw"

def run():
    print("Hello and welcome to this Pokémon game!\n")
    print("Getting you a random pokemon card")
    print("------------")
    print("------------")
    time.sleep(1)

    players_pokemon = get_random_pokemon()
    computers_pokemon = get_random_pokemon()

    print("Your Pokémon is {}\n".format(players_pokemon["name"]))
    print("It's id is {}, it's height is {} and it's weight is {}\n".format(players_pokemon["id"], players_pokemon["height"], players_pokemon["weight"]))
    time.sleep(1)

    stat_choice = input("Which stat would you like to use?\n")

    game_result = compare_stats(stat_choice, players_pokemon, computers_pokemon)

    print("You chose {}".format(stat_choice))
    print("------------")
    time.sleep(0.5)
    print("Your Pokémon's {} is {}".format(stat_choice, str(players_pokemon[stat_choice])))
    print("------------")
    time.sleep(1)
    print("The computer's Pokémon is {}".format(computers_pokemon["name"]))
    print("The computer's Pokémon's {} is {}".format(stat_choice, str(computers_pokemon[stat_choice])))
    print("------------")
    time.sleep(1)

    print(game_result)

run()
