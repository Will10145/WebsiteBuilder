import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()

config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "projectId": os.getenv("projectId"),
    "storageBucket": os.getenv("storageBucket"),
    "messagingSenderId": os.getenv("messagingSenderId"),
    "appId": os.getenv("appId"),
    "measurementId": os.getenv("measurementId"),
    "databaseURL": ''
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def login_email_password(email,password):
    user = auth.sign_in_with_email_and_password(email,password)
    return user

def send_password_reset(email):
    auth.send_password_reset_email(email)
    return 'sent'

def create_account_email_password(email,password):
    user = auth.create_user_with_email_and_password(email, password)
    return user

def get_session_info(token):
    return auth.get_account_info(token)
#user = auth.create_user_with_email_and_password(email, password)
#print(user)

#user = auth.sign_in_with_email_and_password(email,password)
#info = auth.get_account_info(user['idToken'])
#print(info)


#auth.send_email_verification(user['idToken'])

#auth.send_password_reset_email(email)

if __name__ == '__main__':
    print('Do not run this script directly!')