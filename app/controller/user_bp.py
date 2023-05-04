from flask import Flask, Blueprint
from flask_restful import Api, Resource
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin

app = Flask(__name__)

user_bp = Blueprint('api_user', __name__)
api = Api(user_bp)

class collectuser(Resource):
  def get(self):

    return {"hello": "moto"}

api.add_resource(collectuser, '/')
app.register_blueprint(user_bp)
