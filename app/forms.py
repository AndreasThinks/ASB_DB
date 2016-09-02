from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class SearchForm(Form):
    firstName = StringField('firstName')
    surname = StringField('surname')
    dob = StringField('dob')
    identifier = StringField('identifier')
