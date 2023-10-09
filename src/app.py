"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, Character
from models import db, Planet
from models import db, Vehicle
from models import db, UserFavorites


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# USER-----------------------------------------------------------------------------------------------
# create a User
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating user'}), 500)

# get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)
    
# get user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting user'}), 500)

# Update user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      user.username = data['username']
      user.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating user'}), 500)

# DELETE a User
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting user'}), 500)

# CHARACTERS-----------------------------------------------------------------------------------------------
# create a character
@app.route('/people', methods=['POST'])
def create_character():
    try:
        data = request.get_json()
        new_character = Character(charactername=data['charactername'], uid=data['character.id'], url=data['character.url'])
        db.session.add(new_character)
        db.session.commit()
        return make_response(jsonify({'message': 'character created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating character'}), 500)

# get all characters
@app.route('/people', methods=['GET'])
def get_characters():
    try:
        characters = Character.query.all()
        return make_response(jsonify([character.json() for character in characters]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)
    
# get character by ID
@app.route('/people/<int:id>', methods=['GET'])
def get_character(id):
  try:
    character = Character.query.filter_by(id=id).first()
    if character:
      return make_response(jsonify({'character': character.json()}), 200)
    return make_response(jsonify({'message': 'character not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting character'}), 500)

# Update a character
@app.route('/users/<int:id>', methods=['PUT'])
def update_character(id):
  try:
    character = Character.query.filter_by(id=id).first()
    if character:
      data = request.get_json()
      character.charactername = data['charactername']
      character.uid = data['uid']
      character.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating user'}), 500)

# DELETE a character
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_character(id):
  try:
    character = User.query.filter_by(id=id).first()
    if character:
      db.session.delete(character)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting user'}), 500)


# PLANETS-----------------------------------------------------------------------------------------------
# create a planet
@app.route('/planets', methods=['POST'])
def create_planet():
    try:
        data = request.get_json()
        new_planet = Planet(charactername=data['planetname'], uid=data['planet.id'], url=data['planet.url'])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(jsonify({'message': 'character created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating character'}), 500)

# get all planets
@app.route('/planets', methods=['GET'])
def get_planets():
    try:
        planets = Planet.query.all()
        return make_response(jsonify([planet.json() for planet in planets]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)
    
# get a planet by id
@app.route('/planets/<int:id>', methods=['GET'])
def get_character(id):
  try:
    planet = Planet.query.filter_by(id=id).first()
    if planet:
      return make_response(jsonify({'planet': planet.json()}), 200)
    return make_response(jsonify({'message': 'planet not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting planet'}), 500)

# update a planet
@app.route('/planets/<int:id>', methods=['PUT'])
def update_character(id):
  try:
    planet = Planet.query.filter_by(id=id).first()
    if planet:
      data = request.get_json()
      planet.charactername = data['charactername']
      planet.uid = data['uid']
      planet.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'planet updated'}), 200)
    return make_response(jsonify({'message': 'planet not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating planet'}), 500)

# delete a planet
@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
  try:
    planet = Planet.query.filter_by(id=id).first()
    if planet:
      db.session.delete(planet)
      db.session.commit()
      return make_response(jsonify({'message': 'planet deleted'}), 200)
    return make_response(jsonify({'message': 'planet not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting planet'}), 500)


# VEHICLES-----------------------------------------------------------------------------------------------
# create a vehicle
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    try:
        data = request.get_json()
        new_vehicle = Vehicle(vehiclename=data['vehiclename'], uid=data['vehicle.id'], url=data['vehicle.url'])
        db.session.add(new_vehicle)
        db.session.commit()
        return make_response(jsonify({'message': 'vehicle created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating vehicle'}), 500)

# get all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    try:
        vehicles = Vehicle.query.all()
        return make_response(jsonify([vehicle.json() for vehicle in vehicles]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting vehicles'}), 500)
    
# get vehicle by ID
@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle(id):
  try:
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
      return make_response(jsonify({'vehicle': vehicle.json()}), 200)
    return make_response(jsonify({'message': 'vehicle not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting vehicle'}), 500)

# Update a vehicle
@app.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle(id):
  try:
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
      data = request.get_json()
      vehicle.charactername = data['charactername']
      vehicle.uid = data['uid']
      vehicle.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'vehicle updated'}), 200)
    return make_response(jsonify({'message': 'vehicle not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating vehicle'}), 500)

# DELETE a vehicle
@app.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_character(id):
  try:
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
      db.session.delete(vehicle)
      db.session.commit()
      return make_response(jsonify({'message': 'vehicle deleted'}), 200)
    return make_response(jsonify({'message': 'vehicle not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting vehicle'}), 500)


# FAVORITES-----------------------------------------------------------------------------------------------

