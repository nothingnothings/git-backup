import requests 
import os
import subprocess


ACCOUNT_USERNAME = "nothingnothings"
ACCOUNT_TOKEN = os.environ['ACCOUNT_TOKEN']
BACKUP_DIRECTORY = 'backup-folder'


if not os.path.exists(BACKUP_DIRECTORY):
    os.makedirs(BACKUP_DIRECTORY)



def backup_repository(repo):
    repo_name = repo['name']
    repo_url = repo['clone_url']
    repo_dir = os.path.join(BACKUP_DIRECTORY, repo_name)

    print(f'Backing up repository: {repo_name}')
    if (repo_url != f'https://github.com/{ACCOUNT_USERNAME}/git-backup/'):
            subprocess.call(['git', 'clone', '--mirror', repo_url, repo_dir])




url = f'https://api.github.com/users/{ACCOUNT_USERNAME}/repos'
headers = {'Authorization': f'token {ACCOUNT_TOKEN}'}

response = requests.get(url, headers=headers)
repositories = response.json()


for repo in repositories:
    print(repo['name'])
    if repo['name'] != 'git-backup':
        backup_repository(repo)
        
        