import random
import string
import time

class Utils:

    @staticmethod
    def generate_random_string(length) -> str:
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join((random.choice(letters) for i in range(length)))

    @staticmethod
    def generate_random_number(length) -> str:
        numbers = string.digits
        return ''.join((random.choice(numbers) for i in range(length)))

    @staticmethod
    def wait_for_action(action, sleep_time, retries):
        result = action
        while retries > 0:
            if result:
                return True
            result = action
            time.sleep(sleep_time)
            retries -= retries
        return False





# this class in infra because it can be used all around the world
# not only for a specific website or app.
