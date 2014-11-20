#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response



app= Flask(__name__)

@app.route('/')

def index():
    response = make_response("<h1> Hello, World</h1>")
    return response

#app.add_url_rule('/')   the same as @app.route('/')

@app.route('/<kigali>')

def rda(kigali):
    response = make_response('<h1>i am in capital of Rwanda</h1>')
    return response

@app.route('/greet/<name>')

def greet(name):
    response = make_response('"<h1>Mwaramutse, %s how is home?<h1>" % name')
    return response

@app.route('/counter/<int:num>')

def counter(num):
    dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    response = make_response('Number %s' % dict.get( num,'unknown'))
    return response


if __name__ == '__main__':
    app.run(port=6000,debug=True)
