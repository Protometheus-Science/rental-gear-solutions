def csv(path):
	return [line.split(",") for line in open("data/stock_1.csv")]