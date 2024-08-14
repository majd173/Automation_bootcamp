from error_handling_projects.file_processing_system.custom_exceptions import CustomException
from error_handling_projects.file_processing_system.file_processing_system import FileProcessingSystem


def main():
    """
    This is the main function.
    The customer can choose to read from a file or write to a file.
    """
    try:
        print("Hello! please choose an option:\n"
              "r = Read from file\n"
              "w = Write to file")
        # Inserting file name and option (r or w)
        file_name = input("File name: ").lower()
        option = input("Option (r/w): ").lower()
        FileProcessingSystem().open_file(file_name, option)
        if option == 'r':
            FileProcessingSystem().open_file_and_read(file_name)
        elif option == 'w':
            content = input("Content: ")
            FileProcessingSystem().create_file_and_write(file_name, content)
        else:
            raise CustomException("Invalid option, must be 'r' or 'w'.")
    # Catching keyboard interrupt.
    except KeyboardInterrupt:
        raise CustomException("Invalid input.")
    # Catching all other exceptions.
    except Exception:
        raise CustomException("An error occurred (maybe an invalid mode input)")
    finally:
        print("Goodbye!")


if __name__ == '__main__':
    main()
