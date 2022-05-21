import subprocess
import requests
import json

subprocess.run('clear')

repo = input(f'Name the repository: ').lower() 
new_directory = f'FILENAME/{repo}'

URL = f'https://api.github.com/user/repos'
TOKEN = '' # PERSONAL ACCESS TOKEN
AUTHENTICATION = f"token {TOKEN}"

jsonPayload = {"name": repo}

headers = {"Accept": "application/vnd.github.v3+json",
            "Authorization": AUTHENTICATION      
            }

response = requests.post(URL, headers=headers, data=json.dumps(jsonPayload))
subprocess.run('clear')
commands = [
    ['mkdir',f'{new_directory}'],
    ['touch',f'{new_directory}/{repo}.py'],
    ['python3', '-m', 'venv', f'{new_directory}/venv'],
    ['git', 'init',f'{new_directory}'],
    ['code', f'{new_directory}/'],
    'clear'
    ]

project_creator = [subprocess.run(command) for command in commands]

if response.status_code == 201:
    print(f"'{repo}' was successfully created!!!")
