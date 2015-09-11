from panopta_api import Client
from urlparse import urljoin
import json
import unittest


class APIClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(
            'fake-api-key',
            log_level=Client.LOG_DEBUG,
            log_path='/tmp/'
        )

    def test_getting_a_server(self):
        query_params = {'fqdn': 'panopta.com', 'limit': 10, 'offset': 0}
        results = self.client.get('/server', query_params=query_params)
        self.assertEqual(results['status_code'], '200')

    def test_creating_a_client(self):
        data = {'name': 'john', 'timezone': urljoin(self.client.base_url, 'America/Chicago')}
        results = self.client.post('/contact', request_data=data)
        self.assertEqual(results['status_code'], '201')
