from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField 
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name=StringField("请输入姓名：",validators=[Required()])
    submit=SubmitField('submit')