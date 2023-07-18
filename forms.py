from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField , SubmitField , BooleanField 
from wtforms.validators import DataRequired , length , email_validator, EqualTo , Email 

class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirmpassword", validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    

    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField("password", validators=[DataRequired()])
    
    remember = BooleanField('remember me ')

    submit = SubmitField('Login')