# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
import re
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email=StringField("邮箱",validators=[Required(),Length(5,64),Email()])
    pwd=PasswordField("密码",validators=[Required()])
    remenber_me=BooleanField("记住我")
    submit=SubmitField("登录")

class RegistrationForm(FlaskForm):
    email=StringField("邮箱",validators=[Required(),Length(5,64),Email()])
    username=StringField("用户名",validators=[Required(),Length(5,64),
    Regexp('^[A-Za-z][A-Za-z0-9_]*$',re.I,'用户名为字母,数字,下划线组成且必须以字母打头')])
    pwd=PasswordField("密码",validators=[Required(),EqualTo('pwd2',message='2次密码必须一致')])
    pwd2=PasswordField("确认密码",validators=[Required()])
    
    submit=SubmitField("提交")

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')
        
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')