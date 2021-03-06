from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask_mail import Mail
from flask_cors import CORS

class AlchemyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj.__class__, DeclarativeMeta):
      # an SQLAlchemy class
      fields = {}
      for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
        data = obj.__getattribute__(field)
        try:
          json.dumps(data) # this will fail on non-encodable values, like other classes
          fields[field] = data
        except TypeError:
          fields[field] = None
      # a json-encodable dict
      return fields
    return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
CORS(app)
app.json_encoder = AlchemyEncoder
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
mail = Mail(app)

