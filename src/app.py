"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Characters
from models import db, Planets
from models import db, Vehicles
from models import db, Favorites


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

@app.route('/people', methods=['GET'])
def get_characters():
    json_text = jsonify(Characters)
    return json_text

@app.route('/planets', methods=['GET'])
def get_planets():
    json_text = jsonify(Planets)
    return json_text

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    json_text = jsonify(Vehicles)
    return json_text

@app.route('/favorites', methods=['GET'])
def get_favorites():
    json_text = jsonify(Favorites)
    return json_text

@app.route('/favorites', methods=['POST'])
def add_new_favorites():
    request_body = request.get_json(force=True)
    Favorites.append(request_body)
    json_text = jsonify(Favorites)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/favorites/<int:position>', methods=['DELETE'])
def delete_favorites(id):
    del(Favorites.id)
    json_text = jsonify(Favorites)
    print("This is the position to delete: ", id)
    return json_text

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
