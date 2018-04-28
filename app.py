#!/usr/bin/env python3
#Bitcoin API
#Version 0.1 Alpha
from flask import Flask, render_template, request, redirect
import requests
import time

app = Flask(__name__)

#Default Route
@app.route('/')
def index():
	return render_template('index.html')

#Error handlers

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

if __name__ == "__main__":
	app.run(debug=True)
