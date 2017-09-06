# -*-coding:utf-8 -*
from json import dumps
from requests import put, get, post, delete

####### Clean db ########
delete('http://localhost:5000/api/chapter/delete_all')
delete('http://localhost:5000/api/objective/delete_all')
delete('http://localhost:5000/api/exercice/delete_all')
######## End clean db #########


#couleurs : bleu : "#82B1FF", rouge : "#EA80FC", orange : "#FF9E80", vert : "#009688"
chapters=[
  {
    'nb':0,
    'name':u'Intervalles',
    'class_id':1,
    'color':'#82B1FF',
    'available':True
  },
  {
    'nb':1,
    'name':u'Expressions algébriques',
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':2,
    'name':u"Structure d'un algorithme",
    'class_id':1,
    'color':'#EA80FC'
  },
  {
    'nb':3,
    'name':u'Repérage et configurations du plan',
    'class_id':1,
    'color':'#009688'
  },
  {
    'nb':4,
    'name':u"Fonctions numériques",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':5,
    'name':u"Algorithmie : boucles et itérateurs",
    'class_id':1,
    'color':'#EA80FC'
  },
  {
    'nb':6,
    'name':u"Statistiques",
    'class_id':1,
    'color':'#FF9E80'
  },
  {
    'nb':7,
    'name':u"Variations de fonctions",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':8,
    'name':u"Algorithmie : notion de fonction",
    'class_id':1,
    'color':'#EA80FC'
  },
  {
    'nb':9,
    'name':u"Géométrie dans l'espace",
    'class_id':1,
    'color':'#009688'
  },
  {
    'nb':10,
    'name':u"Résolutions graphiques",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':11,
    'name':u"Probabilités",
    'class_id':1,
    'color':'#FF9E80'
  },
  {
    'nb':12,
    'name':u"Premier degré : fonctions et équations",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':13,
    'name':u"Équations de droites",
    'class_id':1,
    'color':'#009688'
  },
  {
    'nb':14,
    'name':u"Second degré : fonctions et équations",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':15,
    'name':u"Vecteurs : partie 1",
    'class_id':1,
    'color':'#009688'
  },
  {
    'nb':16,
    'name':u"Fonction inverse",
    'class_id':1,
    'color':'#82B1FF'
  },
  {
    'nb':17,
    'name':u"Vecteurs : partie 2",
    'class_id':1,
    'color':'#009688'
  },
  {
    'nb':18,
    'name':u"Échantillonage",
    'class_id':1,
    'color':'#FF9E80'
  },
  {
    'nb':19,
    'name':u"Trigonométrie",
    'class_id':1,
    'color':'#82B1FF'
  }
]

