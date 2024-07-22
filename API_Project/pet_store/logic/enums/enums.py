import random


def generate_a_status():
    statuses = ["available", "pending", "sold"]
    return random.choice(statuses)


class Enums:
    pass