from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='Role',lazy='dynamic')

    def __reqr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__='Users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    password_hash=db.Column(db.String(128))
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

