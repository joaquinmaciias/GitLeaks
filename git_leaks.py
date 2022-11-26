#!user/bin/python3

# git init
# Module GitPython: python -m pip install gitpython
# Module entorno virtual: python -m venv env
# Create a virtual enviroment: env/Scrips >> .\activate
# Data extraction: git clone https://github.com/skalenetwork/skale-manager
# Create: .gitignore

from git import Repo

import re, signal, sys

# Finish the process with  Ctrl + C
def handler_signal(signal, frame):
    print('\n\n [!] Out ....... \n')
    sys.exit(1)

signal.signal(signal.SIGINT, handler_signal)

# Extraction

def extract(path):
    repo = Repo(path)       # Create an object which allows you to interact with the repository what's is the path
    return repo.iter_commits()

# Tranformation

def transform(commits, length):

    compile_key = input('Write a word that you want to find: ')

    list_all_matches = []

    pattern = re.compile(r'.*'+compile_key+'.*', re.IGNORECASE)

    print('Finding matches...\t')

    for commit in commits:
        matches = pattern.finditer(commit.message)
        if matches: list_all_matches.append(matches)
    
    print('Finished\n')

    return matches, list_all_matches

# Load data on the screen

def load(matches, list_all_matches):

    counter = 0

    print('The matches are: ')
    for matches in list_all_matches:
        for match in matches:
            counter += 1
            print(f'{counter} match is:',match)
    print('\n')

if __name__ == '__main__':

    REPO_DIR = './skale-manager'

    commits = extract(REPO_DIR)

    length = len(list(commits))

    matches, list_all_matches = transform(extract(REPO_DIR), length)

    load(matches, list_all_matches)