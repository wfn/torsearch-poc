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

