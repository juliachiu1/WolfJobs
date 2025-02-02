from flask import Flask
from flask_pymongo import PyMongo
from flask_mail import Mail
import database

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'secret'
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
        #self.mongo = PyMongo(self.app)
        self.mongo = database

        # self.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        # self.app.config['MAIL_PORT'] = 465
        # self.app.config['MAIL_USE_SSL'] = True
        # # self.app.config['MAIL_USERNAME'] = "wolfjobs.ncsu@gmail.com"
        # # self.app.config['MAIL_PASSWORD'] = "W00FW00F"
        # self.app.config['MAIL_USERNAME'] = "bogusdummy123@gmail.com"
        # self.app.config['MAIL_PASSWORD'] = "helloworld123!"
        self.mail = Mail(self.app)
