from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email

class EmailForm(Form):
  email = EmailField(validators=[Email()])
