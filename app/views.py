from address_mapper import run_mapper
from app import app
from flask import render_template
import pandas as pd

@app.route("/")
def index():
    ip_dataframe = run_mapper()
    date = ip_dataframe['failed_login_date']
    id = ip_dataframe['login_attempt_ip']
    return render_template("index.html", DATE=date, ID=id)
# def get_df():
#     # ADDR, ip_dataframe = run_mapper()
#     hello = "hello world"
#     return render_template("index.html", addr=hello)

@app.route("/get_map")
def get_map():
    return render_template("map.html")