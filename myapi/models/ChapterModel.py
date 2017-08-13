from flask import jsonify
from app import app,db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

class ChapterModel(db.Model):
  __tablename__ = "chapter"
  id = db.Column(db.Integer, primary_key=True)
  nb = db.Column(db.Integer)
  name = db.Column(db.String(50))
  class_id = db.Column(db.Integer)
  color = db.Column(db.String(10))
  available = db.Column(db.Boolean, default=False)

  def __init__(self, args):
    self.nb = args['nb']
    self.name = args['name']
    self.class_id = args['class_id']
    self.color = args['color']
    if 'available' in args.keys():
      self.available = args['available']

  def __repr__(self):
    return '<Chapitre %s>' % self.name

  def to_json(self):
    return {
      'id': self.id,
      'nb': self.nb,
      'name': self.name,
      'class_id': self.class_id,
      'color': self.color,
      'available': self.available
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return jsonify( {'chapter': self} ), 201

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return jsonify({'result':True}), 201

db.create_all()

'''
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

manager.run()

#apres, faire python api.py db init/migrate/update (dans l'ordre)
'''
