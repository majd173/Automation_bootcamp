import unittest

from object_oriented_programing.pet_management_system.infra.config_provider import ConfigProvider
from object_oriented_programing.pet_management_system.owner import Owner



class TestOwner(unittest.TestCase):


    def setUp(self):
        self._config = ConfigProvider().load_from_file(
            r'C:\Users\Admin\Desktop\Automation_bootcamp\object_oriented_programing\pet_management_system\pet_store_management.json')

    def test_owner(self):
        owner = Owner('Man', 123456789, [])
        self.assertEqual(self._config['owners'][0]['name'], owner.name)