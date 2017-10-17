# coding:utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import os
sql_uri = "mysql+pymysql://root:maxlong!@#123@127.0.0.1:3306/todo"
if os.name == 'nt':
    sql_uri = "mysql+pymysql://root:@127.0.0.1:3306/todo"
app.config['SQLALCHEMY_DATABASE_URI'] = sql_uri
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS',True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


if __name__ == '__main__':
    manager.run()