from app import app, mysql 
from flask import  jsonify, request
import hashlib
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/', methods=['POST'])
def health_check():
    return jsonify({'status': 'ok'})


@app.route('/members')
def recipekeeper_page():
    return {"members":["Member1","Member2", "Member3"]}

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        # Hash the password
        #hashed_password = bcrypt.generate_password_hash(password.encode('utf-8'), bcrypt.gensalt())

        hashed_password = hash_password(password)
        print(hashed_password)

    
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO RecipeKeeper.users
                    (userName, emailAddress, passWord, created_by, created_at, last_edited_by, last_edited_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (username, email, hashed_password, 'application', current_time, 'application', current_time))

        mysql.connection.commit()
        cur.close()

        response = {
            'message': 'User registered successfully',
            'status': 'success'
        }

        return jsonify(response), 201  # 201 Created

    except KeyError as e:
        error_message = f'Missing required field: {str(e)}'
        return jsonify({'error': error_message, 'status': 'error'}), 400  # 400 Bad Request

    except Exception as e:
        error_message = 'Internal Server Error'
        print(f'Error: {str(e)}')
        return jsonify({'error': error_message, 'status': 'error'}), 500  # 500 Internal Server Error
    

def hash_password(password):
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return hashed_password