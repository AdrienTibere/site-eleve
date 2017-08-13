# -*-coding:utf-8 -*
from json import dumps, loads
from requests import put, get, post

data={
  'nb':1,
  'name':u'Équations',
  'class_id':1,
  'color':'#F44336'
}

post('http://localhost:5000/api/chapter', data=dumps(data)).json()
print get('http://localhost:5000/api/chapter/34').json()
