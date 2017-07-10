from random import randint

store = ["aspen", "basalt", "carbondale"]
brand = ["giant", "specialized", "santa cruz"]
style = ["hybrid", "mountain", "road"]
size  = ["s", "m", "l"]

pick = lambda l: l[randint(0, len(l)-1)]

def new_bike():
	bike = ["bike", pick(store), pick(brand), pick(style)]
	bike += [bike[2] + "-" + bike[3] + "-" + str(randint(1, 2)), pick(size)]
	return bike

print "\n".join(map(lambda x: ",".join(x), [new_bike() for i in range(500)]))