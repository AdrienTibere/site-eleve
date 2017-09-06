from flask_restful import Resource
from models.score import Score

class Score(Resource):
  def post(self):
    json_data = request.get_json(force=True)
    score = Score(json_data)
    score.create()
    print("score %r created" %score)
    return {'result': True}

  def get(self, id):
    score = Score.query.get(id)
    return score
