from flask import *
from dotenv import load_dotenv
import os
from authfunctions import *
import json

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    if('token' in session):
        data = get_session_info(session['token'])
        email = data['users'][0]['email']
        return render_template(
            'index.html',
            styles=url_for('static', filename='tailwindstyles.css'),
            plantimg=url_for('static', filename='plant.png'),
            loggedin=True,
            email=email
        )
    else:
        return render_template(
            'index.html',
            styles=url_for('static', filename='tailwindstyles.css'),
            plantimg=url_for('static', filename='plant.png'),
            loggedin=False
        )
    


@app.route('/login', methods=['POST', 'GET'])
def login():
    if('token' in session):
        return redirect('/')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = login_email_password(email,password)
            session['token'] = user['idToken']
            return redirect('/')
        except:
            return render_template(
        'login.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        error='Error logging in!'
        )

    return render_template(
        'login.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        )

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if('token' in session):
        return redirect('/')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = create_account_email_password(email,password)
            session['token'] = user['idToken']
            return redirect('/')
        except:
            return render_template(
        'signup.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        error='Error signing up!'
        )

    return render_template(
        'signup.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        )

@app.route('/logout')
def logout():
    if('token' in session):
        session.pop('token')
    return redirect('/')

@app.route('/resetpassword', methods=['POST', 'GET'])
def resetpassword():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            send_password_reset(email)
            return render_template(
        'resetpassword.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        success=True
        )
        except:
            return render_template(
        'resetpassword.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        error='Error sending email!'
        )

    if('token' in session):
        redirect('/')
    else:
        return render_template(
        'resetpassword.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        )

if __name__ == '__main__':
    app.run(debug=True, port=4444)
