from app import app,db
from flask import jsonify
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter, forms
from wtforms import StringField, validators
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    is_enabled = db.Column(db.Boolean(), nullable=False, default=True)
    first_name = db.Column(db.String(50), nullable=False, default='')
    last_name = db.Column(db.String(50), nullable=False, default='')
    classe = db.Column(db.String(50), nullable=False, default='2nde')

		# Relationships
    roles = db.relationship('Role', secondary='user_roles',
						backref=db.backref('users', lazy='dynamic'))

    def to_json(self):
      return {
        'id': self.id,
        'email': self.email,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'classe': self.classe
      }

    def is_active(self):
      return self.is_enabled

    def create(self):
      db.session.add(self)
      db.session.commit()
      return jsonify( {'user': self} ), 201


class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')

    # Setup for flask-login
    is_authenticated = db.Column(db.Boolean(), default=False)
    is_active = db.Column(db.Boolean(), default=True)
    is_anonymous = db.Column(db.Boolean(), default=False)

    # Relationships
    user = db.relationship('User', uselist=False, foreign_keys=user_id)

    def get_id(self):
      return unicode(self.user_id)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return jsonify( {'userAuth': self} ), 201

# Define the Role data model
class Role(db.Model):
		id = db.Column(db.Integer(), primary_key=True)
		name = db.Column(db.String(50), unique=True)

# Define the UserRoles data model
class UserRoles(db.Model):
		id = db.Column(db.Integer(), primary_key=True)
		user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
		role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

class MyRegisterForm(forms.RegisterForm):
    first_name = StringField('First name', validators=[
          validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
          validators.DataRequired('Last name is required')])

# Create all database tables
db.create_all()

# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

#Setup Flask-login
login_manager = LoginManager()
login_manager.init_app(app)

'''
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

manager.run()
'''
