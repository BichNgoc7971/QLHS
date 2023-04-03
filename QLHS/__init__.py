from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = 'JHGHJGHT&^&*%&^*%&*%^&$^&RFHJGVHJVGHJFGHFGH'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/qlhsdb?charset=utf8mb4" \
                                        % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
login = LoginManager(app)

cloudinary.config(cloud_name='dmz40knqc', api_key='793927371723943', api_secret='gS7qToerpP9bSKsiXxWl7bfc0SM')