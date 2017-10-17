# coding:utf-8
from flask import Flask
from flask_classy import FlaskView, route
from flask import Flask, render_template, request
from service.user_service import UserService
from service.category import CategoryService
from random import choice
import requests
import urlparse
import json
# we'll make a list to hold some quotes for our app


class IndexView(FlaskView):
    def index(self):
        code = request.args.get("code")
        token_url = "https://graph.qq.com/oauth2.0/token"
        params_data = {'grant_type': 'authorization_code',
                       'client_id': '101433876', 'client_secret': 'da662d9b3be0ba04ff2b03b5c73cb83f', 'code': code, 'redirect_uri': 'http://www.51tongyue.com'}
        r = requests.get(token_url, params = params_data)
        dict_r = urlparse.parse_qs(r.content)
        print dict_r
        openid_url = 'https://graph.qq.com/oauth2.0/me?access_token=%s'%dict_r['access_token'][0]
        r = requests.get(openid_url)
        openid = json.loads(r.content[10:-3])['openid']
        get_user_info = 'https://graph.qq.com/user/get_user_info?access_token=%s&oauth_consumer_key=101433876&openid=%s'%(dict_r['access_token'][0],openid)
        r = requests.get(get_user_info)
        print r.content
        return "index view"
