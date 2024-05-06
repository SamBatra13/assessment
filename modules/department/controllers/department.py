from flask_restful import Resource, request
from modules.department.services.department import DepartmentHelper
from flask import jsonify

class GetDepartment(Resource):
    def get(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            resp = DepartmentHelper().get_department(name)
            if isinstance(resp, str):  # it's an error message
                return jsonify({'error': resp}), 400
            else:  # it's the department data
                return jsonify(resp)
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500


class AddDepartment(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            name = request_data.get("name")
            services_offered = request_data.get("services_offered")
            resp, status_code = DepartmentHelper().add_department(name, services_offered)
            return {"data": resp, "status_code": status_code}, status_code
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        

class AssignOrDeassignDepartment(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            doctor_id = request_data.get("doctor_id")
            department_id = request_data.get("department_id")
            type = request_data.get("type")
            resp = DepartmentHelper().assign_or_deassign_department(doctor_id, department_id, type)
            return {"data": resp, "status_code": 200}, 200
        except Exception as e:
            return {"message": str(e), "status_code": 500}, 500
        