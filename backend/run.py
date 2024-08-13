from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Your existing routes and logic

if __name__ == '__main__':
    app.run(debug=True)
