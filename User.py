from flask import Flask , render_template , request ,session
import mysql.connector
import json
import simplejson

app=Flask(__name__)
app.secret_key="Raj Project"
@app.route('/')
def signUp():
    return render_template("Login.html")
    
@app.route('/result',methods=['POST','GET'])
def login():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_user"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        Signup=request.form
        email=Signup['mail']
        password=Signup['Spassword']
        cpassword = Signup['Scpassword']
        mobile=Signup['Snumber']
        address=Signup['Saddress']
        mycursor.execute("insert into registration(email,password,cpassword,phone,address)values(%s,%s,%s,%s,%s)",(email,password,cpassword,mobile,address))
        mydb.commit()
        mycursor.close()
    return render_template("Login.html")
@app.route('/display',methods=['POST','GET'])
def display():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_user"
    )
    mycursor = mydb.cursor()
    if (request.method == 'POST'):
        Signin = request.form
        email = Signin['Lemail']
        session['email']=email
        password = Signin['Lpassword']
        mycursor.execute("select * from registration where email='" + email + "' and password='" + password + "'")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        if (count == 1):
            print(session['email'])
            return render_template("Grocery1.html")
        else:
            return render_template("Login.html")
        
    mydb.commit()
    mycursor.close()
@app.route('/Grocery1')
def grocery():
    if "email" in session:
        return render_template("Grocery1.html")
    return render_template("Login.html")
@app.route('/Fruits')
def fruits():
    if "email" in session:
        return render_template("Fruits.html")
    return render_template("Login.html")
@app.route('/Vegetables')
def vegetables():
    if "email" in session:
        return render_template("Vegetables.html")
    return render_template("Login.html")
@app.route('/Beverages')
def beverages():
    if "email" in session:
        return render_template("Beverages.html")
    return render_template("Login.html")
@app.route('/Snacks')
def snacks():
    if "email" in session:
        return render_template("Snacks.html")
    return render_template("Login.html")

import itertools
@app.route('/Cart')
def cart():
    if "email" in session:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="grocery_user"
        )
        mycursor=mydb.cursor()
        mycursor.execute("select * from carts")
        data = mycursor.fetchall()
        r=mycursor.rowcount
        datas={}
        datas['info']=data
        return render_template("newCart.html",datas=datas)
        mycursor.close()
    return render_template("Login.html")

#####################
@app.route('/insert',methods=["POST","GET"])
def insert():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_user"
    )
    
    mycursor=mydb.cursor()
    if(request.method=='POST'):
        data=request.get_json("text")
        email=session["email"]
        title=data['title']
        price=int(data['price'])*int(data['quan'])
        imgsrc=data['imgsrc']
        quan=data['quan']
        mycursor.execute("insert into carts(email,title,price,imgsrc,quantity)values(%s,%s,%s,%s,%s)",(email,title,price,imgsrc,quan))
    mydb.commit()
    mycursor.close()
    return "hascjs"

app.run(debug=True)