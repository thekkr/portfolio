from Weather_app import login_manager,db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):

    __tablename__ = "Users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True)
    email = db.Column(db.String(128),index=True,unique=True)
    profile_image = db.Column(db.String(256),nullable=False,default="default_profile.png")
    password_hash=db.Column(db.String(128))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username :{self.username}"
