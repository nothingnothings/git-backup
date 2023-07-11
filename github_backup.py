import requests 
import os
import subprocess


GITHUB_USERNAME = os.environ['ACCOUNT_USERNAME']
GITHUB_TOKEN = os.environ['ACCOUNT_TOKEN']
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
    if repo['name'] != 'github_backup':
        backup_repository(repo)