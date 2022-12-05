from flask import Flask, render_template , request, redirect
import mysql.connector
import hashlib


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="chat-app"

)

print(mydb)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('fname')
        lastname = request.form.get('lname')
        email = request.form.get('email')
        passwd = request.form.get('password')
        passwdc = request.form.get('passwordc')

        gender = request.form.get('gender')
        birth = request.form.get('birth')
        nikname = request.form.get('nikname')

        hash_pass = hashlib.md5(passwd.encode("utf-8")).hexdigest()
        
        mycursor = mydb.cursor()

        sql = "INSERT INTO user (first_name, last_name, pseudo, email, passwd, gender, dateofbirth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name,lastname,nikname,email,hash_pass,gender,birth)
        mycursor.execute(sql, val)
        
        mydb.commit()    
        print(mycursor.rowcount, "record inserted.")

    return render_template ('signup.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password') 
    print (email)
    return render_template ('login.html')

    
@app.route('/chat')
def chat():
    return render_template ('chat.html')
    

app.run(host='0.0.0.0')