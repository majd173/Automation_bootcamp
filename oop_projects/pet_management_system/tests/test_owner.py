import unittest
from oop_projects.pet_management_system.src.utilities.config_provider import ConfigProvider
from oop_projects.pet_management_system.src.classes.owner import Owner



class TestOwner(unittest.TestCase):


    def setUp(self):
        self._config = ConfigProvider().load_from_file(r'/oop_projects\pet_management_system\pet_store.json')
        self._man = Owner('Man', 1234567890, [])
        self._man.add_owner()
    def test_owner(self):
        self.assertEqual(self._config['owners'][0]['name'], self._man.name)
