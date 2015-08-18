from httplib2 import Http
from urllib import urlencode
from os.path import join
import json
import socket
import logging
import logging.handlers

#-- Global data

LOG_INFO = logging.INFO
LOG_DEBUG = logging.DEBUG

#-- Api client

class api_client:
    def __init__(self, api_base_url,
                       api_token,
                       version="2",
                       log_level=LOG_INFO,
                       log_path="."):

        self.api_base_url = api_base_url
        self.api_token = api_token
        self.version = version
        self.log_level = log_level
        self.log_path = log_path

        self._setup()

    def _setup(self):
        self._setup_api()
        self._setup_logging()

    def _setup_api(self):
        self.api_base = "%s/v%s" % (self.api_base_url.strip("/"), self.version)
        self.headers = {
            'Authorization': 'ApiKey %s' % self.api_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        } 

    def _setup_logging(self):
        self.logger = logging.getLogger('Panopta API')

        logHandler = logging.handlers.TimedRotatingFileHandler(join(self.log_path, "panopta_api.log"), when='d', interval=1, backupCount=14)
        logHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(logHandler)
        self.logger.setLevel(self.log_level)

    def _get_response(self, status_code, status_reason, content, headers):
        if not headers:
            headers = {"status": status_code}

        return {
            'status_code': status_code,
            'status_reason': status_reason,
            'response_data': content or {},
            'response_headers': headers
        }

    def _request(self, resource_uri, method, data, headers):
        resource_path = ("%s/%s" % (self.api_base, resource_uri.strip("/"))).strip("?")
        headers.update(self.headers)

        #-- Send request

        self.logger.info('%s %s' % (method, resource_path))  

        try:
            resp, content = Http().request(uri=resource_path, method=method, body=data, headers=headers)
        except Exception, err:
            self.logger.error(str(err))  
            return self._get_response("0", str(err), None, None)

        try: content = json.loads(content)
        except: content = {}

        #-- Log request

        try: data = json.loads(data)
        except: data = {}

        log_data = {
            'resource_path': resource_path,
            'method': method,
            'request_headers': headers,
            'request_data': data,
            'response_headers': resp,
            'response_body': content
        }
        self.logger.debug(json.dumps(log_data, indent=2, sort_keys=True))

        #-- Prepare result

        status_code = resp['status']
        if status_code in ['200', '201', '204']:
            status_reason = 'success'
        else:
            reason = resp.get('errormessage', None)
            if reason: 
                status_reason = 'error: %s' % reason
            else:
                status_reason = 'error' 

        return self._get_response(status_code, status_reason, content, resp)
       
    def get(self, resource_uri, query_params={}, headers={}):
        return self._request("%s?%s" % (resource_uri, urlencode(query_params)), "GET", None, headers)

    def post(self, resource_uri, request_data={}, headers={}):
        return self._request(resource_uri, "POST", json.dumps(request_data), headers)

    def put(self, resource_uri, request_data={}, headers={}):
        return self._request(resource_uri, "PUT", json.dumps(request_data), headers)

    def delete(self, resource_uri, headers={}):
        return self._request(resource_uri, "DELETE", None, headers)
