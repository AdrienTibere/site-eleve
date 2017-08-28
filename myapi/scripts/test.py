# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post

user = get('http://localhost:5000/api/user/3').json()
