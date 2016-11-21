import requests
from leanplum import exceptions


class Leanplum:
    """Access the Leanplum API. https://www.leanplum.com"""
    BASE_URL = 'https://www.leanplum.com/api'
    user_id = None
    device_id = None
    api_version = '1.0.6'

    _simple_url_template = '{base_url}?appId={app_id}&clientKey={client_key}&apiVersion={api_version}'

    def __init__(self, app_id, client_key, api_version=None, dev_mode=False):
        """Add your appId and clientKey. If you are using development key, set dev_mode=True.
        :param app_id: Your Leanplum appId.
        :param client_key: Your Leanplum clientKey (production or development).
        :param api_version: Leanplum API version to use defaults to 1.0.6. Should not need to change.
        :param dev_mode: Set to True to access the development environment. Defaults to False.
        """
        self.app_id = app_id
        self.client_key = client_key
        self.dev_mode = dev_mode
        if api_version is not None:
            self.api_version = api_version

    def set_user_id(self, user_id):
        """Set the current userId
        :param user_id: The userId you use to identify your users in Leanplum.
        """
        self.user_id = user_id

    def set_device_id(self, device_id):
        """Set the current deviceId.
        :param user_id: The deviceId you use to identify devices in Leanplum.
        """
        self.device_id = device_id

    def start(self, arguments=None):
        """Start a session. You must have called `set_user_id` or you must include `userId` in the arguments.
        :param arguments: See the Leanplum docs for arguments structure:
            https://www.leanplum.com/dashboard#/4510371447570432/help/setup/api.
        :return: The unwrapped response object from Leanplum.
        """
        if arguments is None:
            arguments = {}
        if self.user_id is None and arguments.get('userId') is None:
            raise Exception(exceptions.USER_ID_NEEDED_IN_ARGS)
        arguments.update({'action': 'start'})
        return self._request(arguments)[0]['response']

    def stop(self):
        return self._request({'action': 'stop'})[0]['response']

    def _request(self, request_body):
        """POST a request to the Leanplum Api.
        :param request_body: Request body as a dict.
        :return: The parsed JSON response.
        """
        return requests.post(
            self._get_url(),
            json=self._get_combined_arguments(request_body),
            headers=self._get_headers()
        ).json()

    def _get_url(self):
        """Create the request URL based on the current values of the class.
        :return: The request URL.
        """
        url_params = {
            'base_url': self.BASE_URL,
            'app_id': self.app_id,
            'client_key': self.client_key,
            'api_version': self.api_version
        }
        return self._simple_url_template.format(**url_params)

    def _get_combined_arguments(self, action_arguments):
        """Combine the action arguments with the default arguments from the class.
        :return: The combined default and action arguments.
        """
        default_arguments = dict()
        if self.dev_mode:
            default_arguments['devMode'] = True
        if self.user_id is not None:
            default_arguments['userId'] = self.user_id
        if self.device_id is not None:
            default_arguments['deviceId'] = self.device_id
        default_arguments.update(action_arguments)
        return default_arguments

    def _get_headers(self):
        """Get the request headers.
        :return: The request headers as a dict.
        """
        return {'Content-Type': 'application/json'}
