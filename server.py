from flask import Flask
from flask import render_template
import requests



app = Flask(__name__)

@app.route('/')
def home():
    pass

if __name__ == "__main__":
    app.run(debug=True)