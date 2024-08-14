import random

class StatusGenerate:

    @staticmethod
    def generate_a_status():
        statuses = ["available", "pending", "sold"]
        return random.choice(statuses)



