---
title: "🛠️Building a Dockerized Flask + React App"
date: 2025-04-14
draft: false
showInHome: false
---
📌 Project Goal

In this project, I set out to build a simple full-stack web application using:

    Flask (Python) as the backend API

    React as the frontend

    Docker to containerize and run the whole app

The goal was to serve the React frontend using Flask and make API calls from React to Flask—all within a Docker container.
🧱 Tech Stack

    Frontend: React

    Backend: Flask + Flask-CORS

    Containerization: Docker

🌐 What the App Does

    React frontend displays a simple UI with a message.

    It fetches the message from a Flask API endpoint: /api/hello.

    Flask serves both the API and the built React frontend.

The message displayed is:

    "Hello Sanaz from Flask!"

🧩 Flask Code

Here’s a simplified version of my app.py:

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend/build')
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello Sanaz from Flask!'})

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

⚛️ React Code (App.js)

import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/hello')
      .then(res => res.json())
      .then(data => setMessage(data.message));
  }, []);

  return (
    <div>
      <h1>This is Sanaz React</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

🐳 Docker Workflow

Here’s how I built and ran the app using Docker:
✅ Step 1: Build the React frontend

cd frontend
npm install
npm run build
cd ..

✅ Step 2: Build the Docker image

docker build -t myflaskreactapp .

✅ Step 3: Run the Docker container

docker run -p 5000:5000 myflaskreactapp

❗ Issues I Faced 

    ❌ Connection was reset
    🔍 Problem: Flask was binding to 127.0.0.1 inside the container.
    ✅ Solution: I changed app.run() to use host='0.0.0.0'.

    ❌ Port 5000 already in use
    🔍 Problem: Docker couldn’t bind port 5000 because another process was using it.
    ✅ Solution: I used sudo lsof -i :5000 to find and kill the process or ran Docker on a different port.

    ❌ React static files not loading (404 errors)
    🔍 Problem: Flask didn’t have a route to serve /static/* assets.
    ✅ Solution: I added a route to serve static files using send_from_directory.

💡 What I Learned

    How to build and serve a React app from a Flask backend

    How to use Docker to package both frontend and backend

    Common deployment and networking issues in Docker

    The importance of mapping paths and routes carefully

✅ Final Result

After resolving all the issues, I was able to successfully:

    Build the React app

    Serve it via Flask from inside Docker

    Fetch data from Flask API to React frontend

    Access the app at http://localhost:5000