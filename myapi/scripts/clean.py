import sys
import os
 
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(os.path.dirname(DOSSIER_COURRANT))
sys.path.append(DOSSIER_PARENT)

from myapi.app import db
from myapi.models.ChapterModel import ChapterModel
from sqlalchemy import create_engine
from myapi.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker

some_engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=some_engine)
session = Session()

all_chapter = session.query(ChapterModel)
for chapter in all_chapter:
  print chapter.name
  session.delete(chapter)
session.commit()
