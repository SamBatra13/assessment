from flask import Blueprint
from flask_restful import Api, Resource

from modules.message_processor.routes import message_processor_blueprint


api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(message_processor_blueprint)
api = Api(api_blueprint)


class HealthAPI(Resource):
    @staticmethod
    def get():
        return {"status_code": 200, "message": "ok"}, 200


api.add_resource(HealthAPI, '/health')