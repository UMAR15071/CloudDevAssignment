from flask import Flask
from Swimmers import swim_utils

app = Flask(__name__)
app.secret_key = 'a_secret_key'

from Swimmers import route

if(__name__ == "__main__"):
    app.run(debug = True)
    