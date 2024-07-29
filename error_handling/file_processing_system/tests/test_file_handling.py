import unittest

from error_handling.file_processing_system.custom_exceptions import CustomException
from error_handling.file_processing_system.file_processing_system import FileProcessingSystem
from error_handling.file_processing_system.config_provider import ConfigProvider


class TestFileHandling(unittest.TestCase):
    """
    This class is for testing file handling.
    """

    def setUp(self):
        """
        Setting up the test environment.
        """
        self._config = ConfigProvider.load_from_file('../file_processing_system.json')
        # ARRANGE
        self.valid_file_name = self._config['file_name']
        self.content = self._config['content']
        self.invalid_file_name = self._config['invalid_file_name']

    #-----------------------------------------------------------------------------------------
    def test_create_file(self):
        """
        Test create file.
        :return : a new created file .
        """
        # ACT
        created_file = FileProcessingSystem().create_file_and_write(self.valid_file_name, self.content)
        # ASSERT
        self.assertEqual(created_file, self.content)

    #-----------------------------------------------------------------------------------------
    def test_load_from_file_valid(self):
        """
        Test load from file.
        """
        # ACT
        loaded_file = FileProcessingSystem().open_file_and_read(self.valid_file_name)
        # ASSERT
        self.assertEqual(loaded_file, self.content)

    #-----------------------------------------------------------------------------------------

    def test_load_from_file_invalid(self):
        """
        Test load from file.
        """
        # ACT
        with self.assertRaises(CustomException) as ce:
            FileProcessingSystem().open_file_and_read(self.invalid_file_name)
        self.assertEqual(str(ce.exception), self._config['error_content'])


if __name__ == '__main__':
    unittest.main()
