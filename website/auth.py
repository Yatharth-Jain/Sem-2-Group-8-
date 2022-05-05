from flask import Blueprint, redirect, render_template , request,flash, url_for

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/student-register',methods=['GET','POST'])
def studentreg():
    return render_template('student-register.html')