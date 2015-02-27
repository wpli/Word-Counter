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

Then install the dependencies from above, and then follow the instructions 
for configuring Apache to run a Flask app via WSGI:
  http://flask.pocoo.org/docs/deploying/mod_wsgi/
