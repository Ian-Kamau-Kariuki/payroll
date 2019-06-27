from app import db
from datetime import datetime

class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(25),unique=True,nullable=False)
    kra_pin = db.Column(db.String(25),unique=True,nullable=True)
    start_date = db.Column(db.DateTime,default=datetime.now())
    basic_salary = db.Column(db.Float(25), default=0)
    benefits = db.Column(db.Float(25), default=0)



    #create method
    def insert_method(self):
        db.session.add(self)
        db.session.commit()

    #Readd
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()
    #delete record
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(employee_id = id)
        record.delete()
        db.session.commit()
        return True