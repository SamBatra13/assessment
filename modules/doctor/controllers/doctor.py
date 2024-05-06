from flask_restful import Resource, request
from modules.doctor.services.doctor import DoctorHelper, ScheduleHelper
from flask import jsonify

class GetDoctor(Resource):
    def get(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            resp = DoctorHelper().get_doctor(name)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the doctors data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500


class AddDoctor(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            specialization = request_data.get("specialization")
            phone = request_data.get("phone")
            email = request_data.get("email")
            address = request_data.get("address")
            resp, status_code = DoctorHelper().add_doctor(name, specialization, phone, email, address)
            return {"data": resp, "status_code": status_code}, status_code
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class GetDoctorBySpeciality(Resource):
    def get(self):
        try:
            request_data = request.get_json()
            specialization = request_data.get("specialization")
            resp = DoctorHelper().get_doctor_by_specialization(specialization)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the doctors data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class SearchDoctorByavailability(Resource):
    def get(self):
        try:
            request_data = request.get_json()
            availability_date = request_data.get("availability_date")
            resp = DoctorHelper().search_doctor_by_availability(availability_date)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the doctors data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class AddDoctorSchedule(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            doctor_id = request_data.get("doctor_id")
            available_dates = request_data.get("available_dates")
            resp = ScheduleHelper().add_schedule(doctor_id, available_dates)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

    def get(self):
        try:
            request_data = request.get_json()
            doctor_id = request_data.get("doctor_id")
            resp = ScheduleHelper().get_schedule(doctor_id)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the doctors data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

    def delete(self):
        try:
            request_data = request.get_json()
            schedule_id = request_data.get("schedule_id")
            resp = ScheduleHelper().delete_schedule(schedule_id)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500