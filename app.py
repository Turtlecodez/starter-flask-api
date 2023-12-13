from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"
    
@app.route("/<name>")
def user(name):
    return f"you silly goober, the page /"{name}/" doesn't exist lol"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
