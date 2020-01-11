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
Create `credentials.json` file with your actual credentials in the following format.

```
{
    "user":"USERNAME",
    "password": "PASSWORD",
    "database": "DATABASE_NAME"
}
```

Run `maindriver.py`.
```
python maindriver.py
```

Read the project Wiki for more details.
