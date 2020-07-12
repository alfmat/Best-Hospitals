from flask import Flask
from flask import render_template
from get_data import *


app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def hello_world():
    return render_template('index.html')