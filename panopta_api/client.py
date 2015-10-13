from . import __version__
from os.path import join
from requests_toolbelt import user_agent
from urlparse import urljoin
import logging
import logging.handlers
import requests


class Client(object):
    LOG_INFO = logging.INFO
    LOG_DEBUG = logging.DEBUG

    VERBS = ('delete', 'get', 'post', 'put')

    def __init__(self, token, host='https://api2.panopta.com', version='2', log_level=LOG_INFO, log_path="."):
        self.session = requests.Session()
        self.session.auth = PanoptaAuth(token)
        self.session.headers.update({'Accept': 'application/json', 'User-Agent': user_agent(__package__, __version__)})
        self.base_url = urljoin(host, 'v' + version)

        logger = logging.getLogger()
        log_handler = logging.handlers.TimedRotatingFileHandler(join(log_path, __package__ + '.log'),
                                                                when='d',
                                                                interval=1,
                                                                backupCount=14)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(log_handler)
        logger.setLevel(log_level)
        logger.getChild(__package__).info(self.__class__.__name__ + ' initialized')

    def url(self, *path_parts):
        return '/'.join([self.base_url] + [part.strip('/') for part in path_parts])

    def __getattr__(self, name):
        if name in self.VERBS:
            def wrapper(url, *args, **kwargs):
                return getattr(self.session, name)(url, *args, **kwargs)
            return wrapper
        else:
            raise AttributeError(
                '{} does not support the "{}" HTTP verb'.format(self.__class__.__name__, name.upper())
            )


class PanoptaAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers.update({'Authorization': 'ApiKey %s' % self.token})

        return request
