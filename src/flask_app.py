from flask import Flask
from get_data import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "First value is " + get_data()['Facility_Name'][0]