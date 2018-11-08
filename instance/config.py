import os

class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

class Development(Config):
    DEBUG = True
    TESTING = True
    DB_URL = os.environ.get('DATABASE_URL')
class Production(Config):
    DEBUG = False
    TESTING = False

class Testing(Config):
    DEBUG = True
    TESTING = True
    DB_URL = os.environ.get('TEST_DB_URL')    

app_config = {
    "development" : Development,
    "testing" : Testing,
    "production" : Production
}
