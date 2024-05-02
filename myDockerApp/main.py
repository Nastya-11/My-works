from flask import Flask
server = Flask("name")

@server.route("/")
def hello():
    return "Hello world"

if name == "main":
    server.run(host='0.0.0.0')