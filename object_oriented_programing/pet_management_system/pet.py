import json
import logging
from object_oriented_programing.pet_management_system.infra.config_provider import ConfigProvider
# from object_oriented_progrmaing.pet_management_system.owner import Owner


class Pet:

    def __init__(self, name, species, age, owner, vaccinated):
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self._vaccinated = vaccinated
        self._config = ConfigProvider().load_from_file(
            r'C:\Users\Admin\Desktop\Automation_bootcamp\object_oriented_programing\pet_management_system\pet_store_management.json')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, value):
        self._vaccinated = value

    def __str__(self):
        try:
            logging.info("listing pet details")
            return f'Pet: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}'
        except Exception as e:
            logging.error(f"Error listing pet details: {e}")

    def __eq__(self, other):
        try:
            logging.info("Checking if pets ar equal.")
            if self.name == other.name and self.species == other.species:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f'Error checking if pets are equal: {e}')

    def add_pet(self):
        try:
            logging.info("Adding a new pet")
            pet_dict = {'name': self.name, 'species': self.species,
                        'age': self.age, 'owner': self.owner,
                        'vaccinated': self._vaccinated}
            return pet_dict
        except Exception as e:
            logging.error(f"Error adding a new pet: {e}")

    def total_pets_count(self):
        try:
            logging.info("Counting total pets")
            total_pets = len(self._config['pets'])
            return total_pets
        except Exception as e:
            logging.error(f"Error counting total pets: {e}")

    def check_pet_is_vaccinated(self):
        try:
            logging.info("Checking pet is vaccinated")
            return self._vaccinated
        except Exception as e:
            logging.error(f"Error checking pet is vaccinated: {e}")

    def set_pet_vaccinated(self):
        try:
            logging.info("Setting pet as vaccinated")
            self._vaccinated = True
        except Exception as e:
            logging.error(f"Error setting pet as vaccinated: {e}")

    def age_retrieve(self):
        try:
            logging.info("Retrieving pet age")
            return self.age * 7
        except Exception as e:
            logging.error(f"Error retrieving pet age: {e}")

    def save_store(self, pet_file_path):
        try:
            with open(pet_file_path, 'w') as file:
                json.dump(
                    self._config['owners']['pets'][self.add_pet()], file, indent=1)
        except Exception as e:
            print(f"Error saving pet: {e}")

    def load_store(self, pet_file_path):
        try:
            with open(pet_file_path, 'r') as file:
                data = json.load(file)
                self.name = data['name']
                self.species = data['species']
                self.age = data['age']
                self.owner = data['owner']
                self._vaccinated = data['vaccinated']
                return self
        except FileNotFoundError:
            return self
        except Exception as e:
            print(f"Error loading pet: {e}")
            return self


# hello = Pet('hello', 4, 9, 'kyle', True)
# print(hello)