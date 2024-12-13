import requests
import animals_web_generator
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def load_data():
    """
    asks the user for an animal and gets the data from API
    """
    while True:
        name = input("Enter a name of an animal: ")
        api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}" })
        if response.status_code == requests.codes.ok and response.json() != []:
            return response.json()
        else:
            animals_web_generator.generate_error_message(name)


def get_animal_facts(animal_data):
    """
    extracts information from data and returns them in one html string
    """
    output = ""
    for animal in animal_data:
        output += '<li class="cards__item">'
        try:
            animal_name = animal["name"]
            output += f"<div class='card__title'>{animal_name}</div>"
        except KeyError:
            continue
        output += f"<p class='card__text'>"
        try:
            animal_diet = animal["characteristics"]["diet"]
            output += f"<strong>Diet:</strong> {animal_diet}<br>"
        except KeyError:
            continue
        try:
            animal_location = animal["locations"][0]
            output += f"<strong>Location:</strong> {animal_location}<br>"
        except KeyError:
            continue
        try:
            animal_type = animal["characteristics"]["type"]
            output += f"<strong>Type:</strong> {animal_type}<br>"
        except KeyError:
            continue
        output += "</p></li>"
    return output

