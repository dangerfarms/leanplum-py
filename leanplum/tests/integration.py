import os

import time
import unittest2

from leanplum.base import Leanplum

LEANPLUM_ENV_MESSAGE = 'Please make sure LEANPLUM_APP_ID, LEANPLUM_PRODUCTION_CLIENT_KEY, and ' \
                       'LEANPLUM_DEVELOPMENT_CLIENT_KEY are available as environmental variables. ' \
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