objectives = [
  {
    'chapter_id':1,
    'nb':1,
    'name':u"Comprendre les notions d'union et d'intersection d'intervalles"
  },
  {
    'chapter_id':1,
    'nb':2,
    'name':u"Représenter graphiquement des intervalles"
  },
  {
    'chapter_id':2,
    'nb':1,
    'name':u"Développer des expressions polynomiales simples"
  },
  {
    'chapter_id':2,
    'nb':2,
    'name':u"Factoriser des expressions polynomiales simples"
  },
  {
    'chapter_id':2,
    'nb':3,
    'name':u"Mettre un problème en équation"
  },
  {
    'chapter_id':2,
    'nb':4,
    'name':u"Connaître et reconnaître les identités remarquables"
  },
  {
    'chapter_id':2,
    'nb':5,
    'name':u"Lire un tableau de signes"
  },
  {
    'chapter_id':4,
    'nb':5,
    'name':u"Connaître les propriétés des figures planes usuelles"
  },
  {
    'chapter_id':4,
    'nb':6,
    'name':u"Utiliser les propriétés des symétries axiales ou centrales"
  },
  {
    'chapter_id':4,
    'nb':7,
    'name':u"Construire la tangente à un cercle en l'un de ses points"
  },
  {
    'chapter_id':4,
    'nb':1,
    'name':u"Repérer un point donné du plan"
  },
  {
    'chapter_id':4,
    'nb':2,
    'name':u"Placer un point en connaissant ses coordonnées"
  },
  {
    'chapter_id':4,
    'nb':3,
    'name':u"Calculer la distance entre deux points"
  },
  {
    'chapter_id':4,
    'nb':4,
    'name':u"Calculer les coordonnées du milieu d'un segment"
  },
  {
    'chapter_id':3,
    'nb':1,
    'name':u"Choisir ou déterminer le type d'une variable"
  },
  {
    'chapter_id':3,
    'nb':2,
    'name':u"Résoudre un problème simple par un algorithme"
  },
  {
    'chapter_id':5,
    'nb':1,
    'name':u"Calculer l'image d'un réel par une fonction"
  },
  {
    'chapter_id':5,
    'nb':2,
    'name':u"Lire graphiquement l'image d'un réel par une fonction"
  },
  {
    'chapter_id':5,
    'nb':3,
    'name':u"Déterminer si un point est sur une courbe représentative"
  },
  {
    'chapter_id':5,
    'nb':4,
    'name':u"Déterminer le domaine de définition d'une fonction"
  },
  {
    'chapter_id':5,
    'nb':5,
    'name':u"Tracer la courbe représentative d'une fonction"
  },
  {
    'chapter_id':5,
    'nb':6,
    'name':u"Calculer les antécédents d'un réel par une fonction"
  },
  {
    'chapter_id':5,
    'nb':7,
    'name':u"Lire graphiquement les antécédents d'un réel par une fonction"
  },
  {
    'chapter_id':5,
    'nb':8,
    'name':u"Lire et utiliser un tableau de valeurs"
  },
  {
    'chapter_id':6,
    'nb':1,
    'name':u"Programmer une instruction conditionnelle"
  },
  {
    'chapter_id':6,
    'nb':2,
    'name':u"Programmer une boucle bornée"
  },
  {
    'chapter_id':6,
    'nb':3,
    'name':u"Programmer une boucle non bornée"
  },
  {
    'chapter_id':7,
    'nb':1,
    'name':u"Passer des effectifs aux fréquences, et inversement"
  },
  {
    'chapter_id':7,
    'nb':3,
    'name':u"Dresser un tableau statistique"
  },
  {
    'chapter_id':7,
    'nb':4,
    'name':u"Représenter graphiquement une série statistique"
  },
  {
    'chapter_id':7,
    'nb':5,
    'name':u"Calculer les caractéristiques de position d'une série statistique"
  },
  {
    'chapter_id':7,
    'nb':6,
    'name':u"Calculer les caractéristiques de dispersion d'une série statistique"
  },
  {
    'chapter_id':7,
    'nb':2,
    'name':u"Calculer des effectifs et fréquences cumulé(e)s"
  },
  {
    'chapter_id':8,
    'nb':1,
    'name':u"Décrire le comportement d'une fonction"
  },
  {
    'chapter_id':8,
    'nb':2,
    'name':u"Déterminer le minimum/maximum d'une fonction sur un intervalle"
  },
  {
    'chapter_id':8,
    'nb':3,
    'name':u"Déterminer des inégalités algébriques grâce aux variations d'une fonction"
  },
  {
    'chapter_id':8,
    'nb':5,
    'name':u"Dresser un tableau de variations"
  },
  {
    'chapter_id':8,
    'nb':4,
    'name':u"Lire un tableau de variations"
  },
  {
    'chapter_id':9,
    'nb':1,
    'name':u"Programmer des fonctions simples"
  },
  {
    'chapter_id':10,
    'nb':1,
    'name':u"Représenter des solides en perspective"
  },
  {
    'chapter_id':10,
    'nb':2,
    'name':u"Reconnaître les solides usuels"
  },
  {
    'chapter_id':10,
    'nb':3,
    'name':u"Calculer des longueurs, des aires, des volumes"
  },
  {
    'chapter_id':11,
    'nb':1,
    'name':u"Résoudre graphiquement une équation"
  },
  {
    'chapter_id':11,
    'nb':2,
    'name':u"Résoudre graphiquement une inéquation"
  },
  {
    'chapter_id':12,
    'nb':1,
    'name':u"Exprimer des évènements en fonction d'autres évènements"
  },
  {
    'chapter_id':12,
    'nb':3,
    'name':u"Déterminer la probabilité d'évènements en situation d'équiprobabilité"
  },
  {
    'chapter_id':12,
    'nb':5,
    'name':u"Proposer un modèle probabiliste à partir de fréquences observées"
  },
  {
    'chapter_id':12,
    'nb':4,
    'name':u"Exploiter les formules du cours"
  },
  {
    'chapter_id':12,
    'nb':2,
    'name':u"Dénombrer des ensembles finis"
  },
  {
    'chapter_id':13,
    'nb':1,
    'name':u"Donner le sens de variations d'une fonction affine"
  },
  {
    'chapter_id':13,
    'nb':2,
    'name':u"Dresser le tableau de signes d'une fonction affine"
  },
  {
    'chapter_id':13,
    'nb':3,
    'name':u"Résoudre algébriquement une équation du premier degré"
  },
  {
    'chapter_id':13,
    'nb':4,
    'name':u"Résoudre algébriquement une inéquation du premier degré"
  },
  {
    'chapter_id':14,
    'nb':1,
    'name':u"Tracer une droite dans le plan repéré"
  },
  {
    'chapter_id':13,
    'nb':4,
    'name':u"Calculer le coefficient directeur d'une droite"
  },
  {
    'chapter_id':14,
    'nb':5,
    'name':u"Lire graphiquement une équation de droite"
  },
  {
    'chapter_id':14,
    'nb':3,
    'name':u"Trouver l'ordonnée à l'origine d'une droite"
  },
  {
    'chapter_id':14,
    'nb':6,
    'name':u"Calculer une équation de droite à partir de deux points"
  },
  {
    'chapter_id':14,
    'nb':7,
    'name':u"Montrer que trois points sont alignés"
  },
  {
    'chapter_id':14,
    'nb':8,
    'name':u"Montrer que deux droites sont parallèles ou sécantes"
  },
  {
    'chapter_id':14,
    'nb':9,
    'name':u"Déterminer les coordonnées du point d'intersection de deux droites sécantes"
  },
  {
    'chapter_id':14,
    'nb':2,
    'name':u"Lier l'équation de la droite aux coordonnées des points de la droite"
  },
  {
    'chapter_id':15,
    'nb':1,
    'name':u"Connaître les propriétés de la fonction carré"
  },
  {
    'chapter_id':15,
    'nb':2,
    'name':u"Donner le tableau de variations d'une fonction polynôme du second degré"
  },
  {
    'chapter_id':15,
    'nb':3,
    'name':u"Résoudre une équation du second degré"
  },
  {
    'chapter_id':15,
    'nb':4,
    'name':u"Résoudre une inéquation du second degré"
  },
  {
    'chapter_id':16,
    'nb':1,
    'name':u"Placer un point défini par un vecteur"
  },
  {
    'chapter_id':16,
    'nb':2,
    'name':u"Utiliser la propriété du parallélogramme"
  },
  {
    'chapter_id':16,
    'nb':3,
    'name':u"Lire graphiquement les coordonnées d'un vecteur"
  },
  {
    'chapter_id':16,
    'nb':4,
    'name':u"Calculer les coordonnées d'un vecteur"
  },
  {
    'chapter_id':16,
    'nb':5,
    'name':u"Calculer les coordonnées de la somme de deux vecteurs"
  },
  {
    'chapter_id':16,
    'nb':6,
    'name':u"Représenter la somme de deux vecteurs"
  },
  {
    'chapter_id':16,
    'nb':7,
    'name':u"Utiliser la relation de Chasles"
  },
  {
    'chapter_id':17,
    'nb':1,
    'name':u"Connaître les propriétés de la fonction inverse"
  },
  {
    'chapter_id':17,
    'nb':2,
    'name':u"Résoudre des équations utilisant des quotients"
  },
  {
    'chapter_id':17,
    'nb':3,
    'name':u"Résoudre des inéquations utilisant des quotients"
  },
  {
    'chapter_id':18,
    'nb':1,
    'name':u"Montrer que deux vecteurs sont colinéaires"
  },
  {
    'chapter_id':18,
    'nb':2,
    'name':u"Utiliser la colinéarité de deux vecteurs"
  },
  {
    'chapter_id':19,
    'nb':1,
    'name':u"Calculer un intervalle de fluctuation"
  },
  {
    'chapter_id':19,
    'nb':2,
    'name':u"Exercer un regard critique sur une information"
  },
  {
    'chapter_id':20,
    'nb':1,
    'name':u"Résoudre algébriquement un système de deux équations à deux inconnues"
  },
  {
    'chapter_id':20,
    'nb':2,
    'name':u"Résoudre graphiquement un système de deux équations à deux inconnues"
  },
  {
    'chapter_id':21,
    'nb':1,
    'name':u"Connaître les valeurs usuelles des fonctions trigonométriques"
  }
]

exercices = [
  {
    'chapter_id':1,
    'obj_id':2,
    'name':"Représenter un intervalle",
    'difficulty':1,
    'url':'api/exercice/content/1'
  },
  {
    'chapter_id':1,
    'obj_id':2,
    'name':"Représenter des unions et des intersections",
    'difficulty':2,
    'url':'api/exercice/content/2'
  },
  {
    'chapter_id':1,
    'obj_id':2,
    'name':"Représenter des unions et des intersections d'intervalles disjoints",
    'difficulty':2,
    'url':'api/exercice/content/3'
  },
  {
    'chapter_id':1,
    'obj_id':1,
    'name':"Appartenance à un intervalle",
    'difficulty':1,
    'url':'api/exercice/content/4'
  },
  {
    'chapter_id':1,
    'obj_id':1,
    'name':"Lien entre inégalités et intervalles",
    'difficulty':1,
    'url':'api/exercice/content/5'
  },
  {
    'chapter_id':1,
    'obj_id':1,
    'name':"Calculer une union d'intervalles",
    'difficulty':2,
    'url':'api/exercice/content/6'
  },
  {
    'chapter_id':1,
    'obj_id':1,
    'name':"Calculer une intersection d'intervalles",
    'difficulty':2,
    'url':'api/exercice/content/7'
  },
  {
    'chapter_id':1,
    'obj_id':1,
    'name':"Vrai ou faux ?",
    'difficulty':2,
    'url':'api/exercice/content/8'
  },
]

for chapter in chapters:
  post('http://localhost:5000/api/chapter', data=dumps(chapter)).json()
for obj in objectives:
  post('http://localhost:5000/api/objective', data=dumps(obj))
for exo in exercices:
  post('http://localhost:5000/api/exercice', data=dumps(exo))
#print get('http://localhost:5000/api/chapter/34').json()
