from models.ObjectiveModel import ObjectiveModel
from flask_restful import fields, marshal_with, reqparse, Resource
from flask import jsonify, request

post_parser = reqparse.RequestParser()
post_parser.add_argument('nb', type=int)
post_parser.add_argument('chapter_id', type=int)
post_parser.add_argument('name', type=unicode)
post_parser.add_argument('color', type=str)

objective_fields = {
  'id': fields.Integer,
  'chapter_id': fields.Integer,
  'nb': fields.Integer,
  'name': fields.String
}

class Objective(Resource):
  @marshal_with(objective_fields)
  def post(self):
    json_data = request.get_json(force=True)
    objective = ObjectiveModel(json_data)
    objective.create()
    print("objective %r created, name: %r" %(objective.id,objective.name))
    return {'result': True}

  @marshal_with(objective_fields)
  def get(self, id):
    objective = ObjectiveModel.query.get(id)
    return objective

  @marshal_with(objective_fields)
  def delete(self, id):
    obj = ObjectiveModel.query.get(id)
    if obj:
      return obj.delete()
    else:
      return {'result':False}

