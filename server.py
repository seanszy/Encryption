from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import csv
import main

app = Flask(__name__)

exists = os.path.isfile("users.csv")

@app.route("/")
def index():
    if not exists:
        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('user.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['submit'] == 'Login':
        username = (request.form['username']).lower()
        password = request.form['password']
        if check_user_pass(username, password):
            # key = get_user_key(username, password)
            # a = main.decode_encypher(password, key)
            session['logged_in'] = True
            session['user'] = username
            return render_template('/')
        else:
            flash('Wrong Password')
    elif request.form['submit'] == 'Register':
        return render_template('register.html')
    return index()


@app.route('/register', methods=['POST'])
def register():
    username = (request.form['password'].lower())
    password = request.form['password']
    if not check_user(username):
        # key = main.create_encypher(password)
        # write(username, password, key)
        return redirect('/login')
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


@app.route('/user', methods=['POST'])
def user():
    if not session[logged_in]:
        return render_template('/')
    username = session['nickname']
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username]
        for row in rows:
            website_list = row
    return render_template('user.html', pages=website_list)



def write(username, password, key):
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
