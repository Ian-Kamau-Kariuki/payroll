from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Production
from resources.payroll_calculator import Employee
from flask_migrate import Migrate
import pygal

app = Flask(__name__)
app.config.from_object(Development)
app.config.from_object(Production)

db = SQLAlchemy(app)
Migrate = Migrate(app,db)

from models.Employees import EmployeesModel
from models.Payrolls import PayrollsModel


@app.before_first_request
def create_tables():
    db.create_all()

# @app.route('/auth')
# def authenticate():
#
#     return render_template('Authentication.html')
@app.route('/')
def home():
    employees = EmployeesModel.fetch_all_records()


    male = 0
    female = 0
    na = 0
    #use list comprehensions and count method to modify this for and if
    for emp in employees:
        if emp.gender == 'M':
            male+=1
        elif emp.gender =='F':
            female +=1
        else:
            na +=1

    pie_chart = pygal.Pie()
    pie_chart.title = 'Male vs Female Employees'
    pie_chart.add('Male Employees ', male)
    pie_chart.add('Female Employees ', female)
    pie_chart.add('Not Applicable ', na)
    graph = pie_chart.render_data_uri()

    return render_template('index.html',wafanyikazi = employees, graph =graph)

# view payrolls
@app.route('/payrolls/<int:id>')
def payrolls(id):
    payroll_welcome = EmployeesModel.fetch_by_id(id)
    return render_template('payroll.html', ya=payroll_welcome)

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

    current_user = EmployeesModel.fetch_by_id(id)

    if EmployeesModel.check_existing_kra(kra_pin) and kra_pin != current_user.kra_pin or EmployeesModel.check_existing_email(email) and email != current_user.email:
        flash("Email/Kra Pin already exists")

    EmployeesModel.update_by_id(id=id,name=name,email=email,kra=kra_pin,salary=basic_salary,benefits=benefits)
    return redirect(url_for('home'))



# add new employee
@app.route('/newemployee',methods=['POST'])
def create_new_employee():
    if request.method == "POST":
        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        kra_pin = request.form['kra']
        basic_salary = request.form['basicsalary']
        benefits = request.form['benefits']


        if EmployeesModel.check_existing_kra(kra_pin) or EmployeesModel.check_existing_email(email):
            flash("Email or KRA already exists")
            return redirect(url_for('home'))


        #create object of class EmployeesModel
        emp = EmployeesModel(name = name,email=email,gender=gender,kra_pin=kra_pin,basic_salary=basic_salary,benefits=benefits)
        emp.insert_method()
        #redirect to home page

    return redirect(url_for('home'))

@app.route('/generate/<int:uid>',methods=['POST'])
def generate_payroll(uid):
    month = request.form['month']
    year = request.form['year']
    overtime = request.form['overtime']

    month = month + str(year)

    employee = EmployeesModel.fetch_by_id(uid)
    basic = employee.basic_salary
    benefits = employee.benefits

    ya = Employee(basic,benefits)
    gross = ya.gross_salary
    payee = ya.calc_payee()
    nhif = ya.calc_NHIF()
    nssf = ya.nssf
    relief = 0
    sacco = 0
    pension = 0
    netSalary = ya.calc_net_salary()
    emp_id = uid

    pay = PayrollsModel(month=month,gross_salary=gross,payee=payee,nhif=nhif,nssf=nssf,personal_relief=relief,

                        sacco_distribution=sacco,pension=pension,net_salary=netSalary,employee_id=emp_id)
    # try:
    pay.insert_record()
    return redirect(url_for('payrolls', id=uid))
    # except:
    #     flash("Error in saving to the database")
    #     return redirect(url_for('payrolls', id=uid))

# if __name__ == '__main__':
#     app.run()
