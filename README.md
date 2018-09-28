# Food Service API

A simple **REST API** allowing users to _CREATE_ orders. Then, they are able to _READ_, _UPDATE_ and _DELETE_ them.

![Build Status](https://travis-ci.org/Chell0/food-api.svg?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/46542d1e81b90842b0bf/maintainability)](https://codeclimate.com/github/Chell0/food-api/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/46542d1e81b90842b0bf/test_coverage)](https://codeclimate.com/github/Chell0/food-api/test_coverage)

## Prerequisites

What you need to run this API.

1. Python 3.
2. Virtualenv environment.
3. Postman.

## Installing

How to get your development environment running.

- Clone the repository.
- Unzip the files to your preferred location.
- **cd**  into the **api** folder.
- Install a virtual environment _pip install virtualenv venv_
- Install the requirements.txt _pip install -r requierments.txt_
- Install [Postman](https://www.getpostman.com/).

## Running Tests

```cd``` into ```app``` RUN ```python app.py```.
- Click [here](https://documenter.getpostman.com/view/4006766/RWaRPRJm) to test every endpoint:

```html

key: Content-Type value: application/json

```

```html

GET  http://127.0.0.1:5000/v1/orders/ (get all your orders)
POST http://127.0.0.1:5000/v1/orders/ (create a new order)
GET http://127.0.0.1:5000/v1/orders/<name> (get a specific order by name)
PUT http://127.0.0.1:5000/v1/orders/<name> (update an existing order)
DELETE http://127.0.0.1:5000/v1/orders/<name> (delete a specific order by name)

```