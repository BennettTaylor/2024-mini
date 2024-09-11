# app/__init__.py: Flask application instance 

from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('path/to/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__) 

from app import routes