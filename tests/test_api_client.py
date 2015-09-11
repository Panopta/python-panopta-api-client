from panopta_api import Client
import json
import unittest


class APIClientTest(unittest.TestCase):
    api_url = 'https://api2.panopta-testing.com'
    api_token = '7cee6cce-f3e7-412c-b219-20a623'
    version = '2'

    def setUp(self):
        self.client = Client(
            self.api_url,
            self.api_token,
            version=self.version,
            log_level=Client.LOG_DEBUG,
            log_path='./'
        )

    def test_getting_a_server(self):
        query_params = {'fqdn': 'panopta.com', 'limit': 10, 'offset': 0}
        results = self.client.get('/server', query_params=query_params)
        self.assertEqual(results['status_code'], '200')

    def test_creating_a_client(self):
        data = {'name': 'john', 'timezone': '%s/v%s/timezone/America/Chicago' % (self.api_url, self.version)}
        results = self.client.post('/contact', request_data=data)
        self.assertEqual(results['status_code'], '201')
