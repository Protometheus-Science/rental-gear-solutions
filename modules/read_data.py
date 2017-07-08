# Read a csv file into a 2d array
def csv(path):
	return [line.strip().split(",") for line in open(path)]

# Pull column from csv_data
def columns(csv):
	# rotate matrix 90 cc: zip(*original)[::-1]
	return dict([(line[0], set(line[1:])) for line in zip(*csv)[::-1]])

# Return data in jinja-usable format
def parse(csv):
	data = map(dict, [[("count", csv.count(item))] + zip(csv[0], item) for item in csv[1:]])
	return data