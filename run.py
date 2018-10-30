import os
from app import create_app
from instance.config import app_config

app = create_app("development")

if __name__ == '__main__':
    app.run()