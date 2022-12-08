#!/usr/bin/python3
"""to display Hello HBNB! on 0.0.0.0"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """print Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
