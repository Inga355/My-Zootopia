import json

def load_data(file_path):
    """loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

def get_animal_facts(data):
    """extracts information from data and returns them in one string"""
    output = ""
    for animal in data:
        try:
            animal_name = animal["name"]
            output += f"Name: {animal_name}\n"
        except KeyError:
            continue
        try:
            animal_diet = animal["characteristics"]["diet"]
            output += f"Diet: {animal_diet}\n"
        except KeyError:
            continue
        try:
            animal_location = animal["locations"][0]
            output += f"Location: {animal_location}\n"
        except KeyError:
            continue
        try:
            animal_type = animal["characteristics"]["type"]
            output += f"Type: {animal_type}"
        except KeyError:
            continue
    return output



# Lesen und Speichern des neuen HTML
with open("animals_template.html", "r") as file:
    html_content = file.read()

old_string = "__REPLACE_ANIMALS_INFO__"
new_string = get_animal_facts(animals_data)

updated_html_content = html_content.replace(old_string, new_string)

with open("animals.html", "w", encoding="utf-8") as new_file:
    new_file.write(updated_html_content)
