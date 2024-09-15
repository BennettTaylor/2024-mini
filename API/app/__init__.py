# app/__init__.py: Flask application instance 

# app.py
# Required Imports
import os
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

username = "newtest"

# Initialize Flask App
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('key.json')

firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/data', methods=['POST'])
def upload():
    try:
        average = request.json['average']
        minimum = request.json['minimum']
        maximum = request.json['maximum']
        score = request.json['score']
        doc_ref = db.collection("response-time-data").document(username)
        doc_ref.set({"Average": average, "Maximum": maximum, "Minimum": minimum, "Score": score})
        return "Sucess!"
    except Exception as e:
        return f"An Error Occured: {e}"