class Config(object):
  DEBUG = True
  ARCHIVE_DIR = '/home/kostas/priv/tordev/data/server-descriptors-2013-02'
  ARCHIVE_PERSISTENCE_FILE = '/home/kostas/priv/tordev/data/used_201302_desc_test'
  DATABASE_URL = 'postgres://<username>:<pwd>@localhost/<database>'

config = Config()
