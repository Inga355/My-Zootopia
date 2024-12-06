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



# Lesen und Speichern des neuen HTML
with open("animals_template.html", "r") as file:
    html_content = file.read()

old_string = "__REPLACE_ANIMALS_INFO__"
new_string = get_animal_facts(animals_data)

updated_html_content = html_content.replace(old_string, new_string)

with open("animals.html", "w", encoding="utf-8") as new_file:
    new_file.write(updated_html_content)
