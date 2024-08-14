from oop_projects.pet_management_system.src.classes.pet import Pet
import logging


class Cat(Pet):

    def __init__(self, name, species, age, owner, vaccinated, indoor):
        super().__init__(name, species, age, owner, vaccinated)
        self.indoor = indoor

    @property
    def indoor(self):
        return self.indoor

    @indoor.setter
    def indoor(self, value):
        self.indoor = value

    def __str__(self):
        try:
            logging.info("Listing all pets in the store.")
            return f'Cat: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}, {self.indoor}'
        except Exception as e:
            logging.error(f"Error listing pets: {e}")


