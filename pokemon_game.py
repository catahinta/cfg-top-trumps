import random
import requests
import time

print("Hello and welcome to this Pokémon game!\n")

def get_random_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/"
    random_num = random.randrange(1,151)
    response = requests.get(url + str(random_num))
    pokemon_data = response.json()

    return {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
        "speed": pokemon_data["stats"][-1]["base_stat"],
        "attack": pokemon_data["stats"][1]["base_stat"],
        "hp": pokemon_data["stats"][0]["base_stat"]
    }

def compare_stats(stat, players_pokemon, computers_pokemon):
    if players_pokemon[stat] > computers_pokemon[stat]:
        return ["YOU WIN!", 0]
    elif players_pokemon[stat] < computers_pokemon[stat]:
        return  ["You lose :(", 1]
    else:
        return ["It's a draw", 2]

def print_stats(pokemon):
    for stat in pokemon:
        print("Its {} is {}".format(stat, pokemon[stat]))


# def display_results(result):
#     if result == "player":
#         return "YOU WIN!"
#     elif result == "computer":
#         return "The computer wins"
#     elif result == "draw":
#         return "It's a draw"

def run():
    print("Getting you a random pokemon card")
    print("------------")
    print("------------")
    time.sleep(1)

    players_pokemon = get_random_pokemon()
    computers_pokemon = get_random_pokemon()

    print("Your Pokémon is {}\n".format(players_pokemon["name"]))
    # print("It's id is {}, it's height is {}, it's weight is {}, it's attack is {} and it's speed is {}\n".format(players_pokemon["id"], players_pokemon["height"], players_pokemon["weight"], players_pokemon["attack"],players_pokemon["speed"]))
    print_stats(players_pokemon)
    time.sleep(1)

    stat_choice = stat_choice = input("Which stat would you like to use?\n")
    while stat_choice not in ["id", "height", "weight", "speed", "attack", "hp"]:
        stat_choice = input("Which stat would you like to use?\n")

    game_result = compare_stats(stat_choice, players_pokemon, computers_pokemon)

    print("You chose {}".format(stat_choice))
    print("------------")
    time.sleep(0.5)
    print("Your Pokémon's {} is {}".format(stat_choice, str(players_pokemon[stat_choice])))
    print("------------")
    time.sleep(1)
    print("Your opponent's Pokémon is {}".format(computers_pokemon["name"]))
    print("Your opponent's Pokémon's {} is {}".format(stat_choice, str(computers_pokemon[stat_choice])))
    print("------------")
    time.sleep(1)

    print(game_result[0])
    return game_result[1]

games_won = 0
games_lost = 0
result = run()
if result == 0:
    games_won += 1
elif result == 1:
    games_lost += 1

print("So far you won {} games and lost {} games".format(games_won, games_lost))
play_again = input("Do you want to play again? y/n\n")
while play_again == "y":
    result = run()
    if result == 0:
        games_won += 1
    elif result == 1:
        games_lost += 1
    print("So far you won {} games and lost {} games".format(games_won, games_lost))
    play_again = input("Do you want to play again? y/n\n")

print("Goodbye!")
