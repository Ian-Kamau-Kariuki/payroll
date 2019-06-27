from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@127.0.0.1:5432/june_payroll_system'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY']='56509b5ec2cf56fa6c7c71d54cdd698c'

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

@app.route('/payrolls/<int:id>')
def payrolls(id):
    return render_template('payroll.html')

@app.route('/delete/<int:id>')
def delete_record(id):
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('home'))
@app.route('/newemployee',methods=['POST'])
def create_new_employee():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        kra_pin = request.form['kra']
        basic_salary = request.form['basicsalary']
        benefits = request.form['benefits']
        #create object of class EmployeesModel
        emp = EmployeesModel(name = name,email=email,kra_pin=kra_pin,basic_salary=basic_salary,benefits=benefits)
        emp.insert_method()
        #redirect to home page

    return redirect(url_for('home'))



# if __name__ == '__main__':
#     app.run()
