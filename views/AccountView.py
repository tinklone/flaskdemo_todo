# coding:utf-8
from flask import render_template, request,redirect
from flask_classy import FlaskView
from service.post import PostService
from service.category import CategoryService


class AccountView(FlaskView):
    def index(self):
        return render_template('login.html')

    def auth(self):
        auth_url = "https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=101433876&redirect_uri=http://www.51tongyue.com"
        return redirect(auth_url)

    def add(self):
        category = CategoryService()
        category_list = category.get_list()
        return render_template('todo_add.html', category_list=category_list)

    def list(self):
        postservice = PostService()
        post_list = postservice.get_list()
        return render_template('list.html', post_list=post_list, page=len(post_list) / 5 + 1)

    def post(self):
        todo_content = request.form.get("content")
        category_name = request.form.get("category")
        todo = PostService()
        todo.save(todo_content, category_name)
        return ("添加成功")
