from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

app = Flask(__name__, template_folder=parent + '/frontend/public')

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3001)