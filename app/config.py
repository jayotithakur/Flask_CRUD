import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)


# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)

# Check the database connection
try:
    with app.app_context():
        db.create_all()
    print("Database connection successful.")
except Exception as e:
    print("Error connecting to the database:", str(e))


