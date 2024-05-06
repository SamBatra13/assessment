from database import db
from datetime import datetime

patient_doctor_association = db.Table(
    'patient_doctor_association',
    db.Column('patient_id', db.Integer, db.ForeignKey('patient.id'), primary_key=True),
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id'), primary_key=True)
)

class MedicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnoses = db.Column(db.String(200))
    allergies = db.Column(db.String(200))
    medications = db.Column(db.String(200))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    patient = db.relationship('Patient', backref='medical_history', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'diagnoses': self.diagnoses,
            'allergies': self.allergies,
            'medications': self.medications
        }

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    patient = db.relationship('Patient', backref='appointments', lazy=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    doctor = db.relationship('Doctor', backref='appointments', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'date_time': self.date_time,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id
        }                       

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120),unique=True)
    address = db.Column(db.String(200))
    gender = db.Column(db.String(10))
    doctors = db.relationship('Doctor', secondary=patient_doctor_association, backref='patients')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'doctors': [doctor.id for doctor in self.doctors],  # Only include the doctor IDs
            'medical_history': [history.serialize() for history in self.medical_history] if self.medical_history else None
        }

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _available_dates = db.Column(db.String(200))  # This could be a more complex type depending on your needs
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    doctor = db.relationship('Doctor', backref='schedule', lazy=True)

    @property
    def available_dates(self):
        # Convert the string of dates to a list of datetime objects
        dates = self._available_dates.split(',')
        return [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    @available_dates.setter
    def available_dates(self, dates):
        # Convert the list of datetime objects to a string of dates
        self._available_dates = ','.join(date.strftime("%Y-%m-%d") for date in dates)


    def serialize(self):
        return {
            'id': self.id,
            'available_dates': self._available_dates,
            'doctor_id': self.doctor_id
        }

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    specialization = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120),unique=True)
    address = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref='doctors', lazy=True)


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'patients': [patient.id for patient in self.patients],  # Only include the patient IDs
            'department': self.department_id,
            'schedule': [schedule.serialize() for schedule in self.schedule]
        }

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    services_offered = db.Column(db.String(80))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'services_offered': self.services_offered,
            'doctors': [doctor.serialize() for doctor in self.doctors]
        }