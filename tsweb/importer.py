from tsweb.database import db_session
from tsweb.models import Descriptor
from tsweb.logger import log
from stem.descriptor.reader import DescriptorReader
import gc

def import_descriptors(wherefrom, persistence_file):
  if not gc.isenabled():
    gc.enable()

  reader = DescriptorReader(wherefrom, persistence_path=persistence_file)
  log('info', 'recalled %d files processed from my source(s) provided' % len(reader.get_processed_files()))
  with reader:
    i = 0
    for i, desc in enumerate(reader): # 'enumerate' might be memory-inefficient here
      desc_model = Descriptor(
        descriptor=desc._path.split('/')[-1], # do we have to be so ugly, though?
        nickname=desc.nickname,
        address=desc.address,
        orport=desc.or_port,
        dirport=desc.dir_port,
        fingerprint=desc.fingerprint,
        platform=desc.platform,
        published=desc.published,
        uptime=desc.uptime)
      db_session.add(desc_model)
      if (i+1) % 100000 == 0: # total could be e.g. 323715 descriptors
                              # (find ../../data/server-descriptors-2013-02 -type f | wc -l)
        print 'committing..',
        db_session.commit() # committed ORM objects can be garbage collected, which is important
                            # when dealing with these amounts of rows
        print 'done. collecting garbage..',
        gc.collect()
        print 'done.'
  log('info', 'iterated over %d files' % i)
  db_session.commit()


