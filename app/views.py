from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_map")
def get_map():
    return render_template("map.html")