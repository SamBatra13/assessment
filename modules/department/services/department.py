from flask import Flask, request, jsonify
from data.models import Department, Doctor
from datetime import datetime, timedelta
from database import db

class DepartmentHelper:

    def get_department(self, department_name):
        try:
            departments = Department.query.filter(Department.name.contains(department_name)).all()
            return [department.serialize() for department in departments]
        except Exception as e:
            return str(e)
        
    def add_department(self, doctor_name, services_offered):
        try:
            department = Department(name=doctor_name, services_offered=services_offered)
            db.session.add(department)
            db.session.commit()
            return "Department added successfully", 200
        except Exception as e:
            return str(e), 400
        
    def assign_or_deassign_department(self, doctor_id, department_id, type):
        try:
            resp = ""
            doctor = Doctor.query.filter_by(id=doctor_id).first()
            department = Department.query.filter_by(id=department_id).first()
            if doctor is None:
                return "Doctor not found"
            if department is None:
                return "Department not found"
            if type == 'assign':
                doctor.department = department
                resp = "Department assigned successfully"
            elif type == 'deassign':
                if doctor.department == department:
                    doctor.department = None
                    resp = "Department deassigned successfully"
                else:
                    resp = "Doctor is not assigned to the department"
            db.session.commit()
            return resp
        except Exception as e:
            return str(e)