from __future__ import with_statement
from contextlib import closing
from tsweb.database import db_session, init_db
from tsweb.config import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('TSWEB_SETTINGS', silent=True)

import tsweb.views

#init_db()

@app.teardown_request
def teardown_request(exception):
  db_session.remove()

