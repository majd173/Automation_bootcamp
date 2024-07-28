import json


class ConfigProvider:
    # no constructor because this class only submits actions

    @staticmethod
    def load_from_file(filename):
        try: # with opening files always we usr -try-
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")

