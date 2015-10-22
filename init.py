from flask import Flask
from flask.ext.cors import CORS
from flask.ext.restful import Api
from db.model import db

app = Flask(__name__)

config = app.config
config.from_pyfile('app.properties')

db.init_app(app)

CORS(app)
api = Api(app)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.