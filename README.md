# GitLeaks
 Finder of Git Repository's  Leaks

Data from: https://github.com/skalenetwork/skale-manager

Before start the python file make in the windows console:

1. Start git: git init
2. Install a virtual enviroment with venv: python -m pip install virtualenv 
3. Create a virtual enviroment: python -m venv env
4. Activate virtual enviroment:
 - Move to: cd .\env\Scripts\
 - Start: activate
5. Install packages for the python file: pip install -r requirements.txt
6. Extract data from Skale: git clone https://github.com/skalenetwork/skale-manager
7. Run the python file: python git_leaks.py
8. Deactivate virtual enviroment:
- Move to: cd .\env\Scripts\
 - Start: deactivate
