from object_oriented_progrmaing.pet_management_system.pet import Pet
import logging


class Cat(Pet):

    def __init__(self, indoor):
        self.indoor = indoor

    def __str__(self):
        try:
            logging.info("Listing all pets in the store.")
            return f'Cat: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}, {self.indoor}'
        except Exception as e:
            logging.error(f"Error listing pets: {e}")
