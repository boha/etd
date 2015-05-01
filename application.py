from datetime import datetime

# Flask
from flask import Flask, render_template, request, redirect, url_for, flash

# Meta
from database import init_db, db_session

# Forms
from flask_wtf.csrf import CsrfProtect
from forms import EmailForm

# Persistence
from werkzeug.contrib.cache import SimpleCache
from models import Subscription

## Setup

from config import settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
CsrfProtect(app)
init_db()
cache = SimpleCache()


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

        flash("Thanks! You've been subscribed.")
        return redirect(url_for('index'))


@app.route('/subscriptions/generate')
def generate_subscriptions():
    """Write a CSV to disk for fetching via FTP, but cache
       a timer to make sure it doesn't get hammered."""

    CSV_TIMEOUT = 1 * 60  # in seconds
    CSV_FILE = '../subscriptions.csv'

    # Only allow this to run once every minute
    last_update_at = cache.get('LAST_CSV_UPDATE')
    if (last_update_at is None):
        cache.set('LAST_CSV_UPDATE', datetime.now(), timeout=CSV_TIMEOUT)
    else:
        return redirect(url_for('index'))  # no error message, deliberately

    import csv
    outfile = open(CSV_FILE, 'wb')
    outcsv = csv.writer(outfile)

    cols = {
        'created_at': 'Date Subscribed (UTC)',
        'email':      'Email Address',
    }
    subscriptions = Subscription.query.order_by(Subscription.created_at).all()

    outcsv.writerow(cols.values())
    [outcsv.writerow([getattr(curr, col) for col in cols.keys()]) for curr in subscriptions]
    outfile.close()

    flash("Generated.")
    return redirect(url_for('index'))

## Main runtime

if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.run()


## Meta

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
