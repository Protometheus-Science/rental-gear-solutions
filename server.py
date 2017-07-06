from flask import Flask, render_template, request, url_for, redirect
from flask_compress import Compress
from modules import authenticate
import ssl

# Generate app
app = Flask("server")
Compress(app)

# Load SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('./ssl/server.crt', './ssl/server.key')

# Define routes
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login", methods=['GET', 'POST'])
def login():
	# if it is a user visiting...
	if request.method == 'GET':
		return render_template('login.html', name=request.args.get('name', ''))
	
	# Else check the password
	if authenticate.password(request.form['password']):
		return render_template('login.html', error="you were logged in succesfully")
	
	# Let them know they failed if the password was wrong
	return render_template('login.html', error="your password was incorrect", name=request.args.get('name', ''))


# Start App
app.run(host='127.0.0.1', port=5000, 
    debug = True, ssl_context=context)