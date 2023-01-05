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

    headers = {"Accept": "appliechoion/vnd.github.v3+json",
                "Authorization": AUTHENTICATION      
                }

    response = requests.post(URL, headers=headers, data=json.dumps(jsonPayload))

    def project_creator(commands):
        project_creator = [subprocess.run(command) for command in commands]

# Lists of commands that will create the individual project folder with the proper coding language and files needed.
    
    # Python Project Folder
    commands_py = [
        ['mkdir',f'{new_directory}'],
        ['mkdir',f'{new_directory}/tests'],
        ['touch',f'{new_directory}/{repo}.py'],
        ['python3', '-m', 'venv', f'{new_directory}/env'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/'],

        # Test Folder
        ['mkdir',f'{new_directory}/tests'],
        ['touch',f'{new_directory}/tests/__init__.py'],
        ['touch',f'{new_directory}/tests/test_{repo}.py']
        ]

    # ETL Project Folder
    commands_etl = [
        ['mkdir',f'{new_directory}'],

        # Script Folder
        ['mkdir',f'{new_directory}/scripts'],
        ['cp', 'prompts/etl.py', f'{new_directory}/scripts/execute.py'],
        ['touch',f'{new_directory}/scripts/__init__.py'],
        ['touch',f'{new_directory}/scripts/extract.py'],
        ['touch',f'{new_directory}/scripts/transform.py'],
        ['touch',f'{new_directory}/scripts/load.py'],
        
        # Test Folder
        ['mkdir',f'{new_directory}/tests'],
        ['touch',f'{new_directory}/tests/__init__.py'],
        ['touch',f'{new_directory}/tests/test_execute.py'],
        ['touch',f'{new_directory}/tests/test_extract.py'],
        ['touch',f'{new_directory}/tests/test_transform.py'],
        ['touch',f'{new_directory}/tests/test_load.py'],
        
        # Data Folder
        ['mkdir',f'{new_directory}/data'],
        ['python3', '-m', 'venv', f'{new_directory}/env'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/']
        ]

    # Airflow Project Folder
    commands_af = [
        ['mkdir',f'{new_directory}'],

        # Script Folder
        ['mkdir',f'{new_directory}/scripts'],
        ['cp', 'prompts/etl.py', f'{new_directory}/scripts/execute.py'],
        ['touch',f'{new_directory}/scripts/extract.py'],
        ['touch',f'{new_directory}/scripts/transform.py'],
        ['touch',f'{new_directory}/scripts/load.py'],
        
        # Test Folder
        ['mkdir',f'{new_directory}/tests'],
        ['touch',f'{new_directory}/tests/__init__.py'],
        ['touch',f'{new_directory}/tests/test_execute.py'],
        ['touch',f'{new_directory}/tests/test_extract.py'],
        ['touch',f'{new_directory}/tests/test_transform.py'],
        ['touch',f'{new_directory}/tests/test_load.py'],

        # Airflow folder
        ['mkdir',f'{new_directory}/dags'],
        ['cp', 'prompts/dag.py', f'{new_directory}/dags/dag.py'],
        
        ['mkdir',f'{new_directory}/data'],
        
        ['python3', '-m', 'venv', f'{new_directory}/env'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/']
        ]

    # Web Development Project Folder
    commands_web_dev = [
        ['mkdir',f'{new_directory}'],
        ['mkdir',f'{new_directory}/tests'],
        ['touch',f'{new_directory}/{repo}.html'],
        ['touch',f'{new_directory}/index.js'],
        ['touch',f'{new_directory}/style.css'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/']
        ]

    if project_type == 'py': 
        project_creator(commands_py)
    elif project_type == 'etl': 
        project_creator(commands_etl)
    elif project_type == 'af': 
        project_creator(commands_af)
    elif project_type == 'wd': 
        project_creator(commands_web_dev)

# Confirms that the project template was created successfully.
    if response.status_code == 201:
        print(f"\n'{repo}' was successfully created!!!\n")
    else:
        print(f'\n{response.status_code}')
        print(f'{response.content}\n')

@app.command()
def py(name: str):
    create(repo(name), project('py'))

@app.command()
def etl(name: str):
    create(repo(name), project('etl'))

@app.command()
def wd(name: str):
    create(repo(name), project('wd'))

@app.command()
def af(name: str):
    create(repo(name), project('af'))

if __name__ == "__main__":
    app()