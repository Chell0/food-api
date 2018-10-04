# Food Service API

[![Build Status](https://travis-ci.org/Chell0/food-api.svg?branch=develop)](https://travis-ci.org/Chell0/food-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/46542d1e81b90842b0bf/maintainability)](https://codeclimate.com/github/Chell0/food-api/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/46542d1e81b90842b0bf/test_coverage)](https://codeclimate.com/github/Chell0/food-api/test_coverage)

A simple **REST API** allowing users to _CREATE_ orders. Then, they are able to _READ_, _UPDATE_ and _DELETE_ them.

## Development SetUp

What you need to run this API.

1. Python 3.
2. Virtualenv environment.
3. Postman.

## Installation

How to get your development environment running.

- Clone the repository.
- Unzip the files to your preferred location.
- **cd** into the **food-api** folder.
- Install a virtual environment _pip install virtualenv venv_
- Install the requirements.txt _pip install -r requierments.txt_
- Install [Postman](https://www.getpostman.com/).

## Running Tests

- `cd` into `food-api` RUN `python run.py`.

```html
key: Content-Type value: application/json
```

| Methods | Endpoint                                 | Action                            |
| ------- | ---------------------------------------- | --------------------------------- |
| GET     | http://127.0.0.1:5000/v1/orders          | (get all your orders)             |
| POST    | http://127.0.0.1:5000/v1/orders          | (create a new order)              |
| GET     | http://127.0.0.1:5000/v1/orders/order_id | (get a specific order by name)    |
| PUT     | http://127.0.0.1:5000/v1/orders/order_id | (update an existing order)        |
| DELETE  | http://127.0.0.1:5000/v1/orders/order_id | (delete a specific order by name) |

## Release History

+ 0.1.0
  
    + The first proper release

## Meta

Gabriel Machel - [@Ch3ll0h](https://twitter.com/Ch3ll0h) - machelgabriel@gmail.com

http://github.com/Chell0/food-api

## Contributing

1. Fork it (yourname/yourproject/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
