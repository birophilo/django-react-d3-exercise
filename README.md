# Saatchi exercise (Django-React-D3)



## Installation: with Docker

Make sure Docker Desktop is running on your machine, then:

```bash
# clone the repo
$ git clone git@github.com:birophilo/django-react-d3-exercise.git
```

Then copy your CSV file `interview-data.csv` into the directory: `django-react-d3-exercise/automotive-backend` (the Django project root directory). This has been deliberately left out of source control. This will be imported into the database during the Docker build.

Then back in your terminal:

```bash
# cd into repo top level directory
$ cd django-react-d3-exercise

# build and run the Docker containers
$ docker-compose up --build -d
```

Then after a few moments (while React dev server starts), you should be able to access:

- React frontend at http://localhost:3000
- Django API backend at http://localhost:8000



## Without Docker: Install backend

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

Then to populate the local database, copy your the `interview-data.csv` file into the `automotive-backend` directory (the Django project directory)  and run a Django management command:

```bash
$ python manage.py import_csv_data
```

(The data has been excluded from the repo.)

```bash
$ python manage.py runserver
```



## Without Docker: Install frontend

From the `django-react-d3` project root directory:

```bash
$ cd automotive-frontend

# install the requirements
$ npm install

# start the React development server (at http://localhost:3000)
$ npm start
```

(if `npm` is not installed you will need to install it first: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm.)



## Using the API

The backend uses a single resource endpoint, `feedbacks` (a light-hearted grammatical reach, to respect the plural naming conventions of REST APIs!).

```bash
# return all feedback items unfiltered
http://localhost:8000/feedbacks/
```



### Filtering

Filtering options:

- model
- brand
- feedback subcategory
- country code



The Feedback item is in the format:

```json
[
  {
    "customer_id": 123456,
    "post_date": "2025-01-03",
    "country_code": "UK",
    "brand": "Tesla",
    "model": "Model 3",
    "ownership_status": "Owner",
    "feedback_sentiment": "Positive",
    "feedback_subcategory": "Brand/Product Pride"
  }
]
```



Use camel case in query parameters:

```bash
# filter by model and country
http://localhost:8000/feedbacks?brand=Tesla&countryCode=UK

# filter by model and feedback subcategory
http://localhost:8000/feedbacks?model=Enyaq&feedbackSubcategory=Quality
```



### Grouping by date

It is also possible to group items by date using a `feedbacks/` query parameter. This is a convenient data aggregation at the database query stage for efficient performance. It returns a count of all sentiment values of feedback responses for that given date. Format:

```json
[
  {
    "post_date": "2025-01-30",
    "positive": 27,
    "neutral": 16,
    "negative": 19
  }
]
```



Use the parameter `groupBy` with the options:

- `day`
- `month`
- `year`

```bash
# return all items grouped by date
http://localhost:8000/feedbacks?groupBy=day

# return all feedback about price grouped by month
http://localhost:8000/feedbacks?feedbackSubcategory=Price&groupBy=month
```



## Frontend display

This exercise uses three different approaches to display charts for comparison:

- D3.js
- Recharts - an open-source chart library for React built on top of D3.
- Pure React components with CSS.

These are the first, second and third sections of the frontend page respectively. Each approach has its pros and cons and best-fit use cases.

Code for comparison:

- D3: https://github.com/birophilo/django-react-d3-exercise/blob/main/automotive-frontend/src/components/OverallSentimentChart.jsx
- Recharts: https://github.com/birophilo/django-react-d3-exercise/blob/main/automotive-frontend/src/components/IssueStackedChart.jsx
- Pure React/VirtualDOM framework: https://github.com/birophilo/django-react-d3-exercise/blob/main/automotive-frontend/src/components/CountrySummaryChart.jsx

