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
        file = None
        try:
            file = open(file_name, mode)
            yield file
        except ValueError:
            raise CustomException(f"Wrong input {mode}.")
        except PermissionError:
            raise CustomException(f"There are no enough permissions.")
        except FileNotFoundError:
            raise CustomException(f"File {file_name} not found.")
        except IOError:
            raise CustomException(f"File {file_name} not found.")
        finally:
            if file and not file.closed:
                file.close()

    #---------------------------------------------------------------------------------
    def load_from_file_read(self, file_name):
        with self.open_file(file_name, 'r') as file:
            # if file:
            content = file.read()
            print(f'File exists, reading the content of the file:\n{content}')
            return content
            # else:
            #     print("bye!")

    #---------------------------------------------------------------------------------

    def create_file_write(self, file_name, text):
        with self.open_file(file_name, 'w') as file:
            if file:
                file.write(text)
                if file:
                    print("File was written successfully.")
                    print(f'New written text: {text}')
                    return text
                else:
                    print("File was not written successfully.")
            else:
                print("aaaaa")
