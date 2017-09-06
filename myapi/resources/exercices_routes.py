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
    <div style='text-align: center; margin-bottom: 25px'>
    &#9472;&#9472;&#9472;&#9472;''' + '''<span style='color: #F44336'>''' + first_bracet + "<span style='position: relative; top: 25px; right: 13px'>" + str(first_nb) +  "</span>" + '<span style="margin-left: -15px"></span>' + '&#9472;&#9472;&#9472;'*(second_nb-first_nb) + second_bracet + "<span style='position: relative; top: 25px; right: 13px'>" + str(second_nb) +  "</span>" + '''</span>''' + '<span style="margin-left: -15px"></span>' + '''&#9472;&#9472;&#9472;&#9472;<br/>
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
  def below(nb):
    return "<span style='position: relative; top: 25px; right: 13px;'>" + str(nb) + "</span><span style='margin-left: -18px'></span>" 
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
    <div style='display: inline-block; text-align: left; margin-bottom: 25px'>
    &#9472;&#9472;<span style='color: #F44336'>''' + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + below(nb3) + '&#9472;&#9472;'*ecart2 + below(nb2) + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + "</span>" + '</span>' + '&#9472;&#9472;' + '''<br/>
    </div><br/>
    '''
  else:
    sol = '''
    Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + bracet3 + str(nb3) + ' ; ' + str(nb2)  + bracet2 + '''.<br/><br/>
    <div style='display: inline-block; text-align: left; margin-bottom: 25px'>
    &#9472;&#9472;''' + below(nb1) + '&#9472;&#9472;'*ecart1 + "<span style='color: #F44336'>" + bracet3 + below(nb3) + '&#9472;&#9472;'*ecart2 + bracet2 + below(nb2) + "</span>" + '&#9472;&#9472;'*ecart3 + below(nb4) + '&#9472;&#9472;' + '''<br/>
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
  def below(nb):
    return "<span style='position: relative; top: 25px; right: 13px;'>" + str(nb) + "</span><span style='margin-left: -18px'></span>" 
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
        display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + bracet2 + '</span>' + ' ' + below(nb2) + "<span style='color: #F44336'>" + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + '</span>' + '&#9472;&#9472;' + '<br/>'
      else:
        display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + bracet2 + below(nb2) + '</span>' + '&#9472;&#9472;'*ecart2 + "<span style='color: #F44336'>" + bracet3 + below(nb3) + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + '</span>' + '&#9472;&#9472;' + '<br/>'
    else:
      res = '∅'
      if ecart2 == 0:
        display = "&#9472;&#9472;" + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + bracet2 + ' ' + below(nb2) + bracet3 + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + '&#9472;&#9472;' + '<br/>'
      else:
        display = "&#9472;&#9472;" + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + bracet2 + below(nb2) + '&#9472;&#9472;'*ecart2 + bracet3 + below(nb3) + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + '&#9472;&#9472;' + '<br/>'
  else:
    if link == '∪':
      res = bracet1 + str(nb1) + ' ; ' + str(nb4) + bracet4
      display = "&#9472;&#9472;<span style='color: #F44336'>" + bracet1 + below(nb1) + '&#9472;&#9472;'*ecart1 + below(nb2) + '&#9472;&#9472;'*ecart3 + bracet4 + below(nb4) + '</span>' + '&#9472;&#9472;' + '<br/>'
    else:
      res = '{' + str(nb2) + ' }'
      display = "&#9472;&#9472;" + below(nb1) + '&#9472;&#9472;'*ecart1 + "<span style='color: #F44336'>|" + below(nb3) +  "</span>" + '&#9472;&#9472;'*ecart3 + below(nb4) + '&#9472;&#9472;' + '<br/>'
  if link == '∪':
    sol = ''' 
    Pour représenter l'union de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties. La partie coloriée est l'union des deux intervalles, ici ''' + res + '''.<br/><br/>
    <div style='display: inline-block; text-align: left; margin-bottom: 25px'>
    ''' + display + '''
    </div><br/>
    '''
  else:
    if disjoint:
      sol = '''
      Lorsque deux intervalles sont disjoints, ils n'ont aucun élément en commun. Leur intersection vaut donc ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left; margin-bottom: 25px'>
      ''' + display + '''
      </div><br/>
      '''
    else:
      sol = '''
      Pour représenter l'intersection de deux intervalles, on dessine les deux intervalles graphiquement et on colorie les deux parties avec deux couleurs différentes. La partie coloriée deux fois est l'intersection des deux intervalles, ici ''' + res + '''.<br/><br/>
      <div style='display: inline-block; text-align: left; margin-bottom: 25px'>
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
  n0 = random.sample(range(-10,10),1)[0]
  numbers1 = sorted(random.sample(range(-10,10),2))
  n1 = numbers1[0]
  n2 = numbers1[1]
  statement = "Le réel " + str(n0) + " appartient-il à l'intervalle " + bracet1 + str(n1) + " ; " + str(n2) + bracet2 + " ?"
  result = "n'appartient pas"
  if n0 == n1 and bracet1 == "[":
    explication = "l'intervalle est <span style='font-weight: bold'>fermé</span> en " + str(n1) + ", ce qui signifie que le réel " + str(n1) + " est dans cet intervalle."
    result = "appartient bien"
  elif n0 > n1 and n0 < n2:
    explication = "le nombre réel " + str(n0) + " est strictement compris entre les nombres réels " + str(n1) + " et " + str(n2) + "."
    result = "appartient bien"
  elif n0 == n2 and bracet2 == "]":
    explication = "l'intervalle est <span style='font-weight: bold'>fermé</span> en " + str(n2) + ", ce qui signifie que le réel " + str(n2) + " est dans cet intervalle."
    result = "appartient bien"
  elif n0 == n1:
    explication = "le nombre réel " + str(n0) + " est celui de la première borne, mais celle-ci est <span style='font-weight: bold'>ouverte</span>, donc ne fait pas partie de l'intervalle."
  elif n0 == n2:
    explication = "le nombre réel " + str(n0) + " est celui de la deuxième borne, mais celle-ci est <span style='font-weight: bold'>ouverte</span>, donc ne fait pas partie de l'intervalle."
  elif n0 < n1:
    explication = "le nombre réel " + str(n0) + " est strictement plus petit que la première borne de l'intervalle, " + str(n1) + " ; il ne peut donc pas en faire partie."
  else:
    explication = "le nombre réel " + str(n0) + " est strictement plus grand que la deuxième borne de l'intervalle, " + str(n2) + " ; il ne peut donc pas en faire partie."
  solution = "Le réel " + str(n0) + " <span style='font-weight: bold'>" + result + "</span> à l'intervalle " + bracet1 + str(n1) + " ; " + str(n2) + bracet2 + ".<br/> En effet, " + explication
  return jsonify({
    'statement': statement,
    'solution':'''
    <div style='text-align: center'>
    ''' + solution + '''
    </div>
    '''
  }), 201
  
