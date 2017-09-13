# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post
import sys
from os import path
sys.path.append( path.dirname( path.dirname(path.abspath(__file__)) ) )
print path.dirname( path.dirname(path.abspath(__file__)) ) 
from config import SERVER_URL


users = get(SERVER_URL + 'user/get_all').json()
users = users.get('result')
print "Number of users: " + str(len(users))
for user in users:
  score = get(SERVER_URL + 'user/' + str(user.get('id')) + "/total_score").json()
  score = score.get('result')
  print "User " + str(user.get('id')) + ": " + user.get('first_name') + " " + user.get('last_name') + ". Total score of " + str(score)
