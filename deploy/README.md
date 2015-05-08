Steps to deploy:

  1. Create a virtualenv up in the root [home] directory
  1. Move into that 
  1. Copy `etd/` into the current directory
  1. `cp etd/etd.sample.ini etd/etd.ini` and fill with secret values
  1. Activate virtualenv and install dependencies:

      ```
      . bin/activate
      pip install -r etd/requirements.txt
      ```

  1. Move `passenger_wsgi.py` from `etd/deploy/` into this directory
  1. `touch tmp/restart.txt` to reboot passenger

Profit!
