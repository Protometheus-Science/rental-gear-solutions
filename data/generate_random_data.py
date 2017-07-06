from random import randint

stores = ["aspen", "basalt", "carbondale"]
models = ["giant", "specialized", "santa cruz"]
sizes  = ["s", "m", "l"]

print "\n".join(map(lambda x: ",".join(x), [["bike", stores[randint(0,2)], models[randint(0,2)], sizes[randint(0,2)]] for i in range(100)]))