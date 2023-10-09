from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    characters = db.relationship("Favorites", secondary="favorite_character")
    planets = db.relationship("Favorites", secondary="favorite_planet")
    vehicles = db.relationship("Favorites", secondary="favorite_vehicle")

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    users = db.relationship("User", secondary="favorite_characters")

    def __repr__(self):
        return '<people %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }    


class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    users = db.relationship("User", secondary="favorite_planets")

    def __repr__(self):
        return '<planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }


class Vehicle(db.Model):
    __tablename__ = 'vechicles'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(350), unique=True, nullable=False)

    users = db.relationship("User", secondary="favorite_vehicles")

    def __repr__(self):
        return '<vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
        }


class UserFavorites(db.Model):
    __tablename__ = 'user_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    user = db.relationship(User, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))
    character = db.relationship(Character, backref=db.backref("favorite_characters", cascade="all, delete-orphan"))
    planet = db.relationship(Planet, backref=db.backref("favorite_planets", cascade="all, delete-orphan"))
    vehicle = db.relationship(Vehicle, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.character, '<FavoritePlanet %r>' % self.planet, '<FavoriteVehicle %r>' % self.vehicle

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_id,
            "planet_name": self.planet_id,
            "vehicle_name": self.vehicle_id,
        }

db.create_all()