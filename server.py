from flask import Flask, render_template, request, url_for
from flask_compress import Compress
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

@app.route("/login")
def login():
	return render_template('login.html', name=request.args.get('name', ''))

@app.route("/auth", methods=['POST', 'GET'])
def authenticate():
	error = "you the system took a wrong turn somewhere"
	if request.method == 'POST':
		error = "your password is " + request.form['password']

	return render_template('login.html', error=error, name=request.args.get('name', ''))

# Start App
app.run(host='127.0.0.1', port=5000, 
    debug = True, ssl_context=context)