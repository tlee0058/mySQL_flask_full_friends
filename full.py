from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends') #not always with db

@app.route("/")
def index_full():
    friends = mysql.query_db("SELECT * FROM users") # the table within db
    
    
    return render_template("index_full.html", all_friend = friends)

@app.route('/add_user', methods = ['POST'])
def adding_user():
    name = request.form['name']
    age = request.form['age']
    query = "INSERT INTO users (name, age, friend_since, year) VALUES (:name, :age, NOW(), NOW())"
    data = {
        'name' : name,
        'age' : age
    }
    mysql.query_db(query, data)
    return redirect ("/")

app.run(debug=True)