import json
import logging
from object_oriented_programing.pet_management_system.src.utilities.config_provider import ConfigProvider


class Owner:
    """
    Class for storing owner details
    """

    def __init__(self, name, phone, pets=None):
        self.name = name
        self.phone = phone
        self.pets = pets if pets is not None else []
        self._load_config_path = "../../pet_store_management.json"
        self._load_config = ConfigProvider().load_from_file(self._load_config_path)
        # self._save_config_path = "../../pet_store_management.json"
        # self._save_config = ConfigProvider().create_a_file(self._save_config_path)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def pets(self):
        return self._pets

    @pets.setter
    def pets(self, value):
        self._pets = value

    def __str__(self):
        try:
            logging.info("Listing owner details")
            return f' Owner: {self.name} is an owner with phone number: {self.phone}'
        except Exception as e:
            logging.error(f"Error listing owner details: {e}")

    def owner_to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "pets": [pet.pet_to_dict() for pet in self.pets]
        }

    def add_owner(self):
        try:
            logging.info("Adding new owner")
            with open(self._load_config_path, '+') as file:
                json.dump({"owners": [self.owner_to_dict()]}, file, indent=1)
                self._load_config.save_to_file(self._load_config_path)
                logging.info(f"Owner was added and data saved to json")
        except Exception as e:
            logging.error(f"Error adding and saving owner: {e}")

    # Open delete and load functions.
    # def delete_owner(self, owner):
    #     try:
    #         logging.info("Deleting owner")
    #         if owner in self._config.get["owners", []]:
    #             self._config["owners"].remove(owner)
    #             with open(self._config_path, 'a') as file:
    #                 json.dump(self._config, file, indent=1)
    #                 logging.info(f"Owner was deleted and data saved to json")
    #         else:
    #             logging.info(f"Owner not found: {owner}")
    #             raise ValueError(f"Owner not found: {owner}")
    #     except Exception as e:
    #         logging.error(f"Error deleting owner: {e}")

    # def load_owner(self):
    #     from object_oriented_programing.pet_management_system.src.classes.pet import Pet
    #     try:
    #         with open(self._load_config, 'r') as file:
    #             data = json.load(file)
    #             self.name = data['name']
    #             self.phone = data['phone']
    #             self.pets = [Pet(**pet_data) for pet_data in data['pets']]
    #             return self
    #     except FileNotFoundError:
    #         raise 'File not found.'
    #     except Exception as e:
    #         print(f"Error loading owner: {e}")
    #         return selfsdsd


if __name__ == "__main__":
    from object_oriented_programing.pet_management_system.src.classes.pet import Pet

    pet_1 = Pet('rex', 'dog', 5, '1', True)
    pet_2 = Pet('boby', 'dog', 9, '1', False)
    owner_1 = Owner('john', '0523362356', [pet_1, pet_2])
    owner_2 = Owner('mark', '2256523262', [pet_1])
    owner_2.add_owner()
    owner_1.add_owner()


