from flask import Blueprint
from flask_restful import Api
from modules.patient.controllers.patient import Patient, AssignOrDeassignDoctor, Appointment, MedicalHistory

patient_blueprint = Blueprint('patient', __name__, url_prefix='/patient')
patient_api = Api(patient_blueprint)

patient_api.add_resource(Patient, '/patient_details')
patient_api.add_resource(AssignOrDeassignDoctor, '/assign_doc_to_patient')
patient_api.add_resource(Appointment, '/appointment_details')
patient_api.add_resource(MedicalHistory, '/medical_history')