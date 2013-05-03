from tsweb.database import db_session
from tsweb.models import Descriptor
from tsweb.logger import log

def search_for(expr):
  if not expr.strip():
    return []
  if '.' in expr:
    clause = Descriptor.address == expr
  elif len(expr) == 40:
    clause = Descriptor.descriptor == expr
  else:
    clause = Descriptor.nickname.like('%'+expr+'%')
  q = db_session.query(Descriptor).filter(clause)
  log('info', 'Result count for "%s": %d' % (expr, q.count()))
  return q.all()
