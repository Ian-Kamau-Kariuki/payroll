from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Production

app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Production)

db = SQLAlchemy(app)

from models.Employees import EmployeesModel
from models.Payrolls import PayrollsModel


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    employees = EmployeesModel.fetch_all_records()
    return render_template('index.html',wafanyikazi = employees)

# view payrolls
@app.route('/payrolls/<int:id>')
def payrolls(id):
    return render_template('payroll.html')

# delete employee
@app.route('/delete/<int:id>')
def delete_record(id):
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('home'))

# edit employee
@app.route('/editemployee/<int:id>',methods=['POST'])
def edit_employee(id):
    name = request.form['name']
    email = request.form['email']
    kra_pin = request.form['kra']
    basic_salary = request.form['basicsalary']
    benefits = request.form['benefits']

    EmployeesModel.update_by_id(id=id,name=name,email=email,kra=kra_pin,salary=basic_salary,benefits=benefits)
    return redirect(url_for('home'))



# add new employee
@app.route('/newemployee',methods=['POST'])
def create_new_employee():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        kra_pin = request.form['kra']
        basic_salary = request.form['basicsalary']
        benefits = request.form['benefits']


        if EmployeesModel.check_existing_kra(kra_pin) or EmployeesModel.check_existing_email(email):
            flash("Email or KRA already exists")
            return redirect(url_for('home'))


        #create object of class EmployeesModel
        emp = EmployeesModel(name = name,email=email,kra_pin=kra_pin,basic_salary=basic_salary,benefits=benefits)
        emp.insert_method()
        #redirect to home page

    return redirect(url_for('home'))



# if __name__ == '__main__':
#     app.run()
