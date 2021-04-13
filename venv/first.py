from flask import Flask , render_template , request
import mysql.connector

app=Flask(__name__)

@app.route('/')
def signUp():
    return render_template("../templates/Login.html")

@app.route('/Login.html',methods=['POST','GET'])
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

app.run(debug=True)