from flask import Flask 
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt


app = Flask(__name__) 
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = '41f986378b9b792cd44e7350'

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass@123'
app.config['MYSQL_DB'] = 'RecipeKeeper'

mysql = MySQL(app) 
CORS(app) 
CORS(app, origins=["http://localhost:3000"])  

from app import routes