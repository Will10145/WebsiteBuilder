from flask import *
from dotenv import load_dotenv
import os
from authfunctions import *

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template(
        'index.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        plantimg=url_for('static', filename='plant.png')
        )


@app.route('/login', methods=['POST', 'GET'])
def login():
    if('user' in session):
        return f"Hi, {session['user']}"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            login_email_password(email,password)
            session['user'] = email
        except:
            return 'Failed to login'

    return render_template(
        'login.html',
        styles=url_for('static', filename='login-style.css'),
        )

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
