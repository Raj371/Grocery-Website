from flask import Flask , render_template , request
import mysql.connector

app=Flask(__name__)

@app.route('/')
def login():
    return render_template("Login.html")

app.run(debug=True)