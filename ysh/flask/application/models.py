"""
models.py

App Engine datastore models

"""


from application import db, app

from flask.ext.login import LoginManager, UserMixin

class BadModel(db.Model):
	__tablename__ = 'BadModel'
	"""result model"""
	id = db.Column(db.Integer, primary_key =True)
	text = db.Column(db.String(120))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)


from flask.ext.login import LoginManager

lm = LoginManager(app)
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

lm.login_view = 'index'


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(140))
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


	def __repr__(self):
		return '<Post %r>'% (self.body)
