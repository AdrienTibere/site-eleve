from models.ExerciceModel import ExerciceModel
from flask_restful import fields, marshal_with, reqparse, Resource
from flask import jsonify, request

fields = {
  'id': fields.Integer,
  'chapter_id': fields.Integer,
  'name': fields.String,
  'obj_id': fields.Integer,
  'difficulty': fields.Integer,
  'url': fields.String
}

class Exercice(Resource):
  @marshal_with(fields)
  def post(self):
    json_data = request.get_json(force=True)
    exo = ExerciceModel(json_data)
    exo.create()
    print("exercice %r created, name: %r" %(exo.id,exo.name))
    return {'result': True}

  @marshal_with(fields)
  def get(self, id):
    exo = ExerciceModel.query.get(id)
    return exo

  @marshal_with(fields)
  def delete(self, id):
    exo = ExerciceModel.query.get(id)
    if exo:
      return exo.delete()
    else:
      return {'result':False}

