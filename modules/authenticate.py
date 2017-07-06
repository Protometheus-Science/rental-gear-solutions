import hashlib

def authenticate_password(password):
	filepass = open("./user/login.key", "r").read()
	hashpass = hashlib.md5(password).hexdigest()
	return filepass == hashpass

if __name__ == '__main__':
	print authenticate_password("12345")
	print authenticate_password("1234")