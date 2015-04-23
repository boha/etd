from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Email

from models import Subscription
from validators import Unique


class EmailForm(Form):
    email = EmailField(validators=[
        Required(),
        Email(),
        Unique(Subscription, Subscription.email, message=u"This email is already subscribed")
    ])
