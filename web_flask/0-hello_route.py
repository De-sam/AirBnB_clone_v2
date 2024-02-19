#!/usr/bin/python3
""" initiates a Flash Web Application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints  Hello HBNB when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
