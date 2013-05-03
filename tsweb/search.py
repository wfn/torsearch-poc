from tsweb.database import db_session
from tsweb.models import Descriptor
from tsweb.logger import log

from flask import request
from datetime import datetime

def search_for(expr):
  if not expr.strip():
    return []
  if expr.startswith('$'):
    clause = Descriptor.fingerprint == expr[1:]
  elif '.' in expr:
    clause = Descriptor.address == expr
  elif len(expr) == 40:
    clause = Descriptor.descriptor == expr
  else:
    clause = Descriptor.nickname.like('%'+expr+'%')
  q = db_session.query(Descriptor).filter(clause)
  if request.values.get('trydate'):
    q = q.filter(Descriptor.published > datetime(2013, 2, 5, 0, 0, 0, 0)).\
          filter(Descriptor.published < datetime(2013, 2, 25, 0, 0, 0, 0))
  log('info', 'Result count for "%s": %d' % (expr, q.count()))
  return q.all()
