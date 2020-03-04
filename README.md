## Course-Offering-API

Replace anything in between `<>` with the actual value. `[]` means optional.

### Terms
| Endpoint               | Description                                                              | Example          |
|------------------------|--------------------------------------------------------------------------|------------------|
| `/terms/[limit]`    | Get all terms. Optionally add a limit to the number of terms returned\.     |                  |

### Courses
| **Endpoint**                                               | **Description**                                               | **Example** |
|------------------------------------------------------------|---------------------------------------------------------------|-------------|
| `/courses/<term>/all`                                      | Get all courses for the given term.                           |             |
| `/courses/<term>/<major>`                                  | Get all courses for the given term and major.                 |             |
| `/courses/<term>/<major>/<course-number>`                  | Get all sections for the given term, major and course number. |             |
| `/courses/<term>/<major>/<course-number>/<section-number>` | Get a section for the given term, major and course number.    |             |
| `/courses/<term>/<CRN>`                                    | Get the course for the given term and CRN.                    |             |

### Majors

### Instructors

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

Run `run.py` with run as the entry point.
```
python run.py run
```

Read the project Wiki for more details.
