# ETL

•	The purpose of this ETL is to have a clean dataset for food production index, birth rate and the currency exchange rates that can be used for further analysis.

•	Extract the exchange rates for 52 different countries from the web, transform and process the data and load it to relational database to store, build the Flask so that users can search for food production index or exchange rates for different time period.

Datasets:
- Food Production Index (https://data.worldbank.org/indicator/AG.PRD.FOOD.XD)
- Monthly Average Exchange Rates (https://www.ofx.com/en-us/forex-news/historical-exchange-rates/monthly-average-rates/)
- Yearly Birth Rate Data (https://data.worldbank.org/indicator/SP.DYN.CBRT.IN)

Possible Investigations:
- Correlation between any of our three data sets
- See how food prices affect birth rates and vice versa

Final database will be relational, with keys corresponding to country, food type, and possibly date.
