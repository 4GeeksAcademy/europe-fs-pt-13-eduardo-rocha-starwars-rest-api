from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.user_name,
        }

class Characters(db.Model):
    __tablename__ = 'characters'
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
    __tablename__ = 'planets'
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
    __tablename__ = 'vechicles'
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

class FavoriteCharacter(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_name = db.Column(db.Integer, db.ForeignKey('characters.name'))
    user = db.relationship(User, backref=db.backref("favorite_characters", cascade="all, delete-orphan"))
    character = db.relationship(Characters, backref=db.backref("favorite_characters", cascade="all, delete-orphan"))

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.character

    def serialize(self):
        return {
            "id": self.id,
            "name": self.character_name,
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_name = db.Column(db.Integer, db.ForeignKey('planets.name'))
    user = db.relationship(User, backref=db.backref("favorite_planets", cascade="all, delete-orphan"))
    planet = db.relationship(Planets, backref=db.backref("favorite_planets", cascade="all, delete-orphan"))

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.planet

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
        }

class FavoriteVehicle(db.Model):
    __tablename__ = 'favorite_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicle_name = db.Column(db.Integer, db.ForeignKey('vehicles.name'))
    user = db.relationship(User, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))
    vehicle = db.relationship(Vehicles, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.vehicle

    def serialize(self):
        return {
            "id": self.id,
            "name": self.vehicle_name,
        }

class UserFavorites(db.Model):
    __tablename__ = 'user_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    user = db.relationship(User, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))
    character = db.relationship(Characters, backref=db.backref("favorite_characters", cascade="all, delete-orphan"))
    planet = db.relationship(Planets, backref=db.backref("favorite_planets", cascade="all, delete-orphan"))
    vehicle = db.relationship(Vehicles, backref=db.backref("favorite_vehicles", cascade="all, delete-orphan"))

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.character, '<FavoritePlanet %r>' % self.planet, '<FavoriteVehicle %r>' % self.vehicle

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_id,
            "planet_name": self.planet_id,
            "vehicle_name": self.vehicle_id,
        }