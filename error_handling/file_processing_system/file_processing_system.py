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
        try:
            file = open(file_name, mode)
            yield file
        except ValueError:
            raise CustomException(f"Wrong input mode: {mode}.")
        except PermissionError:
            raise CustomException(f"There are no enough permissions.")
        except FileNotFoundError:
            raise CustomException(f"File {file_name} not found.")
        except Exception:
            raise CustomException("An error occurred while opening the file.")
        finally:
            file.close()

    #---------------------------------------------------------------------------------
    def open_file_and_read(self, file):
        """
        This function is used to read from a file.

        """

        try:
            with self.open_file(file, 'r') as file:
                content = file.read()
                print(f'File exists, reading the content of the file:\n{content}')
                return content
        except FileNotFoundError:
            raise CustomException(f"File {file} not found.")
        except CustomException as ce:
            raise ce

    #---------------------------------------------------------------------------------

    def create_file_and_write(self, file, text):
        """
        This function is used to write a file.
        """

        try:
            with self.open_file(file, 'w') as file:
                file.write(text)
                print("File was written successfully.")
                print(f'New written text: {text}')
                return text
        except FileNotFoundError:
            raise CustomException(f"File {file} not found.")
        except Exception:
            raise CustomException("An error occurred (maybe an invalid mode input)")

