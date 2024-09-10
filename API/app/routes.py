# app/routes.py

from app import app

@app.route('/')
@app.route('/upload')
def index():
    return "Hello, World!"