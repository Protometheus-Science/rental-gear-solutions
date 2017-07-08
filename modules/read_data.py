# Read a csv file into a 2d array
def csv(path):
	return [line.strip().split(",") for line in open(path)]

# Pull column from csv_data
def columns(csv_data):
	return map(lambda x: x.title(), csv_data[0])

# Return data in jinja-usable format
def parse(csv):
	data = map(dict, [[("count", csv.count(item))] + zip(columns(csv), item) for item in csv[1:]])
	print data
	return data