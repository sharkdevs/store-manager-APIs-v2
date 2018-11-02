[![Build Status](https://travis-ci.org/sharkdevs/store-manager-APIs-v2.svg?branch=develop)](https://travis-ci.org/sharkdevs/store-manager-APIs-v2)
[![Coverage Status](https://coveralls.io/repos/github/sharkdevs/store-manager-APIs-v2/badge.svg?branch=develop)](https://coveralls.io/github/sharkdevs/store-manager-APIs-v2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/e8d05349e313293cab9c/maintainability)](https://codeclimate.com/github/sharkdevs/store-manager-APIs-v2/maintainability)

# store-manager-APIs-v2
Store manager API Version 2 is a collection of API endpoints that enable store users to manipulate and manage the store. The users are in two categories, Administrators and attendants. Each of the categories needs authorization to access their bvarious endpoints

Data of the API endpoints is persisted through a postgres database that is hosted in heroku alongside  the application. 

## API Endpoints covered included in this branch


| Method        |       Endpoint                |         Description               |
| ------------- |       -------------           |         -------------             |
| `POST`        |  `/api/v2/auth/login`         |           login a user            |
| `POST`        |  `/api/v2/auth/signup`        |           register  a user        |
| `POST`        |  `/api/v2/products`           |           add a product           |
| `GET`         |  `/api/v2/products`           |           Get all product         |
| `GET`         |  `/api/v2/products/<int:id>`  |           Get a product by id     |
| `PUT`         |  `/api/v2/products/<int:id>`  |           UPDATE a product by id  |
| `DELETE`      |  `/api/v2/products/<int:id>`  |           DELETE a product by id  |
| `POST`        |  `/api/v2/sales`              |           Make a sale order       |
| `GET`         |  `/api/v2/sales`              |           Get all sale orders     |
| `GET`         |  `/api/v2/sales/<int:id>`     |           Get one sale order      |

## Set Up instructions
The following are a set of steps you can follow to set tu the application
#### Cloning the application
git clone https://github.com/sharkdevs/store-manager-APIs-v2/

 #### Configure Virtual environment
     pip install Virtialenv
     virtualenv venv
     source /venv/Scripts/activate : windows  
     source /venv/bin/activate : linux

   ### Install dependancies
     pip install -r requirements.txt
    
## Unit Testing
To test the endpoints, ensure that the following tools are available the follow steps below
   ### Tools and dependancies required:
    -Postman
    -nose test runner
    -postgres Database
  ### Commands
  The application was tested using `nose` and `coverage`. To run the tests on the bash terminal use
     
  `nosetests --with-coverage --cover-package=app  && coverage report`
     
## Deployment

The app is deployed in heroku [Click here ](https://shark-store-v2.herokuapp.com/). Click 
after it opens, append the specific endpoint. 
ie `<url>/api/v2/sales`

## Author 

[Meshack Ogeto ](https://github.com/sharkdevs)