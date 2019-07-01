# coding:utf-8

from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db


@auth.route('/secret')
@login_required
def secret():
    return '未登录'

@auth.route('/login',methods=['GET','POST'])
def login():
    log_form=LoginForm()
    if log_form.validate_on_submit():
        user=User.query.filter_by(email=log_form.email.data).first()
        if user is not None and user.verify_password(log_form.pwd.data):
            print(user)
            login_user(user,log_form.remenber_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html',form=log_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logged out')
    return redirect(url_for("main.index"))

@auth.route('/registor',methods=['GET','POST'])
def registor():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email=form.email.data,username=form.username.data,password=form.pwd.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('auth/login'))
    return render_template('auth/registor.html',form=form)
