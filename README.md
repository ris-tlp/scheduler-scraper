## Setup
Install `pipenv` if you haven't already.
```
pip install pipenv
```

Navigate to the project directory and run the following command to create/activate the virtual environment. 
```
pipenv shell
```

Install all required dependencies.
```
pipenv install
```

Any new dependency must be installed using:
```
pipenv install <package-name>
```

## Usage
Update the `credentials.json` file with your actual credentials. You may have to run the following command to stop git from tracking the file.

```
git update-index --assume-unchanged credentials.json
```

Run `maindriver.py`.
```
python maindriver.py
```

Read the project Wiki for more details.
