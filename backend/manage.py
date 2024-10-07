from flask import Flask, jsonify, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a strong secret key for session management
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Set session lifetime to 30 mins

# In-memory storage for users and sessions
users_db = {
    'testuser': {'password': 'password', 'devices': []}  # Example user
}

# Basic status check route
@app.route('/')
def index():
    return jsonify({"message": "SignOutSync Backend Running"}), 200

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user exists and password matches
    user = users_db.get(username)
    if user and user['password'] == password:
        # Simulating device info (could be from request headers in real-world scenarios)
        device = request.headers.get('User-Agent', 'Unknown device')

        # Add device to user's active devices list
        if device not in user['devices']:
            user['devices'].append(device)

        # Create session for the user
        session['user'] = username
        session['device'] = device
        session.permanent = True  # Session will persist for the duration set in config

        return jsonify({"message": f"Logged in as {username} from {device}"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    # Check if the user is logged in
    if 'user' in session:
        username = session['user']
        device = session.get('device')  # Use .get() to safely access 'device' key
        user = users_db.get(username)

        if not user:
            return jsonify({"message": "User not found in the database!"}), 404

        # Remove only the device from the user's active devices list
        if device and device in user.get('devices', []):
            user['devices'].remove(device)
            # Update user data in the database
            users_db[username] = user  # Save updated user data

        # Remove only the device info from the session, but keep the session intact
        session.pop('device', None)

        return jsonify({"message": f"Logged out from {device}"}), 200
    else:
        return jsonify({"message": "No active session found!"}), 401



# View active devices
@app.route('/devices', methods=['GET'])
def view_devices():
    # Check if user is logged in
    if 'user' in session:
        username = session['user']
        user = users_db.get(username)
        if user:
            return jsonify({"devices": user['devices']}), 200
    return jsonify({"message": "No active session found!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
