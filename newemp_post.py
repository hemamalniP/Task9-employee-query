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
@app.route('/etr',methods=['POST'])
def emrec():
    id=request.args.get('id')
    name=request.args.get('name')
    city=request.args.get('city')
    addr=request.args.get('addr')
    pin=request.args.get('pin')
    salary=request.args.get('salary')
    ipt=request.get_json()
    print(ipt)
    det=emp(id=ipt['id'],name=ipt['name'],city=ipt['city'],addr=ipt['addr'],pin=ipt['pin'],salary=ipt['salary'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")

if __name__ == '__main__':
    app.run(debug=True)
