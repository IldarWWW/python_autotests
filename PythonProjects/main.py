import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9b68e0fbbee5222f2f73e38849b7014a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '256946'
TRAINER_ID = '22233'

body_create_pokemon = {
    "name": "Ван9",
    "photo_id": -1
}

body_change_name =  {
    "pokemon_id": POKEMON_ID,
    "name": "228Ваня",
}

body_pokeball = {
    "pokemon_id": POKEMON_ID
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)

response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

