from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
login_manager = LoginManager()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR,'static\profile_images\\')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] =  "Kkr@6362"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)



from Weather_app.core.views import core
from Weather_app.user.views import users
from Weather_app.weather.views import weather

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(weather)
