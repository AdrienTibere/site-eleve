from app import app,db
from flask import jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models.user import User
from models.ObjectiveModel import ObjectiveModel
from datetime import datetime

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', uselist=False, foreign_keys=user_id)
    objective_id = db.Column(db.Integer(), db.ForeignKey('objective.id', ondelete='CASCADE'))
    objective = db.relationship('ObjectiveModel', foreign_keys=objective_id)
    score = db.Column(db.Integer(), default=0)
    last_updated = db.Column(db.DateTime(), default=datetime.utcnow)
    db.UniqueConstraint('user_id', 'objective_id', name='uix_1')

    def __init__(self, args):
      self.user_id = args['user'].id
      self.user = args['user']
      self.objective_id = args['objective'].id
      self.objective = args['objective']
      if 'score' in args.keys():
        self.score = args['score']

    def __repr__(self):
      return '<Score %d for %r and %r>' % (self.score, self.user, self.objective)

    def to_json(self):
      return {
        'id': self.id,
        'user': self.user.to_json(),
        'objective': self.objective.to_json(),
        'score': self.score,
        'last_updated': self.last_updated
      }

    def update(self, score):
      self.score = self.score + score
      db.session.commit()
      return jsonify({'result': True})

    def create(self):
      db.session.add(self)
      db.session.commit()
      return jsonify( {'score': self} ), 201


# Create all database tables
db.create_all()


'''
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

manager.run()
'''
