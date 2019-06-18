# CHAT-API
This is a simple chat api developed using Flask framework

## Dependencies ##

1) flask : web micro framework
2) flask-sqlalchemy : ORM to manage entities and database
3) python-dotenv : .env files manager
4) marshmallow : for DTO schemas definitions and easy serialization and deserialization objects to/from Json
5) marshmallow-sqlalchemy
6) passlib : hashing library for manage passwords
7) flask-jwt-extended : for JWT authorization and token generation
8) pipenv : to handle development enviroments insted using pip

## Running the project ##
### Install pipenv ###
I decide use pipenv over the regular pip because the simplicity of not only handling packages but also manage virtual enviroments at the same time. 

    > pip install pipenv
    

### Installing dependencies ###
All the packages described in the #dependencies section can be installed using the following command:

    > pipenv install

### .ENV File ###
Is necessary to create a file with different environments variables that the api will use at certains momments. The file is a .env file that could be created using vim in the root folder of the project

    > vim .env
    
And completed with the following content

    # GENERAL
    SECRET_KEY = 'challenge'

    # Flask
    FLASK_ENV=development
    FLASK_DEBUG=1

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///challenge.db'

    # JWT
    JWT_SECRET_KEY = 'challenge'

### Running the app ###
To start the app and testing the api you can use the script start.sh located in the root folder

    > ./start.sh
    
It is posible that you need to set it as an executable file first using 
    
    > chmod +x start.sh
    
### Docker ###
The code also include the dockerfile to run the app in a docker container. If you choose run the app in this way, remember tell to docker the existence of the .env file
    
    > docker run --env-file .env --name chat-api -d -p 8080:8080 chat-api

### Test ###

And that's it... you can start testing the api :)

I create this postman collection that I like to share

    https://www.getpostman.com/collections/8fe6c6ef5a171eb024a4

## Feedback ##
Your feedback is always welcome, please write me to my personal email hi@carlosrodrigo.me
