
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User
from .forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()
    errors = {}
    if request.method=='POST':
        form = LoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user !=None and user.check_password(form.password.data):
                login_user(user,True)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.home')
                return redirect(next)
            errors = form.errors.copy()
            errors['invalid']='Invalid login credentials'
        errors['invalid']='Invalid login credentials '
    return render_template('login.html',errors=errors)

@auth.route('/register/',  methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.form)
        if form.validate():
            user = User(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                phone_number = form.phone_number.data,
                gender = form.gender.data,
                date_of_birth = form.date_of_birth.data,
                password = form.password1.data               
            )
            db.session.add(user)
            db.session.commit()
            login_user(user,True)
            return redirect(url_for('main.home'))
        else:
            print(form.errors)
    return render_template('registration.html', errors=form.errors)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))