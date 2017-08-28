from app import app
from models.ChapterModel import ChapterModel
from models.ObjectiveModel import ObjectiveModel
from models.ExerciceModel import ExerciceModel
from flask import jsonify, request
from models.user import MyRegisterForm, User, UserAuth, user_manager, login_manager
import models
from flask_login import login_user

@login_manager.user_loader
@app.route('/api/login', methods=['GET', 'POST'])
def login():
  form = request.form
  username = form.get('username')
  password = form.get('password')
  userAuth = UserAuth.query.filter_by(username=username).first()
  if userAuth and user_manager.verify_password(password,userAuth):
    login_user(userAuth, force=True)
    user = userAuth.user.to_json()
    user['username'] = username
    return jsonify({'result': True, 'user': user}), 201
  else:
    return jsonify({'result': False, 'error': "Le nom d'utilisateur ou le mot de passe est incorrect."}), 400

@app.route('/api/register', methods=['GET', 'POST'])
def register():
  form = request.form
  if request.method == 'POST':
    user = models.user.User(email=form.get('email'),
                first_name=form.get('first_name'),
                last_name=form.get('last_name'),
                classe=form.get('classe'))
    user.create()
    userAuth = UserAuth(username=form.get('username'),
                        password=user_manager.hash_password(form.get('password')),
                        user=user)
    userAuth.create()
    return jsonify({'result': True, 'user': user}), 201
  return jsonify({'result': False}), 400

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

