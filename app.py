import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
import numpy

#http://alignedleft.com/tutorials/d3/drawing-divs
#https://github.com/dfm/flask-d3-hello-world/blob/master/templates/index.html
#http://www.datasciencecentral.com/profiles/blogs/beyond-the-visualization-zoo

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
	dataset = [1,2,3,4,5,6,7,8,9,85,99,66]
	return render_template("index.html", dataset=dataset, text="Some girls")

@app.route("/s", methods=("GET", "POST"))
def svg():
	return render_template('another.html')


if __name__ == '__main__':
	app.run()