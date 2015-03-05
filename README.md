Word-Counter
============

A web app to do simple word frequency counting, bigrams and trigrams. 
Created for use in data visualization and storytelling classrooms.

Installation
------------

Make sure you havy Python 2.7 (and the pip package manager). Then install the dependencies:

```
pip install nltk
pip install flask
pip install flask-uploads
```

Then install the NLTK libraries you need:
```
sudo python -m nltk.downloader punkt
sudo python -m nltk.downloader stopwords
```

Testing
-------

Run this command and then visit `localhost:5000` with a web browser

```
python server.py
```

Deploying
---------

We tend to deploy on Ubuntu machines with Apache and WSGI.

First, prep your machine (if you haven't already):
```
sudo aptitude install python
sudo aptitude install libapache2-mod-wsgi
sudo easy_install pip
```

Then checkout the repo, set up a virtual environment, and get the NLTK libraries you need:
```
cd /var/www/
git clone https://github.com/c4fcm/Word-Counter
cd Word-Counter
virtualenv venv
source venv/bin/activate
pip install nltk
pip install flask
pip install flask-uploads
sudo python -m nltk.downloader -d /usr/share/nltk_data punkt
sudo python -m nltk.downloader -d /usr/share/nltk_data stopwords
```

To configure Apache follow the instructions on how to run a Flask app via WSGI:
  http://flask.pocoo.org/docs/deploying/mod_wsgi/
