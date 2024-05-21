import requests
import random

def get_random_character():
    url = "https://hp-api.onrender.com/api/characters"
    response = requests.get(url)
    data = response.json()
    random_num = random.randint(0, len(data) - 1)
    return data[random_num]
