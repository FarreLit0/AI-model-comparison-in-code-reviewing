from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return "User already exists!", 400
    users[username] = password
    return "Registered successfully!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if users[username] == password:
        return "Login successful!"
    return "Invalid credentials!", 401
