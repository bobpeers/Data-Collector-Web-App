#Import dependencies
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#Create instance of Flask App
app = Flask(__name__)

#Connect to the Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://qlypyonycmvmjc:4d216baa0889e5e1cf70f59ba26f9fa25e6abc2b6c86d952a489b6c3ef7bf452@ec2-23-23-184-76.compute-1.amazonaws.com:5432/d8cvi73sj545ot?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    #create a table
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    shoesize = db.Column(db.Integer)
    sex = db.Column(db.String)

    def __init__(self, height, weight, shoesize, sex):
        self.height = height
        self.weight = weight
        self.shoesize = shoesize
        self.sex = sex

#Define Route and Contant of that page
@app.route("/")
def index():
    return render_template("index.html")

#Define 2nd Route and Content
@app.route("/success", methods = ['POST'])
def success():
    if(request.method == 'POST'):
        height_ = request.form["height"]
        weight_ = request.form["weight"]
        shoesize_ = request.form["shoesize"]
        sex_ = request.form["sex"]
        data = Data(height_,weight_,shoesize_,sex_)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True)
