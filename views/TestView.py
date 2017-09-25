from flask import Flask
from flask_classy import FlaskView
from random import choice
# we'll make a list to hold some quotes for our app


class TestView(FlaskView):
    def index(self):
        return "test view"

    def get(self, id):
        return "id is %s"%id