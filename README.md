# pricing_test

## Setup

Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install requirements

```
make install
```

Before loading the database, ensure the Data.csv (with the exact name) file is in the main directly of the repo / in the same folder as manage.py

To load the database with the data from the csv:

```
make load_db
```


## Running Locally

Running the service

```
make service
```

Access the quiz by clicking [here](http://127.0.0.1:8000/admin/) or opening a new browser tab and going to:

```
http://127.0.0.1:8000/admin/
```

## Create Superuser

Create a superuser with username/email & password

```
python manage.py createsuperuser
```

Log into the admin portal, then click on the Quotes or navigate to:

```
http://127.0.0.1:8000/admin/dashboard/quotes
```


## Testing

To run tests

```
make test
```


## Extra

If you want to clear the database at any point

```
make clear_db
```