@app.route('/api/exercice/content/5')
def exercice_5():
  sign1 = random.choice(['<','≤'])
  sign2 = random.choice(['<','≤'])
  numbers1 = sorted(random.sample(range(-10,10),2))
  n1 = numbers1[0]
  n2 = numbers1[1]
  statement = "Quel est l'intervalle qui correspond à : " + str(n1) + " " + sign1 + " x " + sign2 + " " + str(n2) + " ?"
  bracet1 = "]" if sign1=='<' else '['
  bracet2 = "[" if sign2=='<' else ']'
  solution = bracet1 + str(n1) + " ; " + str(n2) + bracet2
  return jsonify({
    'statement':statement,
    'solution':'''
    <div style='text-align: center'>
    L'intervalle correspondant est <span style='font-weight: bold'>''' + solution + '''</span>.<br/><br/>
    <span style='font-style: italic'>Lorsque l'inégalité est stricte (<), x ne peut être égal à cette valeur, donc l'intervalle est ouvert. Sinon (inégalité large ≤), il est fermé.</span>
    </div>
    '''
  }), 201

@app.route('/api/exercice/content/6')
def exercice_6():
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
    <span style='font-weight: bold'>''' + text + res + '''</span>.<br/><br/>
    <span style='font-style: italic'>Pour résoudre cet exercice, on peut éventuellement passer par les représentations graphiques des intervalles.<br/>
    Rappel : une union d'intervalles est l'ensemble des nombres réels qui appartiennent à l'un ou à l'autre de ces intervalles.<br/></span>
    </div>
    '''
  }), 201

@app.route('/api/exercice/content/7')
def exercice_7():
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
      text = "Les deux intervalles sont disjoints, ce qui signifie que le résultat est l'ensemble vide : "
      res = "∅"
    elif n2 == n3:
      if bracet2 == ']' and bracet3 == '[':
        text = "Il n'y a qu'un élément appartenant aux deux intervalles, donc leur intersection vaut : "
        res = "{" + str(n2) + "}"
      else:
        text = "Les deux intervalles sont disjoints, ce qui signifie que le résultat est l'ensemble vide : "
        res = "∅"
    else:
      if n2 < n4:
        text = "L'intersection des deux intervalles vaut : "
        res = bracet3 + str(n3) + ' ; ' + str(n2) + bracet2
      else:
        if n2 == n4 and bracet4 == ']':
          text = "L'intersection des deux intervalles vaut : "
          res = bracet3 + str(n3) + ' ; ' + str(n2) + bracet2
        else:
          text = "L'intersection des deux intervalles vaut : "
          res = bracet3 + str(n3) + ' ; ' + str(n4) + bracet4
  else:
    if n1 == n3 and bracet1 == '[':
      temp_bracet = bracet3
    else:
      temp_bracet = bracet1
    if n1 < n4:
      if n2 < n4:
        text = "L'intersection des deux intervalles vaut : "
        res = temp_bracet + str(n1) + ' ; ' + str(n2) + bracet2
      elif n2 == n4 and bracet4 == ']':
        text = "L'intersection des deux intervalles vaut : "
        res = temp_bracet + str(n1) + ' ; ' + str(n2) + bracet2
      else:
        text = "L'intersection des deux intervalles vaut : "
        res = temp_bracet + str(n1) + ' ; ' + str(n4) + bracet4
    elif n1 == n4 and bracet1 == '[' and bracet4 == ']':
      text = "Il n'y a qu'un élément appartenant aux deux intervalles, donc leur intersection vaut : "
      res = "{" + str(n1) + "}"
    else:
      text = "Les deux intervalles sont disjoints, ce qui signifie que le résultat est l'ensemble vide : "
      res = "∅"
  return jsonify({
    'statement':'''
    Déterminer l'intersection de ces deux intervalles : ''' + bracet1 + str(n1) + ' ; ' + str(n2) + bracet2 + " et " + bracet3 + str(n3) + ' ; ' + str(n4) + bracet4 + '''.
    ''',
    'solution':'''
    <div style='text-align: center'>
    <span style='font-weight: bold'>''' + text + res + '''</span>.<br/><br/>
    <span style='font-style: italic'>Pour résoudre cet exercice, on peut éventuellement passer par les représentations graphiques des intervalles.<br/>
    Rappel : une intersection de deux intervalles est l'ensemble des nombres réels appartenant à l'un et à l'autre de ces intervalles (autrement dit, les nombres réels communs aux deux intervalles).<br/>
    </span>
    </div>
    '''
  }), 201

