from panopta_api import Client
import unittest


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client('fake-api-key',
                             host='http://api2.panopta-testing.com',
                             version='test',
                             log_level=Client.LOG_DEBUG,
                             log_path='/tmp/')

    def test_url(self):
        full_url = 'http://api2.panopta-testing.com/vtest/collection/id/resource'
        self.assertEqual(full_url, self.client.url('/collection/id/resource/'))
        self.assertEqual(full_url, self.client.url('collection', 'id', 'resource'))

    def test_request_authorization(self):
        response = self.client.session.head(self.client.url())
        self.assertTrue('Authorization' in response.request.headers)

    def test_request_content_type(self):
        response = self.client.session.post(self.client.url(), json={}, verify=False)
        self.assertTrue('Content-Type' in response.request.headers)
        self.assertEquals('application/json', response.request.headers.get('Content-Type'))

    def test_verbs(self):
        for verb in ['DELETE', 'GET', 'POST', 'PUT']:
            self.assertTrue(hasattr(self.client, verb.lower()))

        for verb in ['CONNECT', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE']:
            with self.assertRaises(AttributeError):
                getattr(self.client, verb.lower())(self.client.url())
