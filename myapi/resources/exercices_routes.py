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
    &#9472;&#9472;&#9472;&#9472;''' + '''<span style='color: #F44336'>''' + first_bracet + '&#9472;&#9472;&#9472;'*(second_nb-first_nb) + second_bracet + '''</span>''' + '''&#9472;&#9472;&#9472;&#9472;<br/>
    <span style='visibility:hidden;'>&#9472;&#9472;&#9472;---</span> ''' + str(first_nb) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(3*(second_nb-first_nb)-1) + '''</span> ''' + str(second_nb) + ''' <span style='visibility:hidden;'>&#9472;&#9472;&#9472;&#9472;-</span><br/>
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
  ecart1 = nb3 - nb1
  ecart2 = nb2 - nb3
  ecart3 = nb4 - nb2
  if nb1>=0:
    nb1 = '&nbsp;' + str(nb1)
  if nb2>=0:
    nb2 = '&nbsp;' + str(nb2)
  if nb3>=0:
    nb3 = '&nbsp;' + str(nb3)
  if nb4>=0:
    nb4 = '&nbsp;' + str(nb4)
  if link == '∪':
    sol = '''
    Pour représenter l'union de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties. La partie coloriée est l'union des deux intervalles, ici ''' + bracet1 + str(nb1) + ' ; ' + str(nb4)  + bracet4 + '''.<br/><br/>
    <div style='display: inline-block; text-align: left'>
    &#9472;&#9472;<span style='color: #F44336'>''' + bracet1 + '&#9472;&#9472;'*ecart1 + '&#9472;&#9472;'*ecart2 + '&#9472;&#9472;'*ecart3 + bracet4 + '</span>' + '&#9472;&#9472;' + '''<br/>
    <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-2) + '''-</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart2-2) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''-</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>------</span>
    </div><br/>
    '''
  else:
    sol = '''
    Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + bracet3 + str(nb3) + ' ; ' + str(nb2)  + bracet2 + '''.<br/><br/>
    <div style='display: inline-block; text-align: left'>
    &#9472;&#9472;''' + '&#9472;&#9472;'*ecart1 + "<span style='color: #F44336'>" + bracet3 + '&#9472;&#9472;'*ecart2 + bracet2 + "</span>" + '&#9472;&#9472;'*ecart3 + '&#9472;&#9472;' + '''<br/>
    <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-2) + '''-</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart2-2) + '''-</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''-</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;--</span>
    </div><br/>
    '''


  return jsonify({
    'statement':'''
    <div>
    Représenter graphiquement l'intervalle ''' + bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4 + '''.
    </div>
    ''',
    'solution':'''
    <div style='text-align: center'>''' + sol + '''
    /!\ L'échelle doit être respectée pour avoir une réponse exacte : par exemple, il doit y avoir ''' + str(ecart2) + ''' unités entre les deux crochets du milieu.
    </div>
    '''
  }), 201

