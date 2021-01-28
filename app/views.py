from geomapping import query_database
from app import app
from flask import render_template

@app.route("/")
def index():
    res = query_database # output addresses
    return render_template("index.html", res=res)

@app.route("/get_map")
def get_map():
    return render_template("map.html")