from app import create_app
from config import Config

# Create the Flask app using the factory function
app, db, bcrypt = create_app()

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=Config.DEBUG, port=Config.PORT)

