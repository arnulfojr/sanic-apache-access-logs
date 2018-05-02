import sys


LOGGER_DEFAULT = {
    'level': 'INFO',
    'handlers': [],
    'propagate': True,
    'qualname': ''
}


HANDLER_TEMPLATE = {
    'class': 'logging.StreamHandler',
    'formatter': '',
    'stream': sys.stdout
}


LOGGING_CONFIG_DEFAULTS = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'common': {
            'format': '%(h)s %(l)s %(u)s %(asctime)s '
                      + '"%(m)s %(U)s%(q)s %(H)s" %(s)d %(b)d',
            'datefmt': '[%Y-%m-%d %H:%M:%S%z]',
            'class': 'logging.Formatter'
        },
        'combined': {
            'format': '%(h)s %(l)s %(u)s %(asctime)s '
                      + '"%(m)s %(U)s%(q)s %(H)s" %(s)d %(b)d'
                      + '"%(Referer)s" "%(User-Agent)s"',
            'datefmt': '[%Y-%m-%d %H:%M:%S%z]',
            'class': 'logging.Formatter'
        }
    }
)