# create a favorite character
@app.route('/favorites/character', methods=['POST'])
def create_favorite_character():
    try:
        data = request.get_json()
        new_favorite_character = UserFavorites(charactername=data['charactername'], uid=data['character.id'], url=data['character.url'])
        db.session.add(new_favorite_character)
        db.session.commit()
        return make_response(jsonify({'message': 'favorite character created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating favorite character'}), 500)

# create a favorite planet
@app.route('/favorites/planet', methods=['POST'])
def create_favorite_planet():
    try:
        data = request.get_json()
        new_favorite_planet = UserFavorites(planetname=data['planetname'], uid=data['planet.id'], url=data['planet.url'])
        db.session.add(new_favorite_planet)
        db.session.commit()
        return make_response(jsonify({'message': 'favorite planet created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating favorite planet'}), 500)
    
# create a favorite vehicle
@app.route('/favorites/vehicle', methods=['POST'])
def create_favorite_vehicle():
    try:
        data = request.get_json()
        new_favorite_vehicle = UserFavorites(vehiclename=data['vehiclename'], uid=data['vehicle.id'], url=data['vehicle.url'])
        db.session.add(new_favorite_vehicle)
        db.session.commit()
        return make_response(jsonify({'message': 'favorite vehicle created'}), 201)
    except e:
        return make_response(jsonify({'message': 'error creating favorite vehicle'}), 500)

# get all favorites
@app.route('/favorites', methods=['GET'])
def get_favorites():
    try:
        favorites = UserFavorites.query.all()
        return make_response(jsonify([favorite.json() for favorite in favorites]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)
    
# get favorite character by id
@app.route('/favorites/character/<int:id>', methods=['GET'])
def get_favorite_character(id):
  try:
    favorite_character = UserFavorites.query.filter_by(id=id).first()
    if favorite_character:
      return make_response(jsonify({'favorite character': favorite_character.json()}), 200)
    return make_response(jsonify({'message': 'favorite character not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting favorite character'}), 500)

# get favorite planet by id
@app.route('/favorites/planet/<int:id>', methods=['GET'])
def get_favorite_planet(id):
  try:
    favorite_planet = UserFavorites.query.filter_by(id=id).first()
    if favorite_planet:
      return make_response(jsonify({'favorite character': favorite_planet.json()}), 200)
    return make_response(jsonify({'message': 'favorite character not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting favorite character'}), 500)

# get favorite vehicle by id
@app.route('/favorites/vehicle/<int:id>', methods=['GET'])
def get_favorite_vehicle(id):
  try:
    favorite_vehicle = UserFavorites.query.filter_by(id=id).first()
    if favorite_vehicle:
      return make_response(jsonify({'favorite character': favorite_vehicle.json()}), 200)
    return make_response(jsonify({'message': 'favorite character not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting favorite character'}), 500)

# Update a favorites character
@app.route('/favorites/character/<int:id>', methods=['PUT'])
def update_favorite_character(id):
  try:
    favorite = UserFavorites.query.filter_by(id=id).first()
    if favorite:
      data = request.get_json()
      favorite.charactername = data['charactername']
      favorite.uid = data['uid']
      favorite.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'favorite character updated'}), 200)
    return make_response(jsonify({'message': 'favorite character not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating favorite character'}), 500)

# Update a favorites planet
@app.route('/favorites/planet/<int:id>', methods=['PUT'])
def update_favorite_planet(id):
  try:
    favorite = UserFavorites.query.filter_by(id=id).first()
    if favorite:
      data = request.get_json()
      favorite.planetname = data['planetname']
      favorite.uid = data['uid']
      favorite.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'favorite planet updated'}), 200)
    return make_response(jsonify({'message': 'favorite planet not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating favorite planet'}), 500)

# Update a favorites vehicle
@app.route('/favorites/vehicle/<int:id>', methods=['PUT'])
def update_favorite(id):
  try:
    favorite = UserFavorites.query.filter_by(id=id).first()
    if favorite:
      data = request.get_json()
      favorite.vehiclename = data['vehiclename']
      favorite.uid = data['uid']
      favorite.url = data['url']
      db.session.commit()
      return make_response(jsonify({'message': 'favorite vehicle updated'}), 200)
    return make_response(jsonify({'message': 'favorite vehicle not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating favorite vehicle'}), 500)

# DELETE a favorite
@app.route('/favorites/<int:id>', methods=['DELETE'])
def delete_character(id):
  try:
    favorite = UserFavorites.query.filter_by(id=id).first()
    if favorite:
      db.session.delete(favorite)
      db.session.commit()
      return make_response(jsonify({'message': 'favorite deleted'}), 200)
    return make_response(jsonify({'message': 'favorite not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting favorite'}), 500)


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
