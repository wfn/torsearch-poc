# a (working) stub, to be later made to be run via crontab.

from tsweb.config import config
from tsweb.importer import import_descriptors
import_descriptors(config.ARCHIVE_DIR, config.ARCHIVE_PERSISTENCE_FILE)
