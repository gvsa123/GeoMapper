from address_mapper import run_mapper
from app import app
from flask import render_template
from geomapping import query_database
from random import randint

@app.route("/")
def index():
    sample = run_mapper()
    # sample = ADDR #[randint(0,1) for x in range(10)]
    # res = query_database # output addresses
    return render_template("index.html", data=sample)

@app.route("/get_map")
def get_map():
    return render_template("map.html")