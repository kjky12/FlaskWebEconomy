# coding = utf-8

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "!!1994-11-13 BORA!!"

@app.route("/hello/")
def hello_flask():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run()

