import os
import connexion
import logging
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth 
from werkzeug.security import check_password_hash, generate_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# DB root path
db_root_path = os.path.join(basedir, "db")
# Database file name
db_filename = "agents.db"
db_file_path = os.path.join(db_root_path, db_filename)

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + db_file_path

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

fileHandler = RotatingFileHandler('rengacloud.log', maxBytes=1000000, backupCount=1)
fileHandler.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandler)
rootLogger.addHandler(consoleHandler)

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# 3rd party modules
from flask import render_template

import flask
# Stops app from crashing when started as a service
flask.cli.show_server_banner = lambda *args: None

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')
multi_auth = MultiAuth(basic_auth, token_auth)

users = {
    "admin": generate_password_hash("!top_secret__!"),
}

tokens = {
    "!top_secret__!": "admin"
}


@basic_auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@token_auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]	

# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")