@app.route('/api/exercice/content/8')
def exercice_8():
  bracet1 = random.choice([']','['])
  bracet2 = random.choice([']','['])
  bracet3 = random.choice([']','['])
  numbers1 = sorted(random.sample(range(-10,10),2))
  n1 = numbers1[0]
  n3 = numbers1[1]
  n2 = random.randrange(-10,n3)
  rand = random.choice([x*0.1 for x in range(1,9)])
  if n1 > n2 or (n1 == n2 and (bracet1 == ']' or bracet2 == '[')):
    solution = "C'est <span style='font-weight: bold'>vrai</span> !<br/><br/> <span style='font-style: italic'>On dit aussi que l'intervalle " + bracet1 + str(n1) + " ; " + str(n3) + bracet3 + " est <span style='font-weight: bold'>inclus</span> dans l'intervalle " + bracet2 + str(n2) + " ; " + str(n3) + bracet3 + ", ce que l'on note : " + bracet1 + str(n1) + " ; " + str(n3) + bracet3 + " ⊂ " + bracet2 + str(n2) + " ; " + str(n3) + bracet3 + ".</span>"
  else:
    explication = ""
    if n1 < n2 - 1:
      n0 = random.randrange(n1,n2-1)
      n0 = n0 + rand
      explication = "<br/><br/><span style='font-style: italic'>Si tu n'avais pas le même contre-exemple, cela ne veut pas dire que ta réponse est incorrecte ! Il y a une infinité de contre-exemples possibles, alors vérifie juste que le tien fonctionne bien.</span>"
    elif n1 < n2:
      n0 = n1 + rand
      explication = "<br/><br/><span style='font-style: italic'>Si tu n'avais pas le même contre-exemple, cela ne veut pas dire que ta réponse est incorrecte ! Il y a une infinité de contre-exemples possibles, alors vérifie juste que le tien fonctionne bien.</span>"
    else:
      n0 = n1
      explication = "<br/><br/><span style='font-style: italic'>Ici, c'est le seul contre-exemple possible !</span>"
    solution = "C'est <span style='font-weight: bold'>faux</span> ! Par exemple, le nombre réel " + str(n0) + " est dans l'intervalle " + bracet1 + str(n1) + " ; " + str(n3) + bracet3 + ", mais n'est pas dans l'intervalle " + bracet2 + str(n2) + " ; " + str(n3) + bracet3 + "." + explication
  statement = "Vrai ou faux ? Si x ∈ " + bracet1 + str(n1) + " ; " + str(n3) + bracet3 + ", alors x ∈ " + bracet2 + str(n2) + " ; " + str(n3) + bracet3 + ".<br/><span style='font-style: italic'>Si la réponse est 'faux', le prouver par un contre-exemple.</span>"
  return jsonify({
    'statement':statement,
    'solution':'''
    <div style='text-align: center'>
    ''' + solution + '''
    </div>
    '''
  }), 201

