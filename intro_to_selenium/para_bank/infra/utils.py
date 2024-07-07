import random
import string

class Utils:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join((random.choice(letters) for i in range(length)))

    @staticmethod
    def generate_random_number(length):
        letters = string.digits
        return ''.join((random.choice(letters) for i in range(length)))





# this class in infra because it can be used all around the world
# not only for a specific website or app.