LOG_LEVELS = '*' 

import inspect

def log(level, msg):
  """Placeholder logger stub, simply prints out the message and where it came from
  """
  if LOG_LEVELS != '*' and level not in LOG_LEVELS:
    return
  frame, filename, line_number, function_name, lines, index =\
    inspect.getouterframes(inspect.currentframe())[1]
  s = inspect.stack()
  print '[%s] (%s->%s, line %d):' % (level, inspect.getmodule(s[1][0]).__name__, function_name, line_number), msg
