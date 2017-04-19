from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import csv
import uuid
import hashlib
import main
import RSA_Encryption_New
import gmail

app = Flask(__name__)

exists = os.path.isfile("users.csv")

@app.route('/')
def index():
    if not exists:
        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['username', 'password', 'email', 'key'])
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.form['submit'] == 'Login':
        username = (request.form['username']).lower()
        password = request.form['password']
        if check_user_pass(username, password):
            email = get_email(username)
            print(email)
            session['2_factor'] = gmail.send_2_factor(email)
            key = get_user_key(username)
            primes = main.decode_encypher(password, key)
            session['p'] = primes[0]
            session['q'] = primes[1]
            session['logged_in'] = True
            session['user'] = username
            return render_template('2_factor.html')
        else:
            error = "Username or password is incorrect."
            return render_template('login.html', error = error)
    elif request.form['submit'] == 'Register':
        return render_template('register.html')
    elif request.form['submit'] == 'Back':
            return index()
    elif request.form['submit'] == 'Continue':
        code = (request.form['code'])
        if int(code) == int(session['2_factor']):
            return user()
        else:
            error = "Your entered code is incorrect."
            return render_template('2_factor.html', error = error)


@app.route('/register', methods=['POST'])
def register():
    error = None
    if request.form['submit'] == 'Back':
        return index()
    elif request.form['submit'] == 'Register':
        username = (request.form['username'].lower())
        email = request.form['email']
        password = request.form['password']
        if len(password) < 8:
            error = "Password must be at least 8 characters long."
            return render_template('register.html', error= error)
        if not check_user(username, email):
            key = main.create_encypher(password)
            write(username, password, email, key)
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
    if request.form['submit'] == 'Add Website':
        return render_template("add_site.html")
    elif request.form['submit'] == 'Logout':
        return logout()
    else:
        username = session['user']
        with open('users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            rows = [row for row in reader if row[0] == username or row[2] == username]
            password_list_d = []
            for row in rows:
                website_list = row[4::2]
                password_list = row[5::2]
                print(password_list)
                for password in password_list:
                    password_list_d.append(RSA_Encryption_New.decrypt(session['p'], session['q'], password))
        return render_template('user.html', websites=website_list, passwords=password_list_d)


@app.route('/add_site', methods=['POST'])
def add_site():
    if not session['logged_in']:
        return redirect('/')
    error = None
    if request.form['submit'] == 'Back':
        return user()
    elif request.form['submit'] == 'Add Website':
        website = request.form['website']
        password = request.form['password']
        username = session['user']
        with open('users.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            all_rows = [row for row in reader]

        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i, row in enumerate(all_rows):
                if row[0] == username or row[2] == username:
                    print(row)
                    row.append(website)
                    password = RSA_Encryption_New.encrypt(session['p'], session['q'], password)
                    row.append(password)
                    print(row)
                    all_rows[i] = row
            writer.writerows(all_rows)
        return user()


def write(username, password, email, key):
    password = hash_password(password)
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([username, password, email, key])


def check_user(username, email):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if username in row[0] or email in row[2]:
                return(True)


def check_user_pass(username, password):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username or row[2] == username]
        for row in rows:
            if check_password(row[1], password):
                return(True)
            else:
                return(False)


def get_user_key(username):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username or row[2] == username]
        for row in rows:
            return(row[3])


def get_email(username):
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row for row in reader if row[0] == username or row[2] == username]
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
