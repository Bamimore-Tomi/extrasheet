from flask import Flask,Blueprint, render_template
from flask_login import login_required
from . import db 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('preview.html')

@main.route('/home/')
@login_required 
def home():
    return render_template('AfterSign.html')