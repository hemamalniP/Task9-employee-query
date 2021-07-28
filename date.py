from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc,desc,func
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class empdet(db.Model):
    __tablename__='empdetail'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(50))
    place = db.Column(db.String(200))
    pincode = db.Column(db.String(50))
    doj = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    salary = db.Column(db.String(200))
    def __init__(self,id,name,age,place,pincode,doj,contact,salary):
        self.id = id
        self.name = name
        self.age = age
        self.place = place
        self.pincode = pincode
        self.doj = doj
        self.contact = contact
        self.salary = salary

@app.route('/join',methods=['GET'])
def join():
    det = db.session.query(empdet).filter(empdet.doj.between('2021-07-20','2021-07-27')).all()
    res = []
    for i in det:
        op = i.__dict__
        op.pop('_sa_instance_state')
        res.append(op)
    return jsonify(res)
if __name__ == '__main__':
    app.run(debug=True)
