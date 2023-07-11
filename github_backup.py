import requests 
import os
import subprocess

env_file = os.getenv('GITHUB_ENV')


GITHUB_USERNAME = os.environ['GITHUB_USERNAME']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
BACKUP_DIRECTORY = './backup'



if not os.path.exists(BACKUP_DIRECTORY):
    os.makedirs(BACKUP_DIRECTORY)



def backup_repository(repo):
    repo_name = repo['name']
    repo_url = repo['clone_url']
    repo_dir = os.path.join(BACKUP_DIRECTORY, repo_name)

    print(f'Backing up repository: {repo_name}')

    subprocess.call(['git', 'clone', '--mirror', repo_url, repo_dir])




url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
headers = {'Authorization': f'token {GITHUB_TOKEN}'}

response = requests.get(url, headers=headers)
repositories = response.json()


for repo in repositories:
    backup_repository(repo)