import unittest
from project.persistence.users_dao import *

class TestCustomer(unittest.TestCase):
    def test_get_users(self):
        users = get_users()
        print(users)
