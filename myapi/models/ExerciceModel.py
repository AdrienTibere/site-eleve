from flask import jsonify
from app import db

class ExerciceModel(db.Model):
  __tablename__ = "exercice"
  id = db.Column(db.Integer, primary_key=True)
  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
  obj_id = db.Column(db.Integer, db.ForeignKey('objective.id'))
  name = db.Column(db.String(125))
  difficulty = db.Column(db.Integer)
  url = db.Column(db.String(125))

  def __init__(self, args):
    self.obj_id = args['obj_id']
    self.url = args['url']
    self.name = args['name']
    self.chapter_id = args['chapter_id']
    self.difficulty = args['difficulty']

  def __repr__(self):
    return '<Exercice %s>' % self.name

  def to_json(self):
    return {
      'id': self.id,
      'chapter_id': self.chapter_id,
      'name': self.name,
      'obj_id': self.obj_id,
      'difficulty': self.difficulty,
      'url': self.url
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return jsonify( {'exercice': self} ), 201

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return jsonify({'result':True})

db.create_all()
