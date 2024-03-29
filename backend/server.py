from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

app = Flask(__name__, template_folder=parent + '/frontend/build')

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=port)