import json
import logging
from object_oriented_programing.pet_management_system.infra.config_provider import ConfigProvider
from object_oriented_programing.pet_management_system.pet import Pet


class Owner:
    """
    Class for storing owner details
    """

    def __init__(self, name, phone, pets):
        self.name = name
        self.phone = phone
        self.pets = pets
        self._config = ConfigProvider().load_from_file(
            r'C:\Users\Admin\Desktop\Automation_bootcamp\object_oriented_programing\pet_management_system\pet_store_management.json')

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
            return f' Owner: {self.name}, {self.phone}, {self.pets}'
        except Exception as e:
            logging.error(f"Error listing owner details: {e}")

    def add_owner(self):
        try:
            logging.info("Adding a new owner")
            owner_dict = {'name': self.name, 'phone': self.phone, 'pets': self.pets}
            return owner_dict
        except Exception as e:
            logging.error(f"Error adding owner: {e}")


    def save_owner(self, owner_file_path):
        try:
            owner_data = self.add_owner()
            if owner_data is not None:
                with open(owner_file_path, 'w') as file:
                    json.dump({'owners': [owner_data]}, file, indent=1)
                    logging.info(f"Owner data saved to {owner_file_path}")
            else:
                logging.error("No owner data to save.")
        except Exception as e:
            logging.error(f"Error saving owner: {e}")


    def load_owner(self, owner_file_path):
        try:
            with open(owner_file_path, 'r') as file:
                data = json.load(file)
                self.name = data['name']
                self.phone = data['phone']
                self.pets = [Pet(**pet_data) for pet_data in data['pets']]
                return self
        except FileNotFoundError:
            return self
        except Exception as e:
            print(f"Error loading owner: {e}")
            return self

man = Owner('Man', '1234567890', [])
man.save_owner(r'C:\Users\Admin\Desktop\Automation_bootcamp\object_oriented_programing\pet_management_system\pet_store_management.json')
