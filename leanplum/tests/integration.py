import os

import unittest2

from leanplum.base import Leanplum

LEANPLUM_ENV_MESSAGE = 'Please make sure LEANPLUM_APP_ID, LEANPLUM_PRODUCTION_CLIENT_KEY, and ' \
                       'LEANPLUM_DEVELOPMENT_CLIENT_KEY are available as environmental variables. ' \
                       'Add LEANPLUM_TEST_MESSAGE_ID as well if you want a test message to be sent' \
                       'See README for details.'


class TestLeanplumIntegration(unittest2.TestCase):
    def setUp(self):
        self.api_id = os.environ.get('LEANPLUM_APP_ID')
        self.production_client_key = os.environ.get('LEANPLUM_PRODUCTION_CLIENT_KEY')
        self.development_client_key = os.environ.get('LEANPLUM_DEVELOPMENT_CLIENT_KEY')
        assert self.api_id is not None, LEANPLUM_ENV_MESSAGE
        assert self.production_client_key is not None, LEANPLUM_ENV_MESSAGE
        assert self.development_client_key is not None, LEANPLUM_ENV_MESSAGE

    def test_should_be_able_to_start_and_stop_session(self):
        lp = Leanplum(
            self.api_id,
            self.development_client_key,
            dev_mode=True
        )
        start_response = lp.start({'userId': 'test', 'deviceId': 'test'})
        self.assertTrue(start_response['success'])
        stop_response = lp.stop()
        self.assertTrue(stop_response['success'])

    def test_should_set_user_attributes_when_not_in_active_session(self):
        lp = Leanplum(
            self.api_id,
            self.development_client_key,
            dev_mode=True
        )
        lp.set_user_id('test')
        response = lp.set_user_attributes(
            {
                'userAttributes': {
                    'firstName': 'Test',
                    'lastName': 'User',
                    'gender': 'F',
                    'age': 21
                }
            }
        )

        self.assertTrue(response['success'])

    def test_should_track_events(self):
        lp = Leanplum(
            self.api_id,
            self.development_client_key,
            dev_mode=True
        )
        lp.start({'userId': 'test', 'deviceId': 'test'})
        track_response = lp.track('test event', {
            'value': 1,
            'info': 'This event was fired by running the automated test suite of leanplum-py',
            'params': {'gender': 'F', 'age': 21}
        })
        lp.stop()
        self.assertTrue(track_response['success'])

    def test_should_do_multi(self):
        lp = Leanplum(
            self.api_id,
            self.development_client_key,
            dev_mode=True
        )
        time = lp._get_current_timestamp()
        lp.set_device_id('test2')
        lp.set_user_id('test2')
        multi_response = lp.multi(
            [
                {'action': 'start', 'userId': 'test2', 'deviceId': 'test2', 'time': time - 5},
                {'action': 'track', 'event': 'test2', 'time': time - 3},
                {'action': 'stop', 'time': time}
            ]
        )
        self.assertTrue(multi_response['success'])

    def test_should_send_message(self):
        message_id = os.environ.get('LEANPLUM_TEST_MESSAGE_ID')
        self.assertIsNotNone(message_id)
        lp = Leanplum(
            self.api_id,
            self.production_client_key,
            dev_mode=False
        )
        send_message_response = lp.send_message(message_id, user_id='test')

        self.assertTrue(send_message_response['success'])
