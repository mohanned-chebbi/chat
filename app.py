from flask import Flask, render_template , request, redirect
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello'

@app.route('/signup', methods = ['GET','POST'])
def signup():
    name = request.form.get('fname')
    lastname = request.form.get('lname')
    email = request.form.get('email')
    passwd = request.form.get('password')
    passwdc = request.form.get('passwordc')

    gender = request.form.get('gender')
    birth = request.form.get('birth')
    nikname = request.form.get('nikname')

    print (
        'FName : ',name, '\n', 
        'LName : ',lastname, '\n',
        'email : ',email, '\n',
        'pass : ',passwd, '\n',
        'genre : ',gender, '\n',
        'b_day : ',birth, '\n',
        'pseudo : ',nikname, '\n'
    )
    #if request.method == 'POST':

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