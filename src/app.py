"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, Characters
from models import db, Planets
from models import db, Vehicles
from models import db, UserFavorites
from models import db, FavoriteCharacter
from models import db, FavoritePlanet
from models import db, FavoriteVehicle


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

@app.route('/user', methods=['GET'])
def get_user():
    json_text = jsonify(User)
    return json_text


@app.route('/people', methods=['GET'])
def get_characters():
    json_text = jsonify(Characters)
    return json_text

@app.route('/people/<int:people_id>', methods=['GET'])
def get_character_by_id():
    json_text = jsonify(Characters)
    return json_text

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    user = User.query.get(user.id)

    user.favorite_planets
    planets_serialized = [p.serialized() for p in planets]
    return jsonify(planets_serialized), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id():
    json_text = jsonify(Planets)
    return json_text

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    json_text = jsonify(Vehicles)
    return json_text

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id():
    json_text = jsonify(Vehicles)
    return json_text

@app.route('/users', methods=['GET'])
def get_users():
    json_text = jsonify(User)
    return json_text

@app.route('/users/favorites', methods=['GET'])
def get_favorites():
    json_text = jsonify(UserFavorites)
    return json_text

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_new_favorite_character(character_id):
    request_body = request.get_json(force=True)
    FavoriteCharacter(character_id).append(request_body)
    json_text = jsonify(FavoriteCharacter)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_new_favorite_planet(planet_id):
    request_body = request.get_json(force=True)
    FavoritePlanet(planet_id).append(request_body)
    json_text = jsonify(FavoritePlanet)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_new_favorite_vehicle(vehicle_id):
    request_body = request.get_json(force=True)
    FavoriteVehicle(vehicle_id).append(request_body)
    json_text = jsonify(FavoriteVehicle)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/users/favorites', methods=['POST'])
def add_new_favorites():
    request_body = request.get_json(force=True)
    UserFavorites.append(request_body)
    json_text = jsonify(UserFavorites)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_character(character_id):
    del(FavoriteCharacter(character_id))
    json_text = jsonify(FavoriteCharacter)
    print("This is the position to delete: ", id)
    return json_text

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    del(FavoritePlanet(planet_id))
    json_text = jsonify(FavoritePlanet)
    print("This is the position to delete: ", id)
    return json_text

@app.route('/favorite/vehicle/<int:vehicle>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    del(FavoriteVehicle[vehicle_id])
    json_text = jsonify(FavoriteVehicle)
    print("This is the position to delete: ", id)
    return json_text

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
