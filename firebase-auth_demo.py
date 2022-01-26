import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from getpass import getpass

cred = credentials.Certificate(r'C:\Users\mohit\pythonlogin\authpython-b780b-firebase-adminsdk-afy6c-42b9599723.json')

firebase_admin.initialize_app(cred)

firebaseConfig = {'apiKey': "AIzaSyBgXyDzMyO2EG3n1FhUDp9m9uacnnHlf6Y",
    'authDomain': "authpython-b780b.firebaseapp.com",
    'databaseURL': "https://authpython-b780b-default-rtdb.firebaseio.com",
    'projectId': "authpython-b780b",
    'storageBucket': "authpython-b780b.appspot.com",
    'messagingSenderId': "1069385851702",
    'appId': "1:1069385851702:web:20f836eec9f06a37d64997",
    'measurementId': "G-3PRDVNJYRP"}

firebase = pyrebase.initialize_app(firebaseConfig)




def signUp():
    print("Signing Up...")
    email = input("Enter Email: ")
    password = getpass("Enter Password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        auth.send_email_verification(user['idToken'])
        print('email verification link send')
        print("New Account Created!")
        ask = input("Do you want to Login now?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already Exists")
        ask = input("Log in?[y/n]")
        if ask == 'y':
            login()
            

        
def signupUsingId():
    email = input("Enter Email: ")
    id = input("Enter username: ")
    password = getpass("Enter Password: ")
    user = auth.create_user(uid = id, email = email, password = password)
    print("successfully created user :{0} ".format(user.uid))
    auth.generate_password_reset_link(email, action_code_settings)
    print('Email verification link send')
        
    
def login():
    auth = firebase.auth()
    print("Logging In...")
    email = input("Enter Email: ")
    password =getpass("Enter Password: ")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        print("Successfully Logged In")
        userInfo = auth.get_account_info(login['idToken'])
        user = userInfo['users']
        userId = []
        for value in user:
            userId.append(value['localId'])
        print(userId)
    
    except:
        print("Invalid Password")
        ask = input("do you want to reset password?[y/n]")
        if ask == 'y':
            auth.send_password_reset_email(email)
            print('Reset password link send')
   
    
ans=input("Are you a new user[y/n]")
if ans =='y':
    signupUsingId()
elif ans =='n':
    login()