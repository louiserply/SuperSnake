#!/usr/bin/env python
from flask import Flask


app = Flask(__name__)

print "Hi"
@app.route('/')
def index():
    return '<h1>Hello From Vagrant</h1>'


if __name__ == '__main_':
    app.run(host='0.0.0.0', port=5000)