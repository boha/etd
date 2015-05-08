## Requirements

* Python
* `easy_install`
* `virtualenv`

Subsequently:

* Flask

## Getting Started

Go get `easy_install`. Create a virtual environment and get into it.

      sudo easy_install virtualenv
      virtualenv venv
      . venv/bin/activate

Rad. Install depedencies.

    pip install -r requirements.txt

You will need a database called `earntheday`. Once you've made that, copy `etd.sample.ini` to `etd.ini` and fill with appropriate values.

As the great philosopher Edan once said, "Run That Shit":

    python application.py

Load [http://localhost:5000](http://localhost:5000)
