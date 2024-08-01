import unittest
from orange_hrm.api.api_wrapper import ApiWrapper
from orange_hrm.api.config_provider import ConfigProvider

class TestOrangeHrm(unittest.TestCase):

    def setUp(self):
        self._api = ApiWrapper()
        self._config = ConfigProvider().load_from_file('../orange_hrm.json')



if __name__ == '__main__':
    unittest.main()
