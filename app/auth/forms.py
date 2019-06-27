# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Required,Length,Email

class LoginForm(FlaskForm):
    email=StringField("邮箱",validators=[Required(),Length(5,64),Email()])
    pwd=PasswordField("密码",validators=[Required()])
    remenber_me=BooleanField("记住我")
    submit=SubmitField("登录")