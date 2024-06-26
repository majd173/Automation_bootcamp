import os
import sys
import unittest
from library_task.Personal_Library_Manager import MyLibrary, Book
from library_task.App import library_file_path


class TestLibraryClass(unittest.TestCase):

    def setUp(self):
        self.library = MyLibrary("Test Library")
        self.library_file_path = "test_library.json"

    def tearDown(self):
        if os.path.exists(self.library_file_path):
            os.remove(self.library_file_path)

    def test_book_exist(self):
        book = Book("majd", 555, "bader", "drama", 8888, "aaaa")
        loaded_library = MyLibrary.load_library(self.library_file_path)
        self.assertIn(book.__dict__, [b.__dict__ for b in loaded_library.books], "Not found")


if __name__ == '__main__':
    unittest.main()
