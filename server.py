from flask import Flask
from flask_compress import Compress
import ssl


app = Flask("server")
Compress(app)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('./ssl/server.crt', './ssl/server.key')

@app.route("/")
def hello():
    return "Hello World!"

app.run(host='127.0.0.1',port=5000, 
    debug = True, ssl_context=context)