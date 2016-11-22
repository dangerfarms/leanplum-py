import logging

import requests_mock
import unittest2

from leanplum.base import Leanplum

logger = logging.getLogger()
logger.level = logging.ERROR


@requests_mock.mock()
class TestLeanplumStart(unittest2.TestCase):
    url = 'https://www.leanplum.com/api?appId=APP_ID&clientKey=CLIENT_KEY&apiVersion=1.0.6'

    def setUp(self):
        self.lp = Leanplum(
            app_id='APP_ID',
            client_key='CLIENT_KEY'
        )

    def test_should_start_successfully_if_user_id_is_in_args(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        response = self.lp.start({'userId': 1, 'deviceName': 'test'})
        self.assertTrue(response.get('success'))

    def test_should_start_successfully_if_user_id_is_set_before_start(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        self.lp.set_user_id(1)
        response = self.lp.start({'deviceName': 'test'})
        self.assertTrue(response.get('success'))

    def test_should_raise_exception_if_user_id_is_not_set(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        self.assertRaises(Exception, self.lp.start, args={'deviceName': 'test'})

    def test_should_set_user_id_in_class_if_provided_in_start(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        self.assertIsNone(self.lp.user_id)
        self.lp.start({'userId': 1})
        self.assertEqual(self.lp.user_id, 1)

    def test_should_set_device_id_in_class_if_provided_in_start(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        self.assertIsNone(self.lp.device_id)
        self.lp.start({'userId': 1, 'deviceId': 1})
        self.assertEqual(self.lp.device_id, 1)


@requests_mock.mock()
class TestLeanplumStop(unittest2.TestCase):
    url = 'https://www.leanplum.com/api?appId=APP_ID&clientKey=CLIENT_KEY&apiVersion=1.0.6'

    def setUp(self):
        self.lp = Leanplum(
            app_id='APP_ID',
            client_key='CLIENT_KEY'
        )

    def test_should_start_successfully_if_user_id_is_in_args(self, mock_requests):
        mock_requests.post(self.url, json={'response': [{'success': True}]})
        response = self.lp.stop()
        self.assertTrue(response.get('success'))
