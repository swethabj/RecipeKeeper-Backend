# your_app_name.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Flask
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# Add other configurations as needed

db = SQLAlchemy(app)

# Define User model (assuming you have a User model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define your routes and other components below
# ...

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG') == 'True')
