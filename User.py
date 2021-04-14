from flask import Flask , render_template , request
import mysql.connector

app=Flask(__name__)

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
        password = Signin['Lpassword']
        mycursor.execute("select * from registration where email='" + email + "' and password='" + password + "'")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        if (count == 1):
            return render_template("Grocery1.html")
        else:
            return render_template("Login.html")
    mydb.commit()
    mycursor.close()
@app.route('/Grocery1')
def grocery():
    return render_template("Grocery1.html")
@app.route('/Fruits')
def fruits():
    return render_template("Fruits.html")
@app.route('/Vegetables')
def vegetables():
    return render_template("Vegetables.html")
@app.route('/Beverages')
def beverages():
    return render_template("Beverages.html")
app.run(debug=True)