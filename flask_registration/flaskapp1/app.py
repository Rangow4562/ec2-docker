
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)
app.secret_key = 'Cairocoders-Ednalan'

import rds_db as db

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        email = request.form['email']
        gender = request.form['optradio']
        address = request.form['address']
        date = request.form['date']
        sem = request.form['sem']
        rolno = request.form['rolno']
        phone = request.form['phone']
        course = request.form['course']
        db.insert_details(fname,lname,age,date,gender,rolno,email,address,phone,course,sem)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        flash('Information Added successfully')
        return render_template('index.html',var=var)



if __name__ == "__main__":
    
    app.run(debug=True)