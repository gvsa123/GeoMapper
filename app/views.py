from address_mapper import run_mapper
from app import app
from flask import render_template, request
import pandas as pd

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_app", methods=['POST', 'GET'])
def run_app():
    QD = request.form['qd']
    ip_dataframe = run_mapper(qd=QD)

    if type(ip_dataframe) is tuple:
        return render_template("index.html")

    df_date = [i for i in ip_dataframe['failed_login_date']]
    df_ip = [i for i in ip_dataframe['login_attempt_ip']]
    x = len(df_ip)
    df_addr = []

    try:
        for i in ip_dataframe['located_address']:
            try:
                df_addr.append(i['countryName'])
                # df_addr = [i['countryName'] for i in ip_dataframe['located_address']]
            except TypeError as te:
                print(f"TypeError: {te}. Appending <null>.")
                df_addr.append("<null>")
                pass
    except KeyError as ke:
        print(ke)
    return render_template("run-mapper.html", DF_DATE=df_date, DF_IP=df_ip, DF_ADDR=df_addr, x=x)

@app.route("/get_map")
def get_map():
    return render_template("map.html")