from flask import Flask, redirect, render_template, request, session
import os

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if not session.get('isLogin'):
        return render_template('Login.html')
    else:
        return render_template('contact.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        form=request.form
        return render_template('result.html',form=form)
    

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        if request.form['username']=='admin' and request.form['password']=='admin':
            session['isLogin']=True
        return index()

@app.route('/logout',methods=['POST','GET'])
def logout():
    session['isLogin']=False
    return index()

if __name__=='__main__':
    app.secret_key=os.urandom(21)
    app.run(debug=True)
