import os, sys, time, json, logging, csv
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# setup logging
base_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(base_dir,'wordcounter.log'),level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    # do some stuff
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
