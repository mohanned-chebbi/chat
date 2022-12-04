from flask import Flask, render_template , request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello'

@app.route('/signup')
def signup():
    v="hodhod"
    return render_template ('signup.html',h=v)

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