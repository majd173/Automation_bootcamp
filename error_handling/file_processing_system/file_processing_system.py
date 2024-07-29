from contextlib import contextmanager
from error_handling.file_processing_system.custom_exceptions import CustomException


class FileProcessingSystem:
    """
    This class is for handling errors in the file processing system.
    """

    def __init__(self):
        pass

    #---------------------------------------------------------------------------------

    @contextmanager
    def open_file(self, file_name, mode):
        """
        This function is used to open a file.
        """
        file = None
        try:
            file = open(file_name, mode)
            yield file
        except PermissionError:
            raise CustomException(f"There are no enough permissions.")
        except FileNotFoundError:
            raise CustomException(f"File {file_name} not found.")
        except Exception:
            raise CustomException("An error occurred (maybe an invalid mode input)")
        finally:
            if file and not file.closed:
                file.close()

    #---------------------------------------------------------------------------------
    def load_from_file_read(self, file_name):
        """
        This function is used to read from a file.
        :param file_name:
        :return:
        """
        with self.open_file(file_name, 'r') as file:
            content = file.read()
            print(f'File exists, reading the content of the file:\n{content}')
            return content

    #---------------------------------------------------------------------------------

    def create_file_write(self, file_name, text):
        """
        This function is used to write a file.
        """
        with self.open_file(file_name, 'w') as file:
            file.write(text)
            print("File was written successfully.")
            print(f'New written text: {text}')
            return text
