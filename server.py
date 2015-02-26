import os, sys, time, json, logging, csv
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# setup logging
base_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(base_dir,'wordcounter.log'),level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    #this means the form was submitted
	if request.method == 'POST':
		bagOfWords = request.form['bagOfWords']
		fdist = FreqDist(bagOfWords)
		print fdist.most_common(100)

	return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
