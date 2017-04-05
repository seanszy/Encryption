from flask import Flask, render_template, request, redirect
import hashlib
import uuid
import csv
import os.path
import main

app = Flask(__name__)

exists = os.path.isfile("users.csv")

@app.route('/')
def index():
    if not exists:
        with open('users.csv', 'a') as csvfile:
            fieldnames = ['username', 'password', 'key']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    return render_template('index.html')


@app.route('/loginreg', methods=['POST'])
def pick():
    if request.form['loginreg'] == 'Login':
        return render_template('login.html')
    elif request.form['loginreg'] == 'Register':
        return render_template('signup.html')
    else:
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    error = None
    username = (request.form['username']).lower()
    password = request.form['password']
    if check_user_pass(username, password):
        key = get_user_key(username, password)
        a = main.decode_encypher(password, key)
        print(a)
        return render_template('user.html', user = username)
    else:
        error = "Username or password is incorrect. Please try again."
        return render_template('login.html', error = error)


@app.route('/signup', methods=['POST'])
def signup():
    error = None
    username = (request.form['username']).lower()
    password = request.form['password']
    if not check_user(username):
        key = main.create_encypher(password)
        write(username, password, key)
        return redirect('/')
    else:
        error = "Username is taken. Please try again."
        return render_template('signup.html', error = error)


def write(username, password, key):
    with open('users.csv', 'a') as csvfile:
        fieldnames = ['username', 'password', 'key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': username, 'password': hash_password(password), 'key': key})


def check_user(username):
    with open('users.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if username in row['username']:
                return(True)


def check_user_pass(username, password):
    with open('users.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader if row['username'] == username]
        for row in rows:
            if check_password(row['password'], password):
                return(True)
            else:
                return(False)


def get_user_key(username, password):
    with open('users.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader if row['username'] == username]
        for row in rows:
            return(row['key'])


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(db_password, user_password):
    password, salt = db_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    app.run()
