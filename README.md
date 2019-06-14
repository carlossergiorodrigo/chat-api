# chat-api
This is a simple chat api developed using Flask framework

### Dependencies ###

1) flask : web micro framework
2) flask-sqlalchemy : ORM to manage entities and database
3) python-dotenv : .env files manager
4) marshmallow : for DTO schemas definitions and easy serialization and deserialization objects to/from Json
5) marshmallow-sqlalchemy
6) passlib : hashing library for manage passwords
7) flask-jwt-extended : for JWT authorization and token generation
8) pipenv : to handle development enviroments insted using pip



### .ENV File ###

    # GENERAL
    SECRET_KEY = 'assap-challenge'

    # Flask
    FLASK_ENV=development
    FLASK_DEBUG=1

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///challenge.db'

    # JWT
    JWT_SECRET_KEY = 'asapp-challenge'
