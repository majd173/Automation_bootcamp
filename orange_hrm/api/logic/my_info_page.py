import requests
import logging
#-----------------------------API CLASSES----------------------------
from orange_hrm.api.infra.config_provider import ConfigProvider
from orange_hrm.api.infra.api_wrapper import ApiWrapper


class ApiMyInfoPage:
    """
    API class for My Info page.
    """

    CHANGE_EMPLOYEE_INFO = "api/v2/pim/employees/7/personal-details"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file(
                r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
            self._url = self._config['api_base_url']
        except ImportError:
            logging.error("Can not open orange_hrm.json file.")

    #--------------------------------------------------------------------------------

    def change_employee_full_name(self):
        """
        This function is used to change employee full name.
        """
        try:
            logging.info("Sending a put request to change employee full name.")
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_INFO}',
                self._config['employee_new_name_headers'],
                self._config['employee_new_name_body'])
            return response

        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    #--------------------------------------------------------------------------------
    def retrieve_employee_full_name(self):
        """
        This function is used to retrieve employee full name.
        """
        try:
            logging.info("Sending a put request to retrieve employee full name.")
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_INFO}',
                self._config['employee_retrieve_name_headers'],
                self._config['employee_retrieve_name_body'])
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')
