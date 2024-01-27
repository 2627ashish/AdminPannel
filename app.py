from flask import Flask, abort, render_template, request, redirect
from models import db, EmployeeModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('WelcomePage.HTML')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']

        # existing_employee = EmployeeModel.query.filter_by(employee_id=employee_id).first()

        # if existing_employee:
        #     # Handle duplicate employee_id
        #     return render_template('WelcomePage.HTML', error="Employee ID already exists. Please choose a different ID.")
        
            
        employee = EmployeeModel(
            employee_id=employee_id,
            name=name,
            position=position,
            salary=salary,
        )

        db.session.add(employee)
        db.session.commit()

        return redirect('/list')

@app.route('/list')
def retrieve_list():
    employee = EmployeeModel.query.all()
    return render_template('ListingPage.HTML', employee=employee)

@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/list')
            
        abort(404)
        # return redirect('/list')



@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.get(id)
    
    if not employee:
        abort(404)
    
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.salary = request.form['salary']
        db.session.commit()
        return redirect('/list')
    
    return render_template('UpdatePage.HTML', employee=employee)
   

app.run(host='localhost', port=5000)
