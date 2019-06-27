from app import db

class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    payroll_id = db.Column(db.Integer,primary_key=True)
    month = db.Column(db.String(25),nullable=False)
    gross_salary = db.Column(db.Float(25))
    payee = db.Column(db.Float(25))
    nhif = db.Column(db.Float(25))
    nssf = db.Column(db.Float(25))
    personal_relief = db.Column(db.Float(25))
    sacco_distribution = db.Column(db.Float(25))
    pension = db.Column(db.Float(25))
    net_salary = db.Column(db.Float(25))
    employee_id = db.Column(db.Integer,db.ForeignKey('employees.employee_id'))