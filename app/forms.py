from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)

class SearchForm(Form):
    firstName = StringField('firstName')
    surname = StringField('surname')
    dob = StringField('dob')
    identifier = StringField('identifier')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
