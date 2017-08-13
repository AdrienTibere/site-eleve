# -*- coding:utf-8 -*

from app import app
from models.ChapterModel import ChapterModel
from models.ObjectiveModel import ObjectiveModel
from flask import jsonify
import random

######### template ##############
@app.route('/api/exercice/content/n')
def exercice_n():
  return jsonify({
    'statement':'''
    ''',
    'solution':'''
    '''
  }), 201
####### end template ############

@app.route('/api/exercice/content/1')
def exercice_1():
  numbers = sorted(random.sample(range(-8,8),2))
  first_bracet = random.choice([']','['])
  second_bracet = random.choice([']','['])
  first_nb = numbers[0]
  second_nb = numbers[1]

  return jsonify({
    'statement':'''
    <div>
    Représenter graphiquement l'intervalle ''' + first_bracet + str(first_nb) + ' ; ' + str(second_nb) + second_bracet + '''.
    </div>
    ''',
    'solution':'''
    <div style='text-align: center'>
    ---------------''' + first_bracet + '''<span style='color: #F44336'>-----------------</span>''' + second_bracet + '''----------------<br/>
    <span style='visibility:hidden;'>-------------</span> ''' + str(first_nb) + ''' <span style='visibility:hidden;'>---------------</span> ''' + str(second_nb) + ''' <span style='visibility:hidden;'>---------------</span><br/>
    (les pointillés doivent être remplacés par une ligne continue)
    </div>
    '''
  }), 201


@app.route('/api/exercice/content/2')
def exercice_2():
  numbers1 = sorted(random.sample(range(-9,9),4))
  bracet1 = random.choice([']','['])
  bracet2 = random.choice([']','['])
  bracet3 = random.choice([']','['])
  bracet4 = random.choice([']','['])
  link = random.choice(['∪','∩'])
  nb1 = numbers1[0]
  nb2 = numbers1[2]
  nb3 = numbers1[1]
  nb4 = numbers1[3]
  if link == '∪':
    sol = '''
    Pour représenter l'union de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties. La partie coloriée est l'union des deux intervalles, ici ''' + bracet1 + str(nb1) + ' ; ' + str(nb4)  + bracet4 + '''.<br/><br/>
    ---------------''' + bracet1 + '''<span style='color: #F44336'>---------------------------------------------------</span>''' + bracet4 + '-----------------' + '''<br/>
    <span style='visibility:hidden;'>------------</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>---------------</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>-------------</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>------------</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>---------------</span><br/>
    '''
  else:
    sol = '''
    Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + bracet3 + str(nb3) + ' ; ' + str(nb2)  + bracet2 + '''.<br/><br/>
    ---------------''' + bracet1 + '''-----------------''' + bracet3 + "<span style='color: #F44336'>-----------------</span>" + bracet2 + "-----------------" + bracet4 + '-----------------' + '''<br/>
    <span style='visibility:hidden;'>------------</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>---------------</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>-------------</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>------------</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>---------------</span><br/>
    '''


  return jsonify({
    'statement':'''
    <div>
    Représenter graphiquement l'intervalle ''' + bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4 + '''.
    </div>
    ''',
    'solution':'''
    <div style='text-align: center'>''' + sol + '''
    (les pointillés doivent être remplacés par une ligne continue)
    </div>
    '''
  }), 201
