from address_mapper import run_mapper
from app import app
from flask import render_template
import pandas as pd

@app.route("/")
def index():
    ip_dataframe = run_mapper()
    df_date = [i for i in ip_dataframe['failed_login_date']]
    df_ip = [i for i in ip_dataframe['login_attempt_ip']]
    df_addr = [i['countryName'] for i in ip_dataframe['located_address']]
    x = len(df_date)
    return render_template("index.html", DF_DATE=df_date, DF_IP=df_ip, DF_ADDR=df_addr, x=x)

@app.route("/get_map")
def get_map():
    return render_template("map.html")