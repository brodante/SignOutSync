# SignOutSync

**SignOutSync** is a web-based platform that allows users to manage their logged-in accounts across multiple devices. Users can remotely log out from any session, offering enhanced security in case of compromised devices or accounts. The project will eventually feature AI-driven tools to alert users of suspicious login activities, such as multiple failed login attempts or logins from unfamiliar locations.

## Project Layout

The project is divided into two main sections: `frontend` and `backend`, along with additional files for documentation, configuration, and license.

### Folder Structure

```bash
signoutsync/
├── backend/
│   ├── manage.py              # Django/Flask app starter script
│   ├── requirements.txt       # Python dependencies for the backend
│
├── frontend/
│   ├── src/                   # React source files
│   ├── public/                # Public static files for the frontend
│   └── package.json           # Node.js dependencies for the frontend
│
├── README.md                  # Project documentation (you're reading this)
├── CONTRIBUTING.md            # Guidelines for contributing to the project
├── LICENSE                    # License file (MIT License)
├── CODE_OF_CONDUCT.md         # Code of conduct for contributors
└── .gitignore                 # Files to be ignored by Git
```

---

## Files Overview

### 1. **`README.md`**
This file contains all the details about the project, how to set it up, the file structure, and its purpose. It serves as the main entry point for anyone looking at the project.

### 2. **`CONTRIBUTING.md`**
This document provides guidelines on how to contribute to the project, including forking, creating issues, reporting bugs, and submitting pull requests.

### 3. **`LICENSE`**
The project is licensed under the MIT License. This file contains the legal details for how the project can be used, modified, and shared.

### 4. **`CODE_OF_CONDUCT.md`**
This file sets expectations for the behavior of contributors. It outlines acceptable behavior, reporting violations, and consequences of misconduct.

### 5. **`.gitignore`**
This file specifies which files and directories should be ignored by Git. It typically includes things like compiled code, local environment variables, and dependency directories (`node_modules/` and `__pycache__/`).

---

## Features

- **View Active Sessions**: Display a list of devices and applications where the user is logged in.
- **Remote Logout**: Allow users to remotely log out of sessions to ensure security.
- **Future AI Features**: Detect multiple failed login attempts or logins from unfamiliar locations and alert the user.

---

## Getting Started

### 1. **Clone the repository**
```bash
git clone https://github.com/brodante/signoutsync.git
cd signoutsync
```

### 2. **Backend Setup**
Install the required Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

Start the backend server:
```bash
python manage.py runserver
```

### 3. **Frontend Setup**
Install the required Node.js dependencies:
```bash
cd frontend
npm install
```

Start the frontend development server:
```bash
npm start
```

---

## Tech Stack

- **Frontend**: React.js, TailwindCSS
- **Backend**: Python (Django/Flask)
- **Database**: PostgreSQL/MongoDB
- **Authentication**: OAuth 2.0, JWT
- **AI (Future)**: TensorFlow/PyTorch for login behavior anomaly detection

---

## Contribution

We welcome contributions! Whether it's bug fixes, new features, or documentation improvements, feel free to make a pull request. Please review our [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
