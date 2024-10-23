from flask import Flask, jsonify, request, session
from datetime import datetime, timedelta
import uuid
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set a strong secret key for session management from environment variable
app.secret_key = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# In-memory storage for users and sessions (this is for demo purposes, replace with actual DB in production)
users_db = {
    'testuser': {'password': os.getenv('TESTUSER_PASSWORD'), 'devices': []}  # Example user
}

# Basic status check route
@app.route('/')
def index():
    return jsonify({"message": "SignOutSync Backend Running"}), 200

# User authentication function
def authenticate(username, password):
    # Check if user exists in the users_db and the password matches
    user = users_db.get(username)
    if user and user['password'] == password:
        return True
    return False

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    # Validate that both username and password are provided
    if 'username' not in data or 'password' not in data or 'device_name' not in data:
        return jsonify({"message": "Username, password, and device name are required!"}), 400

    username = data['username']
    password = data['password']
    device_name = data['device_name']
    device_id = str(uuid.uuid4())  # Generate a unique device identifier
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    user_agent = request.headers.get('User-Agent')  # Get User-Agent from request headers

    # Perform authentication
    if authenticate(username, password):
        session['user'] = username
        session['device'] = device_id  # Store the unique device identifier in the session
        session.permanent = True  # Mark the session as permanent (honors session lifetime)

        # Add the device to the user's devices list in the database
        user = users_db.get(username)
        user['devices'].append({
            'device_id': device_id,
            'device_name': device_name,
            'login_time': login_time,
            'user_agent': user_agent
        })  # Append new device to user's devices list

        return jsonify({
            "message": f"Logged in from {device_name} at {login_time}",
            "device_id": device_id,
            "user_agent": user_agent
        }), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    if 'user' in session and 'device' in session:
        username = session['user']
        device_id = session['device']  # Get the stored device identifier
        user = users_db.get(username)

        if not user:
            return jsonify({"message": "User not found in the database!"}), 404

        # Find the device in the user's devices list
        device_info = next((device for device in user.get('devices', []) if device['device_id'] == device_id), None)

        if device_info:
            device_name = device_info['device_name']
            user_agent = device_info['user_agent']
            logout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time

            # Remove the device from the user's devices list
            user['devices'] = [device for device in user.get('devices', []) if device['device_id'] != device_id]

            # Clean up the session for the current device
            session.pop('device', None)
            session.pop('user', None)

            return jsonify({
                "message": f"Logged out from {device_name} at {logout_time}",
                "device_id": device_id,
                "user_agent": user_agent
            }), 200
        else:
            return jsonify({"message": "Device not found!"}), 404
    else:
        return jsonify({"message": "No active session found!"}), 401

# View active devices
@app.route('/devices', methods=['GET'])
def view_devices():
    username = request.args.get('username')
    if username:
        user = users_db.get(username)
        if user:
            return jsonify({"devices": user['devices']}), 200
    return jsonify({"message": "No active session found!"}), 401

if __name__ == '__main__':
    app.run(debug=True)