from app import db  
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'  # Specify the actual table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email_address = db.Column(db.String(150), unique=True, nullable=False)
    password_hash =  db.Column(db.String(100),  nullable=False)
    user_image_path =  db.Column(db.String(255),  nullable=True)
    last_password_updated_on = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    created_by = db.Column(db.String(25),  nullable=False, default='Application')
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    last_edited_by = db.Column(db.String(25), nullable=False, default='Application')
    last_edited_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Users {self.username}>"
