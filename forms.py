from flask_wtf import FlaskForm
from wtforms import (StringField, TextField, SubmitField, PasswordField, DateField, SelectField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo, URL)



class RegistrationForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address')), DataRequired()])
    password = PasswordField('Password', [DataRequired("Please enter a password.")])
    confirmPassword = PasswordField('Repeat Password', [EqualTo(password, message='Passwords must match')])
    address_1 = StringField('Address_1', [DataRequired()])
    address_2 = StringField('Address_2', [DataRequired()])
    phone_number = StringField('Phone_Number', [DataRequired()])
    


class CommentsForm(FlaskForm):
    author = StringField('Author', [DataRequired()])
    comment = TextField('Comment', [DataRequired()])
    submit = SubmitField('Submit')
