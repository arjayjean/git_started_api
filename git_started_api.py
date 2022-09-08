import subprocess
import requests
import json
import typer

subprocess.run('clear')

app = typer.Typer()

def repo(name):
    return name
def project(type_of):
    return type_of

def create(repo, project_type):
    new_directory = f'FILENAME/{repo}'

    URL = f'https://api.github.com/user/repos'
    TOKEN = '' # PERSONAL ACCESS TOKEN
    AUTHENTICATION = f"token {TOKEN}"

    jsonPayload = {"name": repo}

    headers = {"Accept": "application/vnd.github.v3+json",
                "Authorization": AUTHENTICATION      
                }

    response = requests.post(URL, headers=headers, data=json.dumps(jsonPayload))

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

    commands_go = [
        ['mkdir',f'{new_directory}'],
        ['touch',f'{new_directory}/{repo}.go'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/'],
        'clear'
        ]

    if project_type == 'py': 
        project_creator = [subprocess.run(command) for command in commands_py]
    elif project_type == 'wd': 
        project_creator = [subprocess.run(command) for command in commands_web_dev]
    elif project_type == 'go': 
        project_creator = [subprocess.run(command) for command in commands_go]
    subprocess.run('clear')


    if response.status_code == 201:
        print(f"'{repo}' was successfully created!!!")
    else:
        print(f'\n{response.status_code}')
        print(response.content)

@app.command()
def py(name: str):
    create(repo(name), project('py'))

@app.command()
def wd(name: str):
    create(repo(name), project('wd'))

@app.command()
def go(name: str):
    create(repo(name), project('go'))

if __name__ == "__main__":
    app()