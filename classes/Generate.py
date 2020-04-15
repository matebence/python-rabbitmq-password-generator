from __future__ import print_function

import base64
import os
import hashlib


class Generate:
    __password = None

    def __init__(self, password):
        self.__password = password

    def rabbitmq_password(self, encoding, rand_salt_number):
        salt = os.urandom(rand_salt_number)
        salted_password = salt + self.__password.encode(encoding)
        sha256_password = hashlib.sha256(salted_password).digest()
        salted_hash = salt + sha256_password
        password_hash = base64.b64encode(salted_hash)

        return password_hash.decode(encoding)
