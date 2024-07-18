class OrderDetails:

    def __init__(self, order_id, pet_id, quantity):
        self._order_id = order_id
        self._pet_id = pet_id
        self._quantity = quantity
        self._shipDate = "2024-07-18T09:30:07.406+0000"
        self._status = "placed"
        self._complete = True

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def to_dict(self):
        """
        Converts the OrderDetails instance to a dictionary.
        """
        return {
            "id": self.order_id,
            "petId": self.pet_id,
            "quantity": self.quantity,
            "shipDate": "2024-07-18T09:30:07.406+0000",
            "status": "placed",
            "complete": True
        }
