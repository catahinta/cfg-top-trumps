# This is the project file for CFG python course
import random
import requests

players_id = random.randrange(1,151)
computers_id = random.randrange(1,151)
url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(id):
    response = requests.get(url + str(id))
    pokemon_data = response.json()

    return {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"]
    }

print(get_pokemon(players_id))
