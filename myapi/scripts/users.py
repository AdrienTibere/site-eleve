# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post

users = get('http://localhost:5000/api/user/get_all').json()
users = users.get('result')
print "Number of users: " + str(len(users))
for user in users:
  print "User " + str(user.get('id')) + ": " + user.get('first_name') + " " + user.get('last_name')
