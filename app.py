# app.py
from flask import Flask, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def form():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form['name']
    email = request.form['email']
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"Thanks {name}, file uploaded!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
