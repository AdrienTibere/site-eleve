from models.ChapterModel import ChapterModel
from flask_restful import fields, marshal_with, reqparse, Resource
from flask import jsonify, request

post_parser = reqparse.RequestParser()
post_parser.add_argument('nb', type=int)
post_parser.add_argument('name', type=unicode)
post_parser.add_argument('color', type=str)
post_parser.add_argument('class_id', type=int)
post_parser.add_argument('available', type=bool)

chapter_fields = {
  'id': fields.Integer,
  'nb': fields.Integer,
  'name': fields.String,
  'class_id': fields.Integer,
  'color': fields.String,
  'available': fields.Boolean
}

class Chapter(Resource):
  @marshal_with(chapter_fields)
  def post(self):
    json_data = request.get_json(force=True)
    chapter = ChapterModel(json_data)
    chapter.create()
    print("chapter %r created, name: %r" %(chapter.id,chapter.name))
    return {'result': True}

  @marshal_with(chapter_fields)
  def get(self, id):
    chapter = ChapterModel.query.get(id)
    return chapter

  @marshal_with(chapter_fields)
  def delete(self, id):
    chapter = ChapterModel.query.get(id)
    if chapter:
      return chapter.delete()
    else:
      return {'result':False}

