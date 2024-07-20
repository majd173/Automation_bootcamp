

class PetDetails:

    # This class manages adding a new pet by adding its details.
    def __init__(self, pet_id, pet_name):
        self._pet_id = pet_id
        self._pet_name = pet_name


    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value

    @property
    def pet_name(self):
        return self.pet_name

    @pet_name.setter
    def pet_name(self, value):
        self._pet_name = value


    def to_dic(self):

        return {
                "id": self._pet_id,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": self._pet_name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }

