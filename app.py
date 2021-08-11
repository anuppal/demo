import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the hello world"

@app.route("/how")
def hello():
    return "I am good, how are you doing?"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")
