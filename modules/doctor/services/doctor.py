from flask import Flask, request, jsonify
from data.models import Doctor, Schedule
from datetime import datetime, timedelta
from database import db

class DoctorHelper:

    def get_doctor(self, doctor_name):
        try:
            doctors = Doctor.query.filter(Doctor.name.contains(doctor_name)).all()
            return [doctor.serialize() for doctor in doctors]
        except Exception as e:
            return str(e)
        
    def add_doctor(self, doctor_name, specialization, phone, email, address):
        try:
            doctor = Doctor(name=doctor_name, specialization=specialization, phone=phone, email=email,address=address)
            db.session.add(doctor)
            db.session.commit()
            return "Doctor added successfully", 200
        except Exception as e:
            return str(e), 400
        
    def get_doctor_by_specialization(self, specialization):
        try:
            doctors = Doctor.query.filter(Doctor.specialization.contains(specialization)).all()
            return [doctor.serialize() for doctor in doctors]
        except Exception as e:
            return str(e)
        
    def search_doctor_by_availability(self, availability_date):
        try:
            doctors = []
            a_date = datetime.strptime(availability_date, "%Y-%m-%d").date()
            schedules = Schedule.query.all()
            schedules = [schedule for schedule in schedules if a_date in schedule.available_dates]
            doctors = [schedule.doctor for schedule in schedules]
        except Exception as e:
            print("Error: ", e)
        return doctors
        

class ScheduleHelper:
        
    
    def add_schedule(self, doctor_id, available_dates):
        try:
            doctor = Doctor.query.get(doctor_id)
            schedule = Schedule(doctor=doctor, _available_dates=available_dates)
            db.session.add(schedule)
            db.session.commit()
            return "Schedule added successfully"
        except Exception as e:
            return str(e)
        
    def get_schedule(self, doctor_id):
        try:
            doctor = Doctor.query.get(doctor_id)
            if doctor is None:
                return "Doctor not found"
            available_dates = []
            for schedule in doctor.schedule:
                available_dates.extend(schedule._available_dates.split(','))
            return {
                'doctor_id': doctor.id,
                'doctor_name': doctor.name,
                'available_dates': available_dates
            }
        except Exception as e:
            return str(e)
        
    def delete_schedule(self, schedule_id):
        try:
            schedule = Schedule.query.get(schedule_id)
            if schedule is None:
                return "Schedule not found"
            db.session.delete(schedule)
            db.session.commit()
            return "Schedule deleted successfully"
        except Exception as e:
            return str(e)
        
    def update_schedule(self, doctor_id, old_date, new_date):
        try:
            doctor = Doctor.query.get(doctor_id)
            schedule = doctor.schedule
            dates = schedule.available_dates
            dates.remove(old_date)
            dates.append(new_date)
            schedule.available_dates = dates
            db.session.commit()
            return "Schedule updated successfully"
        except Exception as e:
            return str(e)
        
    def get_available_slots(self, doctor_id, date):
        try:
            doctor = Doctor.query.get(doctor_id)
            schedule = doctor.schedule
            dates = schedule.available_dates
            return dates
        except Exception as e:
            return str(e)
        
    def get_next_available_slot(self, doctor_id):
        try:
            doctor = Doctor.query.get(doctor_id)
            schedule = doctor.schedule
            dates = schedule.available_dates
            return min(dates)
        except Exception as e:
            return str(e)
        
    def get_available_slots_in_range(self, doctor_id, start_date, end_date):
        try:
            doctor = Doctor.query.get(doctor_id)
            schedule = doctor.schedule
            dates = schedule.available_dates
            return [date for date in dates if start_date <= date <= end_date]
        except Exception as e:
            return str(e)
        