@app.route('/api/exercice/content/3')
def exercice_3():
  bracet1 = random.choice([']','['])
  bracet2 = random.choice([']','['])
  bracet3 = random.choice([']','['])
  bracet4 = random.choice([']','['])
  link = random.choice(['∪','∩'])
  numbers1 = sorted(random.sample(range(-9,5),2))
  nb1 = numbers1[0]
  nb2 = numbers1[1]
  numbers2 = sorted(random.sample(range(nb2,9),2))
  nb3 = numbers2[0]
  nb4 = numbers2[1]
  ecart1 = nb2 - nb1
  ecart2 = nb3 - nb2
  ecart3 = nb4 - nb3
  if nb1>=0:
    nb1 = '&nbsp;' + str(nb1)
  if nb2>=0:
    nb2 = '&nbsp;' + str(nb2)
  if nb3>=0:
    nb3 = '&nbsp;' + str(nb3)
  if nb4>=0:
    nb4 = '&nbsp;' + str(nb4)
  disjoint = True
  #Cas ou les intervalles ne sont pas disjoints
  if ecart2 == 0:
    if link == '∪' and (bracet2 == ']' or bracet3 == '['):
      disjoint = False
    if link == '∩' and bracet2 == ']' and bracet3 == '[':
      disjoint = False
  #assigner res et display
  if disjoint:
    if link == '∪':
      res = bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4
      if ecart2 == 0:
        display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + '&#9472;&#9472;'*ecart1 + bracet2 + '</span>' + ' ' + "<span style='color: #F44336'>" + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + '</span>' + '&#9472;&#9472;' + '''<br/>
        <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-1) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-1) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
        '''
      else:
        display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + '&#9472;&#9472;'*ecart1 + bracet2 + '</span>' + '&#9472;&#9472;'*ecart2 + "<span style='color: #F44336'>" + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + '</span>' + '&#9472;&#9472;' + '''<br/>
        <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-2) + '-' + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart2-2) + '-' + '''</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '-' + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
        '''
    else:
      res = '∅'
      if ecart2 == 0:
        display = "&#9472;&#9472;" + bracet1 + '&#9472;&#9472;'*ecart1 + bracet2 + ' ' + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + '&#9472;&#9472;' + '''<br/>
        <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-1) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''-</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
        '''
      else:
        display = "&#9472;&#9472;" + bracet1 + '&#9472;&#9472;'*ecart1 + bracet2 + '&#9472;&#9472;'*ecart2 + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + '&#9472;&#9472;' + '''<br/>
        <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-2) + '''-</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart2-2) + '''-</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''-</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
        '''
  else:
    if link == '∪':
      res = bracet1 + str(nb1) + ' ; ' + str(nb4) + bracet4
      display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + '&#9472;&#9472;'*ecart1 + '&#9472;&#9472;'*ecart2 + '&#9472;&#9472;'*ecart3 + bracet4 + '</span>' + '&#9472;&#9472;' + '''<br/>
      <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart1-2) + '''-</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
      '''
    else:
      res = '{' + str(nb2) + ' }'
      display = "&#9472;&#9472;" + '&#9472;&#9472;'*ecart1 + "<span style='color: #F44336'>|</span>" + '&#9472;&#9472;'*ecart3 + '&#9472;&#9472;' + '''<br/>
      <span style='visibility:hidden;'>&#9472;</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-3) + '''</span> ''' + "<span style='color: #F44336'>" + str(nb3) + "</span>" + ''' <span style='visibility:hidden;'>''' + '&#9472;'*(2*ecart3-2) + '''-</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>&#9472;&#9472;</span>
      '''
  if link == '∪':
    sol = ''' 
    Pour représenter l'union de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties. La partie coloriée est l'union des deux intervalles, ici ''' + res + '''.<br/><br/>
    <div style='display: inline-block; text-align: left'>
    ''' + display + '''
    </div><br/>
    '''
  else:
    if disjoint:
      sol = '''
      Lorsque deux intervalles sont disjoints, ils n'ont aucun élément en commun. Leur intersection vaut donc ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left'>
      ''' + display + '''
      </div><br/>
      '''
    else:
      sol = '''
      Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left'>
      ''' + display + '''
      </div><br/>
      '''

  return jsonify({
    'statement':'''
    <div>
    Représenter graphiquement l'intervalle ''' + bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4 + '''.
    </div>
    ''',
    'solution':'''
    <div style='text-align: center'>''' + sol + '''
    /!\ L'échelle doit être respectée pour avoir une réponse exacte : par exemple, il doit y avoir ''' + str(ecart1) + ''' unités entre les deux premiers crochets.
    </div>
    '''
  }), 201


