from model.models import db
from model.models import User
class UserService():
    def __init__(self):
        pass
    def save(self,name,email):
        user = User(name,email)
        db.session.add(user)
        db.session.commit()
    def get_list(self):
        users = User.query.all()
        return users