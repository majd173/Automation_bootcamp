import logging

from object_oriented_progrmaing.pet_management_system.pet import Pet


class Dog(Pet):
    def __init__(self, breed):
        self.breed = breed


    def __str__(self):
        try:
            logging.info("Listing dog details")
            return f'Dog: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}, {self.breed}'
        except Exception as e:
            logging.error(f"Error listing dog details: {e}")






