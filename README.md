[![Build Status](https://travis-ci.org/sharkdevs/store-manager-APIs-v2.svg?branch=ft-user-registration-161580805)](https://travis-ci.org/sharkdevs/store-manager-APIs-v2)
[![Coverage Status](https://coveralls.io/repos/github/sharkdevs/store-manager-APIs-v2/badge.svg)](https://coveralls.io/github/sharkdevs/store-manager-APIs-v2)
[![Maintainability](https://api.codeclimate.com/v1/badges/e8d05349e313293cab9c/maintainability)](https://codeclimate.com/github/sharkdevs/store-manager-APIs-v2/maintainability)

# store-manager-APIs-v2
Create a API endspoints that allows the user to login and administrators to register

## API Endpoints covered included in this branch


| Method        |       Endpoint                |         Description               |
| ------------- |       -------------           |         -------------             |
| `POST`        |  `/api/v2/auth/login`         |           login a user            |
| `POST`        |  `/api/v2/auth/signup`        |           register  a user        |
| `POST`        |  `/api/v2/products`           |           add a product           |

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
To test the endpointsensure that the following tools are available the follow steps below
   ### Tools:
     Postman
### Commands
  The application was tested using `nose` and coverage. To run the tests on the bash terminal use
     
     nosetests --with-coverage --cover-package=app  && coverage report
     
## Deployment

The app is deployed in heroku. Click [here](https://shark-store-manager.herokuapp.com/)
after it opens, append the specific endpoint. 
ie `<url>/api/v2/products`

## Author

[Meshack Ogeto ](https://github.com/sharkdevs)