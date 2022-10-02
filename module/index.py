# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import Flask, render_template, request



# Define route "/" & "/<name>"
@app.route("/")
#@app.route("/<name>")
def index(name='Anonymous'):
    #return f"Hello {name}!!"
    return render_template('simple111.html', as_attachment=True)

    #return render_template('index.html', as_attachment=True)
    #return render_template("templates\\index.html")



@app.route("/",methods=['GET'])
def getT(name='Anonymous'):
    #http://127.0.0.1:9000/post?input=1 를 보내면 아래처럼 받아오면됨.
    temp = request.args.get('input')

    msg = "{0}님 환영합니다.".format(temp)
    return msg


@app.route("/post",methods=['POST'])
def post(name='Anonymous'):
    value = request.form['input']
    msg = "POST %s 님 환영합니다." % value
    return msg





@app.route("/hello/")
def hello_flask():
    return "Hello Flask!"
