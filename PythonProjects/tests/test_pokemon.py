import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9b68e0fbbee5222f2f73e38849b7014a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '256946'
TRAINER_ID = '22233'

def test_status_code_trainers(): 
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_id(): 
    response_get = requests.get(url = f'{URL}/trainers?trainer_id=22233')
    assert response_get.json()["data"][0]["id"] == TRAINER_ID    

