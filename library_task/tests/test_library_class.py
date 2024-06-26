import os
import unittest
from library_task.Personal_Library_Manager import MyLibrary, Book
from library_task.App import library_file_path


class TestLibraryClass(unittest.TestCase):

    # def setUp(self):
    #     self.library = MyLibrary("Test Library")
    #     self.library_file_path = "test_library.json"
    #
    # def tearDown(self):
    #     if os.path.exists(self.library_file_path):
    #         os.remove(self.library_file_path)

    def test_book_exist(self):
        book = Book("majd", 555, "bader", "drama", 8888, "aaaa")
        library = MyLibrary.add_book(book)
        library1 = MyLibrary.load_library(library_file_path)
        self.assertIn(book, library1, "book does not found")


if __name__ == '__main__':
    unittest.main()
