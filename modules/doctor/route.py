from flask import Blueprint
from flask_restful import Api
from modules.doctor.controllers.doctor import GetDoctor, AddDoctor, GetDoctorBySpeciality, SearchDoctorByavailability, AddDoctorSchedule

doctor_blueprint = Blueprint('doctor', __name__, url_prefix='/doctor')
doctor_api = Api(doctor_blueprint)

doctor_api.add_resource(GetDoctor, '/doctor_get')
doctor_api.add_resource(AddDoctor, '/doctor_add')
doctor_api.add_resource(GetDoctorBySpeciality, '/doctor_get_by_speciality')
doctor_api.add_resource(SearchDoctorByavailability, '/doctor_get_by_availability')
doctor_api.add_resource(AddDoctorSchedule, '/doctor_schedule')
