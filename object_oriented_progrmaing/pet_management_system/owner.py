import logging

from object_oriented_progrmaing.pet_management_system.pet import Pet


class Owner:
    """
    Class for storing owner details
    """

    def __init__(self, name, phone, pets):
        self.name = name
        self.phone = phone
        self.pets = pets
        self.owners = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, value):
        self.phone = value

    @property
    def pets(self):
        return self.pets

    @pets.setter
    def pets(self, value):
        self.pets = value

    def __str__(self):
        try:
            logging.info("Listing owner details")
            return f' Owner: {self.name}, {self.phone}, {self.pets}'
        except Exception as e:
            logging.error(f"Error listing owner details: {e}")

    def add_owner(self, owner: 'Owner'):
        try:
            logging.info("Adding a new owner")
            self.owners.append(owner)
        except Exception as e:
            logging.error(f"Error adding owner: {e}")

    def add_pet(self, pet: Pet):
        try:
            logging.info("Adding a new pet)")
            self.pets.append(pet)
        except Exception as e:
            logging.error(f"Error adding pet: {e}")

    def remove_pet(self, pet: Pet):
        try:
            logging.info("Removing a pet")
            self.pets.remove(pet)
        except Exception as e:
            logging.error(f"Error removing pet: {e}")
