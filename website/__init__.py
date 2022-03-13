from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize the Database
db = SQLAlchemy()
DB_NAME = "user.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JSM'

    # Add Database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:root@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    return app
