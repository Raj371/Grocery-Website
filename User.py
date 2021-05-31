from flask import Flask , render_template , request ,session
import mysql.connector
import json

app=Flask(__name__)
app.secret_key="Raj Project"
@app.route('/')
def signUp():
    return render_template("Login.html")

@app.route('/Logout')
def Logout():
    session.pop('email')
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

@app.route('/About')
def About():
    if "email" in session:
        return render_template("About.html")
    return render_template("Login.html")

@app.route('/Privacy')
def Privacy():
    if "email" in session:
        return render_template("PrivacyPolicy.html")
    return render_template("Login.html")

@app.route('/Terms')
def Terms():
    if "email" in session:
        return render_template("TermsConditions.html")
    return render_template("Login.html")
##############
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
        email=session['email']
        mycursor.execute("select * from carts where email='" + email +"'")
        data = mycursor.fetchall()
        r=mycursor.rowcount
        datas={}
        desc="YOU HAVE NOT ADDED ANY ITEM IN YOUR CART"
        datas['info']=data
        if(mycursor.rowcount>0):
            return render_template("newCart.html",datas=datas)
        return render_template("EmptyCart.html",desc=desc)
        mycursor.close()
    return render_template("Login.html")

#####################
@app.route('/insert',methods=["POST","GET"])
def insert():
    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="grocery_user"
        
        )
        mycursor=mydb.cursor()
        if(request.method=='POST'):
            print(request.data)
            data=request.get_json("text")
            print(data)
            email=session["email"]
            title=data['text']['title']
            price=int(data['text']['price'])*int(data['text']['quan'])
            imgsrc=data['text']['imgsrc']
            quan=data['text']['quan']
            mycursor.execute("insert into carts(email,title,price,imgsrc,quantity)values(%s,%s,%s,%s,%s)",(email,title,price,imgsrc,quan))
        mydb.commit()
        mycursor.close()
    except Exception as e:
        print("error",e)

    return "hascjs"

###################
@app.route('/delete',methods=["POST","GET"])
def delete():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_user"
    )
    mycursor=mydb.cursor()
    if(request.method=='POST'):
        index=request.get_json('index')
        ind=(int)(index['index'])
        email=session['email']
        mycursor.execute("delete from carts where email='" + email +"' and id='"+str(ind)+"'")
#        mycursor.execute("Delete from carts where email=(%s) and id=(%d}",(email,ind))     
        print("deleted: ",ind)
    mydb.commit()
    mycursor.close()

    return "deleted"

#####################
@app.route('/order',methods=["POST","GET"])
def order():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grocery_user"
    )
    mycursor=mydb.cursor()
    if(request.method=='POST'):
        email=session['email']
        print(email+"hello")
        mycursor.execute("Select * from carts where email='"+email+"'")
        data=mycursor.fetchall()
        for i in data:
            email=session["email"]
            title=i[2]
            price=(int)(i[3])
            imgsrc=i[4]
            quan=i[5]
            mycursor.execute("insert into ordered(email,title,price,imgsrc,quantity)values(%s,%s,%s,%s,%s)",(email,title,price,imgsrc,quan))
            mycursor.execute("delete from carts where email='"+email+"'")
            print("complete")
        mydb.commit()
        mycursor.close()
    return " ordered successfull"
app.run(debug=True)