@app.route('/api/exercice/content/4')
def exercice_4():
  bracet1 = random.choice([']','['])
  bracet2 = random.choice([']','['])
  bracet3 = random.choice([']','['])
  bracet4 = random.choice([']','['])
  numbers1 = sorted(random.sample(range(-10,10),2))
  numbers2 = sorted(random.sample(range(-10,10),2))
  n1 = numbers1[0]
  n2 = numbers1[1]
  n3 = numbers2[0]
  n4 = numbers2[1]
  text = ""
  res = ""
  if n1 < n3:
    if n2 < n3:
      text = "Ici, on ne peut pas simplifier l'union, qui s'écrit donc : "
      res = bracet1 + str(n1) + ' ; ' + str(n2) + bracet2 + ' ∪ ' + bracet3 + str(n3) + ' ; ' + str(n4) + bracet4
    elif n2 == n3:
      if bracet2 == '[' and bracet3 == ']':
        text = "Ici, on ne peut pas simplifier l'union, qui s'écrit donc : "
        res = bracet1 + str(n1) + ' ; ' + str(n2) + bracet2 + ' ∪ ' + bracet3 + str(n3) + ' ; ' + str(n4) + bracet4
      else:
        text = "L'union des deux intervalles vaut : "
        res = bracet1 + str(n1) + ' ; ' + str(n4) + bracet4
    else:
      if n2 < n4:
        text = "L'union des deux intervalles vaut : "
        res = bracet1 + str(n1) + ' ; ' + str(n4) + bracet4
      else:
        if n2 == n4 and bracet4 == ']':
          text = "L'union des deux intervalles vaut : "
          res = bracet1 + str(n1) + ' ; ' + str(n2) + ']'
        else:
          text = "L'union des deux intervalles vaut : "
          res = bracet1 + str(n1) + ' ; ' + str(n2) + bracet2
  else:
    if n1 == n3 and bracet1 == '[':
      temp_bracet = '['
    else:
      temp_bracet = bracet3
    if n1 < n4:
      if n2 < n4:
        text = "L'union des deux intervalles vaut : "
        res = temp_bracet + str(n3) + ' ; ' + str(n4) + bracet4
      elif n2 == n4 and bracet4 == ']':
        text = "L'union des deux intervalles vaut : "
        res = temp_bracet + str(n3) + ' ; ' + str(n4) + ']'
      else:
        text = "L'union des deux intervalles vaut : "
        res = temp_bracet + str(n3) + ' ; ' + str(n2) + bracet2
    elif n1 == n4 and (bracet1 == '[' or bracet4 == ']'):
      text = "L'union des deux intervalles vaut : "
      res = bracet3 + str(n3) + ' ; ' + str(n2) + bracet2
    else:
      text = "Ici, on ne peut pas simplifier l'union, qui s'écrit donc : "
      res = bracet3 + str(n3) + ' ; ' + str(n4) + bracet4 + ' ∪ ' + bracet1 + str(n1) + ' ; ' + str(n2) + bracet2
  return jsonify({
    'statement':'''
    Déterminer l'union de ces deux intervalles : ''' + bracet1 + str(n1) + ' ; ' + str(n2) + bracet2 + " et " + bracet3 + str(n3) + ' ; ' + str(n4) + bracet4 + '''.
    ''',
    'solution':'''
    <div style='text-align: center'>
    Pour résoudre cet exercice, on peut éventuellement passer par les représentations graphiques des intervalles.<br/>
    ''' + text + res + '''.
    </div>
    '''
  }), 201

@app.route('/api/exercice/content/3')
def exercice_3():
  bracet1 = random.choice([']','['])
  bracet2 = random.choice([']','['])
  bracet3 = random.choice([']','['])
  bracet4 = random.choice([']','['])
  link = random.choice(['∪','∩'])
  numbers1 = sorted(random.sample(range(-9,5),2))
  nb1 = numbers1[0]
  nb2 = numbers1[1]
  numbers2 = sorted(random.sample(range(nb2,9),2))
  nb3 = numbers2[0]
  nb4 = numbers2[1]
  ecart1 = nb2 - nb1
  ecart2 = nb3 - nb2
  ecart3 = nb4 - nb3
  if nb1>=0:
    nb1 = '&nbsp;' + str(nb1)
  if nb2>=0:
    nb2 = '&nbsp;' + str(nb2)
  if nb3>=0:
    nb3 = '&nbsp;' + str(nb3)
  if nb4>=0:
    nb4 = '&nbsp;' + str(nb4)
  disjoint = True
  #Cas ou les intervalles ne sont pas disjoints
  if ecart2 == 0:
    if link == '∪' and (bracet2 == ']' or bracet3 == '['):
      disjoint = False
    if link == '∩' and bracet2 == ']' and bracet3 == '[':
      disjoint = False
  #assigner res et display
  if disjoint:
    if link == '∪':
      res = bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4
      if ecart2 == 0:
        display = "----<span style='color: #F44336'>" + bracet1 + '----'*ecart1 + bracet2 + '</span>' + ' ' + "<span style='color: #F44336'>" + bracet3 + '----'*ecart3 + bracet4 + '</span>' + '----' + '''<br/>
        <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-1) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-2) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
        '''
      else:
        display = "----<span style='color: #F44336'>" + bracet1 + '----'*ecart1 + bracet2 + '</span>' + '----'*ecart2 + "<span style='color: #F44336'>" + bracet3 + '----'*ecart3 + bracet4 + '</span>' + '----' + '''<br/>
        <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-3) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart2-3) + '''</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-3) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
        '''
    else:
      res = '∅'
      if ecart2 == 0:
        display = "----" + bracet1 + '----'*ecart1 + bracet2 + ' ' + bracet3 + '----'*ecart3 + bracet4 + '----' + '''<br/>
        <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-1) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-2) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
        '''
      else:
        display = "----" + bracet1 + '----'*ecart1 + bracet2 + '----'*ecart2 + bracet3 + '----'*ecart3 + bracet4 + '----' + '''<br/>
        <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-3) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart2-3) + '''</span> ''' + str(nb3) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-3) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
        '''
  else:
    if link == '∪':
      res = bracet1 + str(nb1) + ' ; ' + str(nb4) + bracet4
      display = "----<span style='color: #F44336'>" + bracet1 + '----'*ecart1 + '----'*ecart2 + '----'*ecart3 + bracet4 + '</span>' + '----' + '''<br/>
      <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-3) + '''</span> ''' + str(nb2) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-2) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
      '''
    else:
      res = '{' + str(nb2) + '}'
      display = "----" + '----'*ecart1 + "<span style='color: #F44336'>|</span>" + '----'*ecart3 + '----' + '''<br/>
      <span style='visibility:hidden;'>-</span> ''' + str(nb1) + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart1-3) + '''</span> ''' + "<span style='color: #F44336'>" + str(nb3) + "</span>" + ''' <span style='visibility:hidden;'>''' + '-'*(4*ecart3-2) + '''</span> ''' + str(nb4) + ''' <span style='visibility:hidden;'>----</span>
      '''
  if link == '∪':
    sol = '''
    Pour représenter l'union de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties. La partie coloriée est l'union des deux intervalles, ici ''' + res + '''.<br/><br/>
    <div style='display: inline-block; text-align: left'>
    ''' + display + '''
    </div><br/>
    '''
  else:
    if disjoint:
      sol = '''
      Lorsque deux intervalles sont disjoints, ils n'ont aucun élément en commun. Leur intersection vaut donc ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left'>
      ''' + display + '''
      </div><br/>
      '''
    else:
      sol = '''
      Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left'>
      ''' + display + '''
      </div><br/>
      '''

  return jsonify({
    'statement':'''
    <div>
    Représenter graphiquement l'intervalle ''' + bracet1 + str(nb1) + ' ; ' + str(nb2) + bracet2 + ' ' +  link + ' ' + bracet3 + str(nb3) + ' ; ' + str(nb4) + bracet4 + '''.
    </div>
    ''',
    'solution':'''
    <div style='text-align: center'>''' + sol + '''
    (les pointillés doivent être remplacés par une ligne continue)<br/>
    /!\ L'échelle doit être respectée pour avoir une réponse exacte : par exemple, il doit y avoir ''' + str(ecart1) + ''' unités entre les deux premiers crochets.
    </div>
    '''
  }), 201


@app.route('/api/exercice/content/4')
def exercice_4():
  return jsonify({
    'statement':'''
    ''',
    'solution':'''
    '''
  }), 201
