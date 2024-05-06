from flask_restful import Resource, request
from modules.patient.services.patient import PatientHelper, AppointmentHelper, MedicalHistoryHelper
from flask import jsonify

class Patient(Resource):
    def get(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            resp = PatientHelper().get_patient(name)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the patient data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        
    def post(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            age = request_data.get("age")
            phone = request_data.get("phone")
            email = request_data.get("email")
            address = request_data.get("address")
            gender = request_data.get("gender")
            resp, status_code = PatientHelper().add_patient(name, age, phone, email, address, gender)
            return {"data": resp, "status_code": status_code}, status_code
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class AssignOrDeassignDoctor(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            doctor_id = request_data.get("doctor_id")
            type = request_data.get("type")
            resp = PatientHelper().assign_or_deassign_doctor(patient_id, doctor_id, type)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class Appointment(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            doctor_id = request_data.get("doctor_id")
            date_time = request_data.get("date_time")
            type = request_data.get("type")
            appointment_id = request_data.get("appointment_id")
            if type == "cancel":
                resp = AppointmentHelper().cancel_appointment(appointment_id=appointment_id)
                return {"data": resp, "status_code": 200}, 200
            elif type == "schedule":
                resp = AppointmentHelper().schedule_appointment(patient_id, doctor_id, date_time)
                return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        
    def get(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            resp = AppointmentHelper().get_appointments(patient_id)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the appointments data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class MedicalHistory(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            diagnoses = request_data.get("diagnoses")
            allergies = request_data.get("allergies")
            medications = request_data.get("medications")
            resp = MedicalHistoryHelper().add_medical_history(patient_id, diagnoses, allergies, medications)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        
    def get(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            resp = MedicalHistoryHelper().get_medical_history(patient_id)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the medical history data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        
    def put(self):
        try:
            request_data = request.get_json()
            patient_id = request_data.get("patient_id")
            diagnoses = request_data.get("diagnoses")
            allergies = request_data.get("allergies")
            medications = request_data.get("medications")
            resp = MedicalHistoryHelper().update_medical_history(patient_id, diagnoses, allergies, medications)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500