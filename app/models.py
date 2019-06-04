from . import db

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
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __reqr__(self):
        return '<User %r>' % self.username

