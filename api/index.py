from flask import Flask
from os import getcwd, listdir

app = Flask(__name__)

@app.route('/')
def home():
    return f"{getcwd()}, {listdir()}"
