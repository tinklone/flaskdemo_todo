#coding:utf-8
from flask import Flask
from flask_classy import FlaskView, route
from flask import Flask, render_template,request
from service.user_service import UserService
from service.category import CategoryService
from random import choice
# we'll make a list to hold some quotes for our app


class Test2View(FlaskView):
    def index(self):
        return "test view"
    def get(self, id):
        return "id is %s"%id
    def adduser(self):
        us = UserService()
        us.save("test3","test3@test.com")
        return "success"
    def template(self):
        us = UserService()
        user_list = us.get_list()
        return render_template('index.html',user_list=user_list,page=len(user_list)/5+1)

    def addcategory(self):
        return render_template('category.html')


    def post(self):
        category_name = request.form.get("name")
        category = CategoryService()
        category.save(category_name)
        return ("添加成功")

