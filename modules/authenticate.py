import hashlib

def password(test):
	filepass = open("./user/login.key", "r").read()
	hashpass = hashlib.md5(test).hexdigest()
	return filepass == hashpass

if __name__ == '__main__':
	print password("12345")
	print password("1234")