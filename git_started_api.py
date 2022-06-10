import subprocess
import requests
import json

subprocess.run('clear')

repo = input(f'Name the repository: ').lower() 
project_type = input(f'What kind of project are you creating? ').lower()
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

commands_py = [
    ['mkdir',f'{new_directory}'],
    ['touch',f'{new_directory}/{repo}.py'],
    ['python3', '-m', 'venv', f'{new_directory}/venv'],
    ['git', 'init',f'{new_directory}'],
    ['code', f'{new_directory}/'],
    'clear'
    ]

commands_web_dev = [
    ['mkdir',f'{new_directory}'],
    ['touch',f'{new_directory}/index.html'],
    ['touch',f'{new_directory}/index.js'],
    ['touch',f'{new_directory}/style.css'],
    ['git', 'init',f'{new_directory}'],
    ['code', f'{new_directory}/'],
    'clear'
    ]

if project_type == 'py': 
    project_creator = [subprocess.run(command) for command in commands_py]
elif project_type == 'wd': 
    project_creator = [subprocess.run(command) for command in commands_web_dev]


if response.status_code == 201:
    print(f"'{repo}' was successfully created!!!")
