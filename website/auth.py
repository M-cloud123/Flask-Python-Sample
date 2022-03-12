from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = None

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName or lastName or username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != confirmPassword:
            flash('Passwords do not match.', category='error')
        elif len(password) < 4:
            flash('Password must be at least 3 characters.', category='error')
        else:
            flash('Account successfully created!', category='error')

    return render_template("sign_up.html")
