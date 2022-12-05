from flask import Flask, render_template , request, redirect, session, url_for
import mysql.connector
import hashlib


app = Flask(__name__)

app.secret_key = 'mys secret key'

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
    if 'loggedin' in session:
        return redirect(url_for('chat'))
    else:

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
    if 'loggedin' in session:
        return redirect(url_for('chat'))
    else:

        msg=''
        if request.method == 'POST' and 'nikname' in request.form and 'password' in request.form:
            # Create variables for easy access
            nikname = request.form['nikname']
            password = request.form['password']
            hash_pass = hashlib.md5(password.encode("utf-8")).hexdigest()
            # Check if account exists using MySQL
            mycursor = mydb.cursor()
            mycursor.execute('SELECT * FROM user WHERE pseudo = %s AND passwd = %s', (nikname, hash_pass,))
            # Fetch one record and return result
            account = mycursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account[0]
                session['nikname'] = account[3]
                # Redirect to home page
                return redirect(url_for('chat'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
        return render_template ('login.html')
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('nikname', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/chat')
def chat():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('chat.html', username=session['nikname'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
    
    

app.run(host='0.0.0.0')