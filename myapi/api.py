import sys
from flask_restful import Api
from resources.chapter import Chapter
from resources.objective import Objective
from resources.exercice import Exercice
from resources.user import User
from resources.score import Score
from app import app
import resources.routes
import resources.exercices_routes

api = Api(app)

api.add_resource(Chapter, '/api/chapter', '/api/chapter/<int:id>')
api.add_resource(Objective, '/api/objective', '/api/objective/<int:id>')
api.add_resource(Exercice, '/api/exercice', '/api/exercice/<int:id>')
api.add_resource(User, '/api/user', '/api/user/<int:id>')
api.add_resource(Score, '/api/score', '/api/score/<int:id>')

if __name__ == '__main__':
  reload(sys)
  sys.setdefaultencoding('utf-8')
  app.run(debug=True)
