#!/usr/bin/env python
from app import db

if __name__ == '__main__':
  print("ok")
  db.create_all()
