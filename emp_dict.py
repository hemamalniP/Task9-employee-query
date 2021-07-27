from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
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
@app.route('/top',methods=['GET'])
def fetc():
    det=db.session.query(emp).all()
    res=[]
    for i in det:
        op=i.__dict__
        op.pop('_sa_instance_state')
        res.append(op)
    return jsonify(res)
if __name__ == '__main__':
    app.run(debug=True)
