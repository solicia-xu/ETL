create table currencies(
	id serial primary key,
	Currency varchar unique,
	Country varchar unique,
	Country_Code varchar unique);
select * from currencies

create table birth_rates(
	id serial primary key,
	Countrycode varchar references currencies(country_code),
	Country varchar,
	Year int,
	BirthRate float);
select * from birth_rates

create table currency(
	id serial primary key,
	Currency varchar references currencies(currency),
	Date int,
	Rate float);
select * from currency

create table food_production(
	id serial primary key,
	Country varchar references currencies(country),
	Countrycode varchar,
	Year int,
	FoodProduction float);
select * from birth_rates

-- select currencies.country, birth_rates.year, birth_rates.birthrate, food_production.foodproduction, currencies.currency, currency.rate
-- from currencies,birth_rates,food_production,currency
-- where currencies.country='Brazil'
-- and birth_rates.year=2001
-- and currencies.currency=currency.currency
-- and currencies.country_code=birth_rates.countrycode
-- and currencies.country=food_production.country