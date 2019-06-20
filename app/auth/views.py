# coding:utf-8

from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User



@auth.route('/secret')
@login_required
def secret():
    return '未登录'