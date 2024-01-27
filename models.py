from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class EmployeeModel(db.Model):
    # students is the model name
    __tablename__ = "employee"
    # data base definition
  
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String())
    position = db.Column(db.String())
    salary = db.Column(db.Integer())
 
    def __init__(self, employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name = name
        self.position = position
        self.salary = salary

    # returning value
    def __repr__(self):
        return f"{self.name}:{self.position}"