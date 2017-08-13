# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post

print get('http://localhost:5000/api/exercice/1').json()
