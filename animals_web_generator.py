import data_fetcher


def main():
    """
    main function
    """ 
    animal_data = data_fetcher.load_data()
    animal_facts = data_fetcher.get_animal_facts(animal_data)
    generate_html(animal_facts) 


def generate_html(animal_facts):
    """
    generates new html file with animal facts extracted from json file
    """
    with open("animals_template.html", "r") as file:
        html_content = file.read()
        old_string = "__REPLACE_ANIMALS_INFO__"
        new_string = animal_facts
        updated_html_content = html_content.replace(old_string, new_string)
        with open("animals.html", "w", encoding="utf-8") as new_file:
            new_file.write(updated_html_content)


def generate_error_message(animal_name):
    """
    generates new html file with error message
    """
    with open("animals_template.html", "r") as file:
        html_content = file.read()
        old_string = "__REPLACE_ANIMALS_INFO__"
        new_string = f"<h2>The animal <span style='color: red;'>{animal_name}</span> doesn't exist.</h2>"
        updated_html_content = html_content.replace(old_string, new_string)
        with open("animals.html", "w", encoding="utf-8") as new_file:
            new_file.write(updated_html_content)


if __name__ == "__main__":
    main()
