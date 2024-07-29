from error_handling.file_processing_system.custom_exceptions import CustomException
from error_handling.file_processing_system.file_processing_system import FileProcessingSystem


def main():
    try:
        print("Hello! please choose an option:\n"
              "r = Read from file\n"
              "w = Write to file")

        file_name = input("File name: ").strip().lower()
        option = input("Option (r/w): ").strip().lower()
        FileProcessingSystem().open_file(file_name, option)
        if option == 'r':
            FileProcessingSystem().load_from_file_read(file_name)
        elif option == 'w':
            content = input("Content: ")
            FileProcessingSystem().create_file_write(file_name, content)
    except KeyboardInterrupt:
        raise CustomException("Invalid input.")
    except Exception:
        raise CustomException("An error occurred.")
    finally:
        print("")


if __name__ == '__main__':
    main()
