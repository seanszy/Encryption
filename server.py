from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import csv
import uuid
import hashlib
import main

app = Flask(__name__)

exists = os.path.isfile("users.csv")

@app.route('/')
def index():
    if not exists:
        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['username', 'password', 'key'])
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.form['submit'] == 'Login':
        username = (request.form['username']).lower()
        password = request.form['password']
        if check_user_pass(username, password):
            key = get_user_key(username, password)
            a = main.decode_encypher(password, key)
            session['logged_in'] = True
            session['user'] = username
            return user()
        else:
            error = "Username or password is incorrect."
            return render_template('login.html', error = error)
    elif request.form['submit'] == 'Register':
        return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    error = None
    if request.form['submit'] == 'Back':
        return index()
    elif request.form['submit'] == 'Register':
        username = (request.form['username'].lower())
        password = request.form['password']
        if len(password) < 8:
            error = "Password must be at least 8 characters long."
            return render_template('register.html', error= error)
        if not check_user(username):
            key = main.create_encypher(password)
            write(username, password, key)
            return redirect('/')
        else:
            error = "Username is taken. Please try again."
            return render_template('register.html', error= error)


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


@app.route('/user', methods=['POST'])
def user():
    if not session['logged_in']:
        return redirect('/')
    username = session['user']
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username]
        for row in rows:
            website_list = row[3::2]
            password_list = row[4::2]
    return render_template('user.html', websites=website_list, passwords=password_list)


def write(username, password, key):
    password = hash_password(password)
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([username, password, key])


def check_user(username):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if username in row[0]:
                return(True)


def check_user_pass(username, password):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username]
        for row in rows:
            if check_password(row[1], password):
                return(True)
            else:
                return(False)


def get_user_key(username, password):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username]
        for row in rows:
            return(row[2])


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(db_password, user_password):
    password, salt = db_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
