import os, sys, time, json, logging, csv
import nltk
import string
from nltk import FreqDist
from nltk.corpus import stopwords
from operator import itemgetter

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# setup logging
base_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(base_dir,'wordcounter.log'),level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
	word_counts = None
	bigram_counts = None
	trigram_counts = None

    #this means the form was submitted
	if request.method == 'POST':	
		bag_of_words = request.form['bagOfWords']
		if "removeStopWords" in request.form:
			remove_stop_words = request.form['removeStopWords']
		else:
			remove_stop_words = False

		if "ignoreCase" in request.form:
			ignore_case = request.form['ignoreCase']
		else:
			ignore_case = False

		words = createWords(bag_of_words, False, ignore_case)

		words_perhaps_with_stop_words = createWords(bag_of_words, remove_stop_words, ignore_case)

		word_counts = sortCountList(countWords(words_perhaps_with_stop_words))

		bigram_counts = sortCountList(countBigrams(words))
		print bigram_counts

		trigram_counts = sortCountList(countTrigrams(words))
		print trigram_counts

		print word_counts

	return render_template("home.html", word_counts=word_counts, bigram_counts=bigram_counts, trigram_counts=trigram_counts)

def createWords(text, remove_stop_words, ignore_case):
	words = nltk.tokenize.word_tokenize(text)
	
	if ignore_case:
		words = [w.lower() for w in words]
	if remove_stop_words:
		words = [w for w in words if not w in stopwords.words('english') and not w in string.punctuation]
	else:
		words = [w for w in words if not w in string.punctuation]
	return words

def countWords(words):
	
	fdist = FreqDist(words)
	return fdist

def countBigrams(words):
	bigrams = nltk.bigrams(words)
	return nltk.FreqDist(bigrams)

def countTrigrams(words):
	trigrams = nltk.trigrams(words)
	return nltk.FreqDist(trigrams)

def sortCountList(freqDist):
	items = freqDist.items()
	return sorted(items, key=itemgetter(1), reverse=True)

if __name__ == "__main__":
    app.debug = True
    app.run()
