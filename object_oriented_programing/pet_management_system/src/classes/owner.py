import json
import logging
from pet_management_system.src.utilities.config_provider import ConfigProvider


class Owner:
    """
    Class for storing owner details
    """

    def __init__(self, name, phone, pets=None):
        self.name = name
        self.phone = phone
        if pets is None:
            pets = []
        self.pets = pets
        self._config_path = "../../pet_store.json"
        self._config = ConfigProvider().load_from_file(self._config_path)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):  # Use isinstance() instead of checking type directly
            raise TypeError("Name must be a string")
        elif value is None:  # This check is redundant since isinstance will cover None
            raise ValueError("Name cannot be None")
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
            from pet_management_system.src.classes.pet import Pet
            logging.info("Adding new owner")
            with open(self._config_path, 'r') as file:
                data = json.load(file)
                # Ensure data structure
                if "owners" not in data:
                    data["owners"] = []
                if "pets" not in data:
                    data["pets"] = []

                # Append new owner
                added_owner = self.owner_to_dict()
                if self.name not in [owner["name"] for owner in data["owners"]]:
                    data["owners"].append(added_owner)
                else:
                    logging.error(f"Owner already exists: {self.name}")
                    raise ValueError(f"Owner already exists: {self.name}")

                # Append new pets if not already present
                existing_pets = {pet["name"]: pet for pet in data["pets"]}
                for pet in self.pets:
                    pet_dict = pet.pet_to_dict()
                    if pet.name not in existing_pets:
                        data["pets"].append(pet_dict)
                    else:
                        logging.error(f"Pet already exists: {pet.name}")
                        raise ValueError(f"Pet already exists: {pet.name}")
            with open(self._config_path, 'w') as file:
                json.dump(data, file, indent=1)
                logging.info(f"Owner/s And Pet/s were added and data saved to json")
        except Exception as e:
            logging.error(f"Error adding and saving owner: {e}")

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


if __name__ == "__main__":
    from pet_management_system.src.classes.pet import Pet

    pet_1 = Pet('aaa', 'dog', 5, '1', True)
    pet_2 = Pet('boby', 'dog', 9, '1', False)
    owner_1 = Owner('john', '0523362356', [pet_1, pet_2])
    owner_2 = Owner('mark', '2256523262', [pet_1])
    owner_2.add_owner()
    owner_1.add_owner()
