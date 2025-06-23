---
title: "🛠️Flask Project"
date: 2025-04-14
draft: false
showInHome: false
---
Getting Started with Flask: A Super Simple Guide for Beginners

If you're new to Python web development, Flask is the perfect place to start! It's lightweight, beginner-friendly, and lets you build web apps quickly.

Let’s walk through a very simple Flask project, explain every line in detail:

🔧 What is Flask?

Flask is a small Python framework used to build websites and web applications.

    Lightweight and easy to use

    Fast to build and test

    Great for learning web development

🛠️ The Simplest Flask App (Hello World)

Here’s the full code for the simplest Flask app:

from flask import Flask

app = Flask(__name__)  # 🌱 Create the Flask app

@app.route('/')        # 🏠 Define the homepage route
def home():
    return "👋 Hello, World! Welcome to Flask! 🚀"

if __name__ == '__main__':
    app.run(debug=True)  # 🔁 Run the development server

🧠 Line-by-Line Explanation
1️⃣ from flask import Flask

    This imports the Flask class from the flask library.

    You're saying: “Hey Python, I want to use Flask in this file.”

2️⃣ app = Flask(__name__)

    Flask(__name__) creates the web app.

    __name__ is a special Python variable. It helps Flask find your files.

    app is just a variable name — you can rename it to anything (like sanaz, website, etc.) as long as you use the same name consistently.

3️⃣ @app.route('/')

    This is a route decorator.

    It means: “When someone visits / (the homepage), run the function below.”

    / is just the root of the website (like http://localhost:5000/).

4️⃣ def home():

    This defines the function that runs when someone visits the homepage.

    You can name this function anything (like hello()), but home() is a clear choice.

5️⃣ return "👋 Hello, World! Welcome to Flask! 🚀"

    This sends text back to the browser when someone visits the route.

    It’s what the user sees on their screen.

6️⃣ if __name__ == '__main__':

    This checks if you're running this file directly (not importing it).

    If yes, then the app starts.

7️⃣ app.run(debug=True)

    This starts Flask’s built-in development server.

    debug=True enables:

        🔁 Auto-reload when code changes

        📢 Helpful error messages in the browser

🌐 Why localhost:5000?

When you run app.run(), Flask automatically:

    Runs on localhost → your own computer

    Uses port 5000 → a default number for Flask

So you access your site at:

http://localhost:5000/

🛠 Can You Change It?

Yes! You can change host and port:

app.run(host='0.0.0.0', port=8000)

    0.0.0.0 lets others on your network access your app

    8000 is a new port number

Now your app would be at: http://localhost:8000/


you can run your app :
1-navigate to the folder where your app.py is located.

cd path/to/your-project-folder

📦 2. Make Sure Flask is Installed

If you haven't installed Flask yet, run this:

pip install flask

✅ You should see a message like Successfully installed Flask.
🏃 3. Run Your App

Now run your app by typing:

python app.py

Enjoy :)



