import os, sys, time, json, logging, csv
import nltk
import string
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
		words = nltk.tokenize.word_tokenize(bagOfWords)
		words = [w for w in words if not w in stopwords.words('english') and not w in string.punctuation]
		fdist = FreqDist(words)
		print fdist.most_common(100)

	return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
