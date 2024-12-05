import json
from math import trunc


def load_data(file_path):
    """loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

def get_animal_facts(data):
    for animal in data:
        print("")
        try:
            animal_name = animal["name"]
            print(f"Name: {animal_name}")
        except KeyError:
            continue
        try:
            animal_diet = animal["characteristics"]["diet"]
            print(f"Diet: {animal_diet}")
        except KeyError:
            continue
        try:
            animal_location = animal["locations"][0]
            print(f"Location: {animal_location}")
        except KeyError:
            continue
        try:
            animal_type = animal["characteristics"]["type"]
            print(f"Type: {animal_type}")
        except KeyError:
            continue



get_animal_facts(animals_data)