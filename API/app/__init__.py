# app/__init__.py: Flask application instance 

# app.py
# Required Imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask App
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()

response_time_data_ref = db.collection('response-time-data')

@app.route('/data', methods=['POST'])
def upload():
    try:
        average = request.json['average']
        print(average)
    except Exception as e:
        return f"An Error Occured: {e}"