from flask import Flask, jsonify
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
engine = create_engine("postgres://postgres:123abc@localhost:5432/etl_db")
Base = automap_base()
Base.prepare(engine, reflect=True)
#Base.classes.keys()
currency = Base.classes.currency
birth_rates = Base.classes.birth_rates
food_production = Base.classes.food_production
currencies = Base.classes.currencies
session = Session(engine)
app = Flask(__name__)

@app.route("/")
def home():
	message = (f"Possible routes:<br>"
			f"/api/v1.0/COUNTRY/YEAR<br>"
			f"<br>See /api/v1.0/countries for possible countries<br>"
			f"<br>The results will be formatted as follows:"
			f"Country"
			f"Year"
			f"Birth Rate"
			f"Food Production"
			f"Currency"
			f"Currency Exchange Rate")
	return message

@app.route("/api/v1.0/countries")
def countries():
	return jsonify(session.query(currencies.country).all())

@app.route("/api/v1.0/<country>/<year>")
def single_year(country, year):
	country_list = session.query(currencies.country)
	country_df = pd.read_sql(country_list.statement, session.bind)
	country_dict = country_df.to_dict()
	for count in country_dict["country"].values():
		if count == country:
			print(country)
			year_list = session.query(birth_rates.year).filter(birth_rates.country == country)
			year_df = pd.read_sql(year_list.statement, session.bind)
			year_dict = year_df.to_dict()
			for date in year_dict["year"].values():
				print(date)
				if date == int(year):
					#return jsonify(session.query(currencies.country, birth_rates.year).all())
					return jsonify(session.query(currencies.country, birth_rates.year, birth_rates.birthrate, food_production.foodproduction, currencies.currency, currency.rate).\
        				filter(currency.date == int(year)).filter(birth_rates.year == int(year)).filter(food_production.year == int(year)).\
        				filter(currency.currency == currencies.currency).filter(birth_rates.country == country).filter(food_production.country == country).filter(currencies.country == country).all())
			return jsonify({"error":"Date not found for that country"}),404
	return jsonify({"error":"Country not found"}),404


if __name__ == "__main__":
    app.run(debug=True)