import requests 
import os
import subprocess


ACCOUNT_USERNAME = os.environ['ACCOUNT_USERNAME']
ACCOUNT_TOKEN = os.environ['ACCOUNT_TOKEN']
BACKUP_DIRECTORY = 'backup-folder'

print(ACCOUNT_USERNAME, ACCOUNT_TOKEN)


if not os.path.exists(BACKUP_DIRECTORY):
    os.makedirs(BACKUP_DIRECTORY)



def backup_repository(repo):
    repo_name = repo['name']
    repo_url = repo['clone_url']
    print(repo_url, "REPO URL")
    repo_dir = os.path.join(BACKUP_DIRECTORY, repo_name)

    print(f'Backing up repository: {repo_name}')
    if repo['name'] != '***':
        subprocess.call(['git', 'clone', '--mirror', repo_url, repo_dir])




url = f'https://api.github.com/users/{ACCOUNT_USERNAME}/repos'
headers = {'Authorization': f'token {ACCOUNT_TOKEN}'}

response = requests.get(url, headers=headers)
repositories = response.json()


for repo in repositories:
    print(repo['name'])
    if repo['name'] != 'github_backup' and repo['name'] != 'DefinitelyTyped' and repo['name'] != '***':
        backup_repository(repo)
