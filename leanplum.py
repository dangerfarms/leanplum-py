import requests
import exceptions


class Leanplum:
    BASE_URL = 'https://www.leanplum.com/api'
    user_id = None
    device_id = None
    api_version = '1.0.6'

    _simple_url_template = '{base_url}?appId={app_id}&clientKey={client_key}&apiVersion={api_version}'

    def __init__(self, app_id, client_key, api_version=None, dev_mode=False):
        self.app_id = app_id
        self.client_key = client_key
        self.dev_mode = dev_mode
        if api_version is not None:
            self.api_version = api_version

    def set_dev_mode(self, dev_mode=True):
        self.dev_mode = dev_mode

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_device_id(self, device_id):
        self.device_id = device_id

    def start(self, arguments=None):
        """
        See the docs for arguments structure: https://www.leanplum.com/dashboard#/4510371447570432/help/setup/api
        :param arguments:
        :return:
        """
        if arguments is None:
            arguments = {}
        if self.user_id is None and arguments.get('userId') is None:
            raise Exception(exceptions.USER_ID_NEEDED_IN_ARGS)
        arguments.update({'action': 'start'})
        return self._request(arguments)[0]['response']

    def _request(self, arguments):
        return requests.post(
            self._get_url(),
            json=self._get_combined_arguments(arguments),
            headers=self._get_headers()
        ).json()

    def _get_url(self):
        url_params = {
            'base_url': self.BASE_URL,
            'app_id': self.app_id,
            'client_key': self.client_key,
            'api_version': self.api_version
        }
        return self._simple_url_template.format(**url_params)

    def _get_combined_arguments(self, arguments):
        default_arguments = dict()
        if self.dev_mode:
            default_arguments['devMode'] = True
        if self.user_id is not None:
            default_arguments['userId'] = self.user_id
        if self.device_id is not None:
            default_arguments['deviceId'] = self.device_id
        default_arguments.update(arguments)
        return default_arguments

    def _get_headers(self):
        return {'Content-Type': 'application/json'}
