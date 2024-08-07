import random
import string

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
    def waiting_fun(action, expected, time, retries):
        result = action
        while action != expected and retries > 0:
            return action
            retries = retries - 1
            time.sleep(time)
        return result





# this class in infra because it can be used all around the world
# not only for a specific website or app.
