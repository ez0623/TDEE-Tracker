from tdee_app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    stats = db.relationship('Stats', backref='username', lazy=True)

    def __repr__(self):
        return f'User("{self.username}","{self.password}")'

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Integer())
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    start_weight = db.Column(db.Integer, nullable=False)
    current_weight = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Stats("{self.user_id}","{self.date}")'
