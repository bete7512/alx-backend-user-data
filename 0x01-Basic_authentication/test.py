#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port)




from flask import Flask

app = Flask(__name__)




