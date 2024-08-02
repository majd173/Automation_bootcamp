import json

import requests
from orange_hrm.api.config_provider import ConfigProvider
from orange_hrm.api.api_wrapper import ApiWrapper


class ApiMyInfoPage:

    CHANGE_EMPLOYEE_INFO = "api/v2/pim/employees/7/personal-details"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file(r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
            self._url = self._config['api_base_url']
        except ImportError:
            raise ImportError("Can not open orange_hrm.json file.")

    def change_employee_full_name(self):
        try:
            response = requests.request("PUT",
                                        self._url + self.CHANGE_EMPLOYEE_INFO,
                                        headers=self._config['employee_full_name_headers'],
                                        json=self._config['employee_full_name_body'])
            return response

        except requests.RequestException as e:
            raise ValueError(f'Put request has not been sent.: {e}')



