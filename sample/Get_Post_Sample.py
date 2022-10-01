
from flask import Flask, render_template, request


###일체형

@app.route("/user",methods=['GET', 'POST'])
def post():
	if(request.method =='GET'):
		return render_template('input.html')

	elif(request.method == 'POST'):
		value = request.form['input']
		return render_template('default.html', name=value)


###분리형


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
