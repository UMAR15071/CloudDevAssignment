from flask import Flask
from Swimmers import swim_utils

app = Flask(__name__)

from Swimmers import route

if(__name__ == "__main__"):
    app.run(debug = True)