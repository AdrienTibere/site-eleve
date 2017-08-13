from app import app,db
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    is_enabled = db.Column(db.Boolean(), nullable=False, default=False)
    first_name = db.Column(db.String(50), nullable=False, default='')
    last_name = db.Column(db.String(50), nullable=False, default='')

		# Relationships
		roles = db.relationship('Role', secondary='user_roles',
						backref=db.backref('users', lazy='dynamic'))

    def is_active(self):
      return self.is_enabled


class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')

    # Relationships
    user = db.relationship('User', uselist=False, foreign_keys=user_id)

# Define the Role data model
class Role(db.Model):
		id = db.Column(db.Integer(), primary_key=True)
		name = db.Column(db.String(50), unique=True)

# Define the UserRoles data model
class UserRoles(db.Model):
		id = db.Column(db.Integer(), primary_key=True)
		user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
		role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

# Create all database tables
db.create_all()

# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User
