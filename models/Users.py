# from main import db
# from models.Employees import EmployeesModel
#
# class UsersModel(db.Model):
#     __tablename__='users'
#     user_id=db.Column(db.Integer,primary_key=True)
#     full_name=db.Column(db.String(25),nullable=False)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String())
#
#     employees = db.relationship(EmployeesModel,backref='users')
#
#
#     #insert record
#     def Insert_record(self):
#         db.session.add(self)
#         db.session.commit()
