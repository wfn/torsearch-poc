from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from tsweb.database import Base

class Descriptor(Base):
  __tablename__ = 'descriptors'
  descriptor = Column(String(40), primary_key=True)
  nickname = Column(String(19))
  address = Column(String(15))
  orport = Column(Integer)
  dirport = Column(Integer)
  fingerprint = Column(String(40))
  platform = Column(String(256))
  published = Column(DateTime)
  uptime = Column(BigInteger)
  extrainfo = Column(String(40))




class Entry(Base):
  __tablename__ = 'entry'
  id = Column(Integer, primary_key=True)
  title = Column(String(20), unique=False)
  text = Column(String(200), unique=False)

  def __init__(self, title=None, text=None):
    self.title = title
    self.text = text

  def __repr__(self):
    '<Entry %r>' % (self.title)
