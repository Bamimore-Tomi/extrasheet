from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email,Regexp, EqualTo
from wtforms import ValidationError
from .models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 100),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
class RegisterForm(FlaskForm):
    first_name = StringField('FirstName', validators=[DataRequired(), Length(1,100), 
                                                  Regexp(r"^[a-zA-Z ,.'-]+$", 0, 'Firstname must have only letters, dots or underscores')])
    last_name = StringField('LastName', validators=[DataRequired(), Length(1,100), 
                                                  Regexp(r"^[a-zA-Z ,.'-]+$", 0, 'Lastname must have only letters, dots or underscores')])
    email = StringField('Email', validators=[DataRequired(), Length(1, 100),Email()])
    phone_number = StringField('PhoneNumber' ,validators=[DataRequired(),
                                                         Regexp(r'(^[0]\d{10}$)|(^[\+]?[234]\d{12}$)',0, 'Enter a valid Phone Number e.g +2348012345678 or 08012345678')])
    gender = StringField('Gender', validators=[DataRequired(),
                                               Regexp(r'male|female',0,'Invalid Entry')])
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d')
    password1 = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')