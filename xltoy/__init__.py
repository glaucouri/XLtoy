import logging

__version__ = 0.1
version = __version__

default_log_name = 'xltoy'
default_log_level = logging.DEBUG
#default_log_format = logging.Formatter('%(asctime)s %(levelname).3s %(name)s %(message)s')
default_log_format = logging.Formatter('%(levelname).3s %(message)s')



log = logging.getLogger(default_log_name)
log.setLevel(default_log_level)

str_log = logging.StreamHandler()
str_log.setFormatter(default_log_format)

log.addHandler(str_log)


