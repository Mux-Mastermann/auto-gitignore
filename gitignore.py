"""
Using the https://www.gitignore.io/ API to get templates for a gitignore file
"""
import logging

import requests
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s — %(levelname)s — Line:%(lineno)d — %(message)s")


def main():
    """
    Using the https://www.gitignore.io/ API to get templates for a gitignore file
    """
    # request to get all possible templates
    r = requests.get("https://www.gitignore.io/api/list?format=lines")
    templates = [line for line in r.text.splitlines()]
    logging.debug(templates)

    # setting the input completer to the list of templates from the API
    input_completer = WordCompleter(templates)
    # prompting the user for template input and setting them as parameter for next API call
    parameter = prompt("Enter all templates with a space in between: ",
                       completer=input_completer, complete_while_typing=True).split()
    logging.info(parameter)
    # Test if all parameters are in the templates list (taking care of invalid input here)
    for param in parameter:
        if param not in templates:
            print(f"Invalid Input: {param} not a valid template")
            quit()

    # actual request with parameters
    r = requests.get(f"https://www.gitignore.io/api/{','.join(parameter)}")
    logging.debug(f"Request: {r.request.path_url}")
    logging.info(r.status_code)

    # write returned text into .gitignore file in the dir from which script was run
    with open(".gitignore", "w") as f:
        f.write(r.text)

    # Success
    print("Successfully created your gitignore file")
