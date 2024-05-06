from flask import Flask, request, jsonify
from data.models import Patient, Appointment, Doctor, Schedule, MedicalHistory
from datetime import datetime, timedelta
from database import db

class PatientHelper:

    def get_patient(self, patient_name):
        try:
            patients = Patient.query.filter(Patient.name.contains(patient_name)).all()
            return [patient.serialize() for patient in patients]
        except Exception as e:
            print(e)
            return str(e)
    
    def search_appointments_tomorrow(self):
        try:
            tomorrow = datetime.now() + timedelta(days=1)
            start = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0)
            end = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 23, 59, 59)
            appointments = Appointment.query.filter(Appointment.date_time.between(start, end)).all()
            return jsonify([appointment.serialize() for appointment in appointments])
        except Exception as e:
            return str(e)
        
    def add_patient(self, patient_name, age, phone, email, address, gender):
        try:
            patient = Patient(name=patient_name, age=age, phone=phone, email=email,address=address, gender=gender)
            db.session.add(patient)
            db.session.commit()
            return "Patient added successfully", 200
        except Exception as e:
            return str(e),400
        
    def assign_or_deassign_doctor(self, patient_id, doctor_id, type):
        try:
            patient = Patient.query.filter_by(id=patient_id).first()
            doctor = Doctor.query.filter_by(id=doctor_id).first()
            if type == "assign":
                patient.doctors.append(doctor)
            elif type == "deassign":
                patient.doctors.remove(doctor)
            db.session.commit()
            return "Doctor assigned/deassigned successfully"
        except Exception as e:
            return str(e)
        
class MedicalHistoryHelper:
    
        def add_medical_history(self, patient_id, diagnoses, allergies, medications):
            try:
                medical_history = MedicalHistory(diagnoses=diagnoses, allergies=allergies, medications=medications, patient_id=patient_id)
                db.session.add(medical_history)
                db.session.commit()
                return "Medical history added successfully"
            except Exception as e:
                return str(e)
            
        def get_medical_history(self, patient_id):
            try:
                medical_history = MedicalHistory.query.filter_by(patient_id=patient_id).first()
                return medical_history.serialize()
            except Exception as e:
                return str(e)
            
        def update_medical_history(self, patient_id, diagnoses, allergies, medications):
            try:
                medical_history = MedicalHistory.query.filter_by(patient_id=patient_id).first()
                medical_history.diagnoses = diagnoses
                medical_history.allergies = allergies
                medical_history.medications = medications
                db.session.commit()
                return "Medical history updated successfully"
            except Exception as e:
                return str(e)
        

class AppointmentHelper:

    @staticmethod
    def schedule_appointment(patient_id, doctor_id, date_time):
        # Convert the date_time string to a datetime object
        date_time = datetime.strptime(date_time, "%Y-%m-%d")

        # Query the Schedule model for the doctor's schedule
        schedule = Schedule.query.filter_by(doctor_id=doctor_id).first()

        # Check if the doctor is available at the specified date and time
        if date_time not in schedule.available_dates:
            return "Doctor is not available at the specified date and time"

        # Create a new Appointment instance
        appointment = Appointment(date_time=date_time, patient_id=patient_id, doctor_id=doctor_id)

        # Add the appointment to the database
        db.session.add(appointment)
        db.session.commit()

        return "Appointment scheduled successfully"

    @staticmethod
    def cancel_appointment(appointment_id):
        # Query the Appointment model for the appointment
        appointment = Appointment.query.get(appointment_id)

        # Check if the appointment exists
        if appointment is None:
            return "Appointment not found"

        # Delete the appointment from the database
        db.session.delete(appointment)
        db.session.commit()

        return "Appointment cancelled successfully"
    
    def get_appointments(self, patient_id):
        try:
            appointments = Appointment.query.filter_by(patient_id=patient_id).all()
            return [appointment.serialize() for appointment in appointments]
        except Exception as e:
            return str(e)