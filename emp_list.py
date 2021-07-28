from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc,desc,func
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class emp(db.Model):
    __tablename__='empsalary'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    salary = db.Column(db.String(200))
    def __init__(self,id,name,city,addr,pin,salary):
        self.id=id
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin
        self.salary=salary
class new(db.Model):
    __tablename__='empdetails'
    id = db.Column('id', db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100))
    father_name = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    marital_status = db.Column(db.String(50))
    def __init__(self,id,emp_name,father_name,mother_name,marital_status):
        self.id=id
        self.emp_name=emp_name
        self.father_name=father_name
        self.mother_name=mother_name
        self.marital_status=marital_status
@app.route('/join',methods=['GET'])
def join():
    det = db.session.query(emp).join(new, new.id == emp.id).filter(emp.id ==10).with_entities(emp.id,new.emp_name,new.father_name,new.mother_name,new.marital_status)
    res = {}
    for row in det:
        row_as_dict = dict(row)
        res.update(row_as_dict)
        return dict(res)
if __name__ == '__main__':
    app.run(debug=True)
