import json
from package import DataMethods

data_items = DataMethods.get_data("./Records/data_items")
stock_data = DataMethods.get_data("./Records/stock")

for item in data_items['Parts']:
	stock_data[item] = []

DataMethods.put_data(stock_data, "./Records/stock")