from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    def __repr__(self):
        return '<people %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    def __repr__(self):
        return '<planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    def __repr__(self):
        return '<vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }
    
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    def __repr__(self):
        return '<favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }