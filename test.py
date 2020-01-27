from flask import Flask, jsonify
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
engine=create_engine("postgres://postgres:123abc@localhost:5432/etl_db")
Base=automap_base()
Base.prepare(engine,reflect=True)
currency = Base.classes.currency
birth_rates = Base.classes.birth_rates
food_production = Base.classes.food_production
currencies = Base.classes.currencies
session = Session(engine)
app = Flask(__name__)

@app.route("/")
def home():
    return(
        f"Possible routes are:<br>"
        f"/api/allresults <br>"
        f"<br>"
        f"/api/COUNTRY/YEAR<br>"
        f"<br>"
        f"results format in:<br>"
        f"Country/Year/Birth Rate/Food Production Index/Currency/Exchange Rate<br>"
        f"<br>"
        f"All the countries available for this research:<br>"
        f"/api/countries<br>"
        f"<br>"
        f"Years available for search between 1990-2016"
        f"<br>"
    )

@app.route("/api/countries")
def country_list():
    country_list=session.query(currencies.country).all()
    return jsonify(country_list)

@app.route("/api/allresults")
def result_all():
    result=session.query(currencies.country, birth_rates.year, birth_rates.birthrate, food_production.foodproduction, currencies.currency, currency.rate).\
        filter(currencies.currency==currency.currency).filter(currencies.country_code==birth_rates.countrycode).\
            filter(currencies.country==food_production.country).all()
    result_li=list(result)
    return jsonify(result_li)

@app.route("/api/<country>/<year>")
def route(country,year):
    result=session.query(currencies.country, birth_rates.year, birth_rates.birthrate, food_production.foodproduction, currencies.currency, currency.rate).\
        filter(currencies.currency==currency.currency).filter(currencies.country_code==birth_rates.countrycode).filter(currencies.country==food_production.country).\
            filter(currency.date ==year).filter(birth_rates.year ==year).filter(food_production.year ==year).filter(currency.currency == currencies.currency).\
                filter(birth_rates.country == country).filter(food_production.country == country).filter(currencies.country == country).all()
    result_li=list(result)
    return jsonify(result_li)


if __name__ == "__main__":
    app.run(debug=True)
