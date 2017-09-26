from flask import render_template
from flask_classy import FlaskView
from service.category import CategoryService


class TodoView(FlaskView):
    def index(self):
        return ""

    def get(self, id):
        return ""

    def add(self):
        category = CategoryService()
        category_list = category.get_list()
        return render_template('todo_add.html', category_list=category_list)