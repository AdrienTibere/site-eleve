from app import app
from models.ChapterModel import ChapterModel
from models.ObjectiveModel import ObjectiveModel
from models.ExerciceModel import ExerciceModel
from models.score import Score
from models.user import MyRegisterForm, User, UserAuth, user_manager, login_manager
import models
from flask import jsonify, request
from flask_login import login_user, login_required, logout_user

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

@app.route('/api/logout', methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return jsonify({'result': True}),201

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


# Chapter routes
@app.route('/api/chapter/delete_all', methods=['DELETE'])
def chapter_delete_all():
  chapters = ChapterModel.query.all()
  for chapter in chapters:
    chapter.delete()
  return jsonify({'result': True}), 201

@app.route('/api/chapter/get_all', methods=['GET'])
def chapter_get_all():
  chapters = ChapterModel.query.all()
  return jsonify({'result': chapters}), 201

@app.route('/api/chapter/<int:chapter_id>/objectives', methods=['GET'])
def chapter_get_objectives(chapter_id):
  chapter = ChapterModel.query.get(chapter_id)
  objectives = ObjectiveModel.query.filter_by(chapter_id=chapter.id).all()
  return jsonify({'result': objectives}), 201


# Objective routes
@app.route('/api/objective/delete_all', methods=['DELETE'])
def objective_delete_all():
  objectives = ObjectiveModel.query.all()
  for obj in objectives:
    obj.delete()
  return jsonify({'result': True}), 201

@app.route('/api/objective/get_all', methods=['GET'])
def objective_get_all():
  objs = ObjectiveModel.query.all()
  return jsonify({'result': objs}), 201

@app.route('/api/objective/<int:obj_id>/get_exercices',methods=['GET'])
def objective_get_exercices(obj_id):
  obj = ObjectiveModel.query.get(obj_id)
  exercices = ExerciceModel.query.filter_by(obj_id=obj.id).all()
  return jsonify({'result': exercices}), 201


# Exercice routes
@app.route('/api/exercice/delete_all', methods=['DELETE'])
def exercice_delete_all():
  exercices = ExerciceModel.query.all()
  for exo in exercices:
    exo.delete()
  return jsonify({'result': True}), 201


# Score routes
@app.route('/api/score/update/<int:user_id>/<int:obj_id>/<int:score>', methods=['POST'])
def update_score(user_id, obj_id, score):
  obj = ObjectiveModel.query.get(obj_id)
  user = models.user.User.query.get(user_id)
  score_obj = Score.query.filter_by(user_id=user.id, objective_id=obj.id).first()
  if score_obj:
    score_obj.update(score)
  else:
    json = {
      "user": user,
      "objective": obj,
      "score": score
    }
    score_obj = Score(json)
    score_obj.create()
  return jsonify({'result': score_obj.to_json()}), 201

@app.route('/api/score/get/<int:user_id>/<int:obj_id>/', methods=['GET'])
def get_score(user_id, obj_id):
  obj = ObjectiveModel.query.get(obj_id)
  user = models.user.User.query.get(user_id)
  score_obj = Score.query.filter_by(user_id=user.id, obj_id=obj.id).first()
  if score_obj:
    return jsonify({'score': score_obj.score}), 201
  else:
    return jsonify({'score': 0}), 201


# Profile route
@login_required
@app.route('/api/profile/<int:user_id>', methods=['GET'])
def profile(user_id):
  chapter_id = 1
  user = models.user.User.query.get(user_id)
  chapter = ChapterModel.query.get(chapter_id)
  objectives = ObjectiveModel.query.filter_by(chapter_id=chapter_id)
  #res update the objectives to add scores
  res = []
  for objective in objectives:
    score = Score.query.filter_by(objective_id=objective.id, user_id=user.id).first()
    if not score:
      score = {
        'user': user.to_json(),
        'objective': objective.to_json(),
        'score': 0
      }
    res.append({'objective': objective, 'score': score})
  return jsonify({
    'current_chapter': chapter.to_json(),
    'objectives': res
  }), 201
