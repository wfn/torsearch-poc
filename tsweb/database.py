from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

uri = os.environ.get('DATABASE_URL', 'postgres://<postgres_username>:<password>@localhost/<database>')
engine = create_engine(uri)
db_session = scoped_session(sessionmaker(autocommit=False,
  autoflush=False,
  bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import tsweb.models
  Base.metadata.create_all(bind=engine)
