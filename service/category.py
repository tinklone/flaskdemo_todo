from model.models import db
from model.models import Category
class CategoryService():
    def __init__(self):
        pass
    def save(self,name):
        category = Category(name)
        db.session.add(category)
        db.session.commit()
    def get_list(self):
        category_list = Category.query.all()
        return category_list