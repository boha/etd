# Flask
from flask import Flask, render_template, request, redirect, url_for

# Meta
from database import init_db, db_session

# Forms
from flask_wtf.csrf import CsrfProtect
from forms import EmailForm

# Persistence
from models import Subscription

## Setup

app = Flask(__name__)
app.secret_key = "asd252rg242tqwf5y6h4wefefa"
CsrfProtect(app)
init_db()


## Routes

@app.route('/')
def index():
  email_form = EmailForm()
  return render_template('index.html', email_form=email_form)

@app.route('/subscribe', methods=['POST'])
def subscribe():
  # TODO: conditional on method?
  # TODO: fill with form data?
  email_form = EmailForm()

  mime_type = request.mimetype
  # json
  if mime_type == 'application/json':
    return 'ok'
  # html
  else:
    # Form submission
    if email_form.validate_on_submit():
      sub = Subscription(email_form.email.data)
      db_session.add(sub)
      db_session.commit()

    # TODO: flash message?
    return redirect(url_for('index'))


## Main runtime

if __name__ == '__main__':
  app.debug = True # not for production
  app.run()


## Meta

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
