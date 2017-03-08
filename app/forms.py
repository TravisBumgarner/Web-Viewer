from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from .models import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1,64),
                                             Email()])
    visit_select = SelectField('visit_select',
                                 choices=[(None, ''), ('theft','Theft'),('reason','Other Reason')],
                                 validators=[DataRequired()]
                                 )
    visit_description = TextAreaField('visit_description', validators=[DataRequired()])

class RegistrationForm(Form):
    name = StringField('Name', validators=[DataRequired(),
                                           Length(1, 64),
                                           Regexp('^[A-Za-z][A-Za-z_.]*$', 0, "First Name, Last Name, and Underscores/periods only")
                                           ])
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1,64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2', message="Passwords do not match.")])
    password2 = PasswordField('Confirm Password', validators= [DataRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


