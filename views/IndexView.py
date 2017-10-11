#coding:utf-8
from flask import Flask
from flask_classy import FlaskView, route
from flask import Flask, render_template,request
from service.user_service import UserService
from service.category import CategoryService
from random import choice
# we'll make a list to hold some quotes for our app


class IndexView(FlaskView):
    def index(self):
        return "index view"

