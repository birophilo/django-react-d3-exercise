# Saatchi exercise (Django-React-D3)





# Artfinder exercise



## Install backend

```bash
# clone the repo
$ git clone git@github.com:birophilo/django-react-d3-exercise.git
$ cd django-react-d3-exercise/automotive-backend

# create and initialize a virtual environment
$ python -m venv env
$ source env/bin/activate

# install the requirements
$ pip install -r requirements.txt

# initialise the database
$ python manage.py migrate
```

Then to populate the local database copy your the interview-data.csv file into the top level project directory and run a Django management command:

```bash
$ python manage.py import_csv_data.csv
```

(The data has been excluded from the repo.)

```bash
$ python manage.py runserver
```


## Install frontend

From the `django-react-d3` project root directory:

```bash
$ cd automotive-frontened
$ npm install

# start the React development server
$ npm start
```

