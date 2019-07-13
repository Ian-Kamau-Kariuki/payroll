from app import db
from datetime import datetime
from models.Payrolls import PayrollsModel

class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    gender = db.Column(db.String(10),nullable=True)
    email = db.Column(db.String(25),unique=True,nullable=False)
    kra_pin = db.Column(db.String(25),unique=True,nullable=True)
    start_date = db.Column(db.DateTime,default=datetime.now())
    basic_salary = db.Column(db.Float(25), default=0)
    benefits = db.Column(db.Float(25), default=0)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    status = db.Column(db.Integer,default=0)
    Payrolls = db.relationship(PayrollsModel,backref = 'employees')


    #create method
    def insert_method(self):
        db.session.add(self)
        db.session.commit()

    #Readd
    @classmethod
    def fetch_all_records(cls):
        return cls.query.filter_by(status=0)

    # check email
    @classmethod
    def check_existing_email(cls,email):
        record = cls.query.filter_by(email = email).first()
        return record
    # check kra
    @classmethod
    def check_existing_kra(cls,kra):
        record = cls.query.filter_by(kra_pin = kra).first()
        return record



    #delete record
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(employee_id = id).first()
        record.status=1

        db.session.commit()
        return True

    #update details
    @classmethod
    def update_by_id(cls,id,name = None,email = None,kra = None,salary=None,benefits=None):
        record = cls.query.filter_by(employee_id=id).first()

        if name:
            record.name = name
        if email:
            record.email = email
        if kra:
            record.kra_pin = kra
        if salary:
            record.basic_salary = salary
        if benefits:
            record.benefits = benefits

        db.session.commit()
        return True
    #fetch by id
    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(employee_id = id).first()