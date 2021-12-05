from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from Weather_app.models import User
from flask_login import current_user
from flask_wtf.file import FileField

class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message="Passwords Change")])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Username already Exists")

    def valitade_username(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("Email already Registered")

class UpdateForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture')
    submit = SubmitField()

    def validate_email(self,email):
        if email.data!=current_user.email:
            if User.query.filter_by(email=self.email.data).first():
                raise ValidationError("Email Already Registred")

    def validate_username(self,username):
        if username.data!=current_user.username:
            if User.query.filter_by(username=self.username.data).first():
                raise ValidationError("Username is not availabel")
