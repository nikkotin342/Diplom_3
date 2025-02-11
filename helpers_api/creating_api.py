import requests
import random
import string

from helpers.url import *

class User:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def new_email(self):
        email = f'{self.generate_random_string(5)}@mail.ru'
        return email

    def new_name_password(self):
        name = f'{self.generate_random_string(10)}'
        return name

    def create_user(self):
        payload = {'email': self.new_email(),
                   'password': self.new_name_password(),
                   'name': self.new_name_password()}
        requests.post(f'{BASE_URL}{CREATE_USER}', data=payload)
        return payload