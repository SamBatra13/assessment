from flask import Blueprint
from flask_restful import Api, Resource

from modules.department.route import department_blueprint
from modules.doctor.route import doctor_blueprint
from modules.patient.route import patient_blueprint


api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(department_blueprint)
api_blueprint.register_blueprint(doctor_blueprint)
api_blueprint.register_blueprint(patient_blueprint)
api = Api(api_blueprint)


class HealthAPI(Resource):
    @staticmethod
    def get():
        return {"status_code": 200, "message": "ok"}, 200


api.add_resource(HealthAPI, '/health')