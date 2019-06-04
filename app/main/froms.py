# --coding:utf-8 -
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField 
from wtforms.validators import Required

class NameForm(FlaskForm):
    name=StringField("请输入姓名：",validators=[Required()])
    submit=SubmitField('submit')