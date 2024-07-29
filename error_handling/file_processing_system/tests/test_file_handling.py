import unittest

from error_handling.file_processing_system.custom_exceptions import CustomException
from error_handling.file_processing_system.file_processing_system import FileProcessingSystem
from error_handling.file_processing_system.config_provider import ConfigProvider


class TestFileHandling(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider.load_from_file('../file_processing_system.json')
        # ARRANGE
        self.valid_file_name = self._config['file_name']
        self.content = self._config['content']
        self.invalid_file_name = self._config['invalid_file_name']

    #-----------------------------------------------------------------------------------------
    def test_create_file(self):
        # ACT
        created_file = FileProcessingSystem().create_file_write(self.valid_file_name, self.content)
        # ASSERT
        self.assertEqual(created_file, self.content)

    #-----------------------------------------------------------------------------------------
    def test_load_from_file_valid(self):
        # ACT
        loaded_file = FileProcessingSystem().load_from_file_read(self.valid_file_name)
        # ASSERT
        self.assertEqual(loaded_file, self.content)

    #-----------------------------------------------------------------------------------------

    def test_load_from_file_invalid(self):
        # ACT
        with self.assertRaises(CustomException) as cm:
            FileProcessingSystem().load_from_file_read(self.invalid_file_name)
        # ASSERT
        self.assertEqual(str(cm.exception), f"File {self.invalid_file_name} not found.")



if __name__ == '__main__':
    unittest.main()
