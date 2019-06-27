from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='Role',lazy='dynamic')

    def __reqr__(self):
        return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__='Users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    email=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __reqr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('unreadable')
    
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

