from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(12)


##connect mySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cindy2421342235@localhost/petservice'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from Petservice import routes