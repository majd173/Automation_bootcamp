import random
import string

class Utils:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return  ''.join((random.choice(letters) for _ in range(length)))
# this class in infra because it can be used all around the world
# not only for a specific website or app.
