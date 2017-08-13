from app import app
from models.ChapterModel import ChapterModel
from models.ObjectiveModel import ObjectiveModel
from models.ExerciceModel import ExerciceModel
from flask import jsonify

@app.route('/api/chapter/delete_all', methods=['DELETE'])
def chapter_delete_all():
  chapters = ChapterModel.query.all()
  for chapter in chapters:
    chapter.delete()
  return jsonify({'result': True}), 201

@app.route('/api/objective/delete_all', methods=['DELETE'])
def objective_delete_all():
  objectives = ObjectiveModel.query.all()
  for obj in objectives:
    obj.delete()
  return jsonify({'result': True}), 201

@app.route('/api/exercice/delete_all', methods=['DELETE'])
def exercice_delete_all():
  exercices = ExerciceModel.query.all()
  for exo in exercices:
    exo.delete()
  return jsonify({'result': True}), 201

@app.route('/api/chapter/get_all', methods=['GET'])
def chapter_get_all():
  chapters = ChapterModel.query.all()
  return jsonify({'result': chapters}), 201

@app.route('/api/objective/get_all', methods=['GET'])
def objective_get_all():
  objs = ObjectiveModel.query.all()
  return jsonify({'result': objs}), 201

@app.route('/api/chapter/<int:chapter_id>/objectives', methods=['GET'])
def chapter_get_objectives(chapter_id):
  chapter = ChapterModel.query.get(chapter_id)
  objectives = ObjectiveModel.query.filter_by(chapter_id=chapter.id).all()
  return jsonify({'result': objectives}), 201

@app.route('/api/objective/<int:obj_id>/get_exercices',methods=['GET'])
def objective_get_exercices(obj_id):
  obj = ObjectiveModel.query.get(obj_id)
  exercices = ExerciceModel.query.filter_by(obj_id=obj.id).all()
  return jsonify({'result': exercices}), 201

