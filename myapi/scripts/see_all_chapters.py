# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post

""""
import sys
import os
 
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(os.path.dirname(DOSSIER_COURRANT))
sys.path.append(DOSSIER_PARENT)

import myapi.app
from myapi.models.ChapterModel import ChapterModel
from myapi.models.ObjectiveModel import ObjectiveModel
from sqlalchemy import create_engine
from myapi.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker

some_engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=some_engine)
session = Session()

all_chapter = session.query(ChapterModel)
for chapter in all_chapter:
  chapter = get('http://localhost:5000/api/chapter/' + str(chapter.id)).json()
  print chapter['name']
all_obj = session.query(ObjectiveModel)
for obj in all_obj:
  obj = get('http://localhost:5000/api/objective/' + str(obj.id)).json()
  print obj
"""

chapters = get('http://localhost:5000/api/chapter/get_all').json()['result']
for chapter in chapters:
	print "Chapter " + str(chapter['id']) + " : " + chapter['name']
objs = get('http://localhost:5000/api/objective/get_all').json()['result']
for obj in objs:
	print "Objectif " + str(obj['id']) + " : " + obj['name']
print get('http://localhost:5000/api/objective/3').json()
