import requests_mock
import unittest2

from leanplum import Leanplum


@requests_mock.mock()
class TestLeanplum(unittest2.TestCase):
    url = 'https://www.leanplum.com/api?appId=APP_ID&clientKey=CLIENT_KEY&apiVersion=1.0.6'

    def setUp(self):
        self.lp = Leanplum(
            app_id='APP_ID',
            client_key='CLIENT_KEY'
        )

    def test_should_start_successfully_if_user_id_is_in_args(self, mock_requests):
        mock_requests.post(self.url, json=[{'response': {'success': True}}])
        response = self.lp.start({'userId': 1, 'deviceName': 'test'})
        self.assertTrue(response.get('success'))

    def test_should_start_successfully_if_user_id_is_set_before_start(self, mock_requests):
        mock_requests.post(self.url, json=[{'response': {'success': True}}])
        self.lp.set_user_id(1)
        response = self.lp.start({'deviceName': 'test'})
        self.assertTrue(response.get('success'))

    def test_should_raise_exception_if_user_id_is_not_set(self, mock_requests):
        mock_requests.post(self.url, json=[{'response': {'success': True}}])
        self.assertRaises(Exception, self.lp.start, args={'deviceName': 'test'})
