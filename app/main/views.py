from datetime import datetime
from flask import render_template, session, redirect, url_for
from .froms import NameForm
from . import main
from ..import db
from ..models import User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user',methods=['GET','POST'])
def userpage():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['isknow'] = False
        else:
            session['isknow'] = True
        session['uname'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.userpage'))
    return render_template('userpage.html', form=form, uname=session.get('uname'),
                    isknow=session.get('isknow', False), cur_time=datetime.utcnow())
