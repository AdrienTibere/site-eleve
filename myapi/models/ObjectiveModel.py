from flask import jsonify
from app import db

class ObjectiveModel(db.Model):
  __tablename__ = "objective"
  id = db.Column(db.Integer, primary_key=True)
  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
  nb = db.Column(db.Integer)
  name = db.Column(db.String(125))

  def __init__(self, args):
    self.nb = args['nb']
    self.name = args['name']
    self.chapter_id = args['chapter_id']

  def __repr__(self):
    return '<Objective %s>' % self.name

  def to_json(self):
    return {
      'id': self.id,
      'chapter_id': self.chapter_id,
      'nb': self.nb,
      'name': self.name
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return jsonify( {'objective': self} ), 201

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return jsonify({'result':True})

db.create_all()
