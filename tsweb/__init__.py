from __future__ import with_statement
from contextlib import closing
from tsweb.database import db_session, init_db
from flask import Flask

# TODO: move all config to a separate config.py and separate class

class Config(object):
  DEBUG = True
  ARCHIVE_DIR = '/home/kostas/priv/tordev/data/server-descriptors-2013-02'
  PERSISTENCE_FILE = '/home/kostas/priv/tordev/data/used_201302_desc_test'
  # database settings, etc. - move from database.py

config = Config()

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('TSWEB_SETTINGS', silent=True)

import tsweb.views

#init_db()

@app.teardown_request
def teardown_request(exception):
  db_session.remove()

