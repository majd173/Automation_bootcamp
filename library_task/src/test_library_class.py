
import unittest
from Personal_Library_Manager import MyLibrary, Book
from library_task.src.App import library_file_path


class TestLibraryClass(unittest.TestCase):

    def test_book_exist(self):
        book = Book("majd", 555, "bader", "drama", 8888, "aaaa")
        MyLibrary.add_book(book)
        library = MyLibrary.load_library(library_file_path)

        self.assertIn(book, library, "Not found")


if __name__ == '__main__':
    unittest.